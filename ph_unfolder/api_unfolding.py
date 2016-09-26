#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

__author__ = "Yuji Ikeda"

import numpy as np
from phonopy import Phonopy
from phonopy.structure.symmetry import Symmetry
from phonopy.structure.cells import get_supercell, get_primitive
from ph_unfolder.harmonic.dynamical_matrix import (
        UnfolderDynamicalMatrix as DynamicalMatrix)
from phonopy.units import VaspToTHz
from ph_unfolder.phonon.band_structure import BandStructure
from ph_unfolder.phonon.single_point import SinglePoint
from ph_unfolder.phonon.mesh_unfolding import MeshUnfolding
# from ph_unfolder.dos_unfolding import TotalDos, PartialDos
from ph_unfolder.phonon.dos_unfolding import TotalDosUnfolding
from ph_unfolder.phonon.density_extractor import DensityExtractor

class PhonopyUnfolding(Phonopy):
    """

    unitcell: before symmetrization
    """
    def __init__(self,
                 unitcell,
                 unitcell_ideal,
                 supercell_matrix,
                 primitive_matrix_ideal,
                 nac_params=None,
                 distance=0.01,
                 factor=VaspToTHz,
                 is_auto_displacements=True,
                 dynamical_matrix_decimals=None,
                 force_constants_decimals=None,
                 dict_spectrum=None,
                 star="none",
                 mode="eigenvector",
                 symprec=1e-5,
                 is_symmetry=True,
                 use_lapack_solver=False,
                 log_level=0):
        self._symprec = symprec
        self._distance = distance
        self._factor = factor
        self._is_auto_displacements = is_auto_displacements
        self._is_symmetry = is_symmetry
        self._use_lapack_solver = use_lapack_solver
        self._log_level = log_level

        # self.create_density_extractor(dict_spectrum)
        self._density_extractor = None

        # Create supercell and primitive cell
        self._unitcell = unitcell
        self._unitcell_ideal = unitcell_ideal
        self._supercell_matrix = supercell_matrix
        self._primitive_matrix = None
        self._primitive_matrix_ideal = primitive_matrix_ideal
        self._supercell = None
        self._primitive = None
        self._build_supercell()
        self._build_primitive_cell()
        self._build_supercell_ideal()
        self._build_primitive_cell_ideal()

        # Set supercell and primitive symmetry
        self._symmetry = None
        self._primitive_symmetry = None
        self._search_symmetry()
        self._search_primitive_symmetry()
        self._search_symmetry_ideal()
        self._search_primitive_symmetry_ideal()

        # set_force_constants or set_forces
        self._force_constants = None
        self._force_constants_decimals = force_constants_decimals

        # set_dynamical_matrix
        self._dynamical_matrix = None
        self._nac_params = nac_params
        self._dynamical_matrix_decimals = dynamical_matrix_decimals

        # set_band_structure
        self._band_structure = None

        # set_mesh
        self._mesh = None

        # set_tetrahedron_method
        self._tetrahedron_method = None

        # set_thermal_properties
        self._thermal_properties = None

        # set_thermal_displacements
        self._thermal_displacements = None

        # set_thermal_displacement_matrices
        self._thermal_displacement_matrices = None

        # set_partial_DOS
        self._pdos = None

        # set_total_DOS
        self._total_dos = None

        # set_modulation
        self._modulation = None

        # set_character_table
        self._irreps = None

        # set_group_velocity
        self._group_velocity = None

        self._star = star
        self._mode = mode

    def create_density_extractor(self, dict_spectrum):
        self._density_extractor = DensityExtractor(
            function=dict_spectrum["function"],
            fmin=dict_spectrum["freq_min"],
            fmax=dict_spectrum["freq_max"],
            fpitch=dict_spectrum["freq_pitch"],
            sigma=dict_spectrum["sigma"],
        )

    # Single point
    def run_single_point(self, qpoint, distance):
        single_point = SinglePoint(
            qpoint,
            distance,
            dynamical_matrix=self._dynamical_matrix,
            unitcell_ideal=self._unitcell_ideal,
            primitive_matrix_ideal=self._primitive_matrix_ideal,
            density_extractor=self._density_extractor,
            factor=self._factor,
            star=self._star,
            mode=self._mode,
            verbose=True)

    # Band structure
    def set_band_structure(self,
                           bands,
                           is_eigenvectors=False,
                           is_band_connection=False):
        if self._dynamical_matrix is None:
            print("Warning: Dynamical matrix has not yet built.")
            self._band_structure = None
            return False

        self._band_structure = BandStructure(
            bands,
            self._dynamical_matrix,
            self._unitcell_ideal,
            self._primitive_matrix_ideal,
            density_extractor=self._density_extractor,
            is_eigenvectors=is_eigenvectors,
            is_band_connection=is_band_connection,
            group_velocity=self._group_velocity,
            factor=self._factor,
            star=self._star,
            mode=self._mode,
            verbose=True)
        return True

    # Sampling mesh
    def set_mesh(self,
                 mesh,
                 shift=None,
                 is_time_reversal=True,
                 is_mesh_symmetry=True,
                 is_eigenvectors=False,
                 is_gamma_center=False):
        if self._dynamical_matrix is None:
            print("Warning: Dynamical matrix has not yet built.")
            self._mesh = None
            return False

        # TODO(ikeda): Check how "rotations" works.
        self._mesh = MeshUnfolding(
            self._dynamical_matrix,
            self._unitcell_ideal,
            self._primitive_matrix_ideal,
            mesh,
            shift=shift,
            is_time_reversal=is_time_reversal,
            is_mesh_symmetry=is_mesh_symmetry,
            is_eigenvectors=is_eigenvectors,
            is_gamma_center=is_gamma_center,
            star=self._star,
            group_velocity=self._group_velocity,
            rotations=self._primitive_symmetry.get_pointgroup_operations(),
            factor=self._factor,
            use_lapack_solver=self._use_lapack_solver,
            mode=self._mode)
        return True

    # DOS
    def set_total_DOS(self,
                      sigma=None,
                      freq_min=None,
                      freq_max=None,
                      freq_pitch=None,
                      tetrahedron_method=False):

        if self._mesh is None:
            print("Warning: \'set_mesh\' has to finish correctly "
                  "before DOS calculation.")
            self._total_dos = None
            return False

        total_dos = TotalDosUnfolding(
            self._mesh,
            sigma=sigma,
            tetrahedron_method=tetrahedron_method)
        total_dos.set_draw_area(freq_min, freq_max, freq_pitch)
        total_dos.run()
        self._total_dos = total_dos
        return True

    def _set_dynamical_matrix(self):
        self._dynamical_matrix = None

        if (self._supercell is None or self._primitive is None):
            print("Bug: Supercell or primitive is not created.")
            return False
        elif self._force_constants is None:
            print("Warning: Force constants are not prepared.")
            return False
        elif self._primitive.get_masses() is None:
            print("Warning: Atomic masses are not correctly set.")
            return False
        else:
            if self._nac_params is None:
                self._dynamical_matrix = DynamicalMatrix(
                    self._supercell,
                    self._primitive,
                    self._force_constants,
                    decimals=self._dynamical_matrix_decimals,
                    symprec=self._symprec)
            else:
                raise ValueError(
                'Currently NAC is not available for unfolding.')
            return True

    def _search_symmetry_ideal(self):
        self._symmetry = Symmetry(self._supercell_ideal,
                                  self._symprec,
                                  self._is_symmetry)

    def _search_primitive_symmetry_ideal(self):
        self._primitive_symmetry = Symmetry(self._primitive_ideal,
                                            self._symprec,
                                            self._is_symmetry)
        
        if (len(self._symmetry.get_pointgroup_operations()) !=
            len(self._primitive_symmetry.get_pointgroup_operations())):
            print("Warning: Point group symmetries of supercell and primitive"
                  "cell are different.")

    def _build_supercell_ideal(self):
        self._supercell_ideal = get_supercell(self._unitcell_ideal,
                                        self._supercell_matrix,
                                        self._symprec)

    def _build_primitive_cell_ideal(self):
        """
        primitive_matrix:
          Relative axes of primitive cell to the input unit cell.
          Relative axes to the supercell is calculated by:
             supercell_matrix^-1 * primitive_matrix
          Therefore primitive cell lattice is finally calculated by:
             (supercell_lattice * (supercell_matrix)^-1 * primitive_matrix)^T
        """

        inv_supercell_matrix = np.linalg.inv(self._supercell_matrix)
        if self._primitive_matrix_ideal is None:
            trans_mat = inv_supercell_matrix
        else:
            trans_mat = np.dot(inv_supercell_matrix, self._primitive_matrix_ideal)
        self._primitive_ideal = get_primitive(
            self._supercell_ideal, trans_mat, self._symprec)
        num_satom = self._supercell_ideal.get_number_of_atoms()
        num_patom = self._primitive_ideal.get_number_of_atoms()
        if abs(num_satom * np.linalg.det(trans_mat) - num_patom) < 0.1:
            return True
        else:
            return False

    def average_masses(self):
        # TODO(ikeda): Now atomic order is supposed to be the same, which should be modified.
        symbols_ideal = self._unitcell_ideal.get_chemical_symbols()
        reduced_symbols_ideal = sorted(set(symbols_ideal), key=symbols_ideal.index)
        masses = self._unitcell.get_masses()
        masses_average = np.zeros_like(masses)
        for rs in reduced_symbols_ideal:
            indices = np.char.strip((symbols_ideal)) == np.char.strip(rs)
            mass_average = np.average(masses[indices])
            masses_average[indices] = mass_average
        self._unitcell.set_masses(masses_average)

        self._build_supercell()
        self._build_primitive_cell()

        self._search_symmetry()
        self._search_primitive_symmetry()
