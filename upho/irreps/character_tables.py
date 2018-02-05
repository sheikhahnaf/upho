#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

Note
----
The order of point groups follows Table 12.1.4.2 in ITA2006.
"""
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

__author__ = "Yuji Ikeda"

import numpy as np


MAX_IRREPS = 12  # D_6h, temporary

r6 = np.exp(2.0j * np.pi / 6.0)
r3 = r6 ** 2

character_tables = {}
# 1(C_1)
character_tables['1'] = {
    'rotation_labels': ('E', ),
    'class_order_list': (1, ),
    'ir_labels': ('A', ),
    'character_table': (
        (1, ),
    )
}
# 2(C_i)
character_tables['-1'] = {
    'rotation_labels': ('E', 'i'),
    'class_order_list': (1, 1),
    'ir_labels': ('Ag', 'Au'),
    'character_table': (
        (1,  1),
        (1, -1),
    )
}
# 3(C_2)
character_tables['2'] = {
    'rotation_labels': ('E', 'C2'),
    'class_order_list': (1, 1),
    'ir_labels': ('A', 'B'),
    'character_table': (
        (1,  1),
        (1, -1),
    )
}
# 4(C_s)
character_tables['m'] = {
    'rotation_labels': ('E', 'sgh'),
    'class_order_list': (1, 1),
    'ir_labels': ('A\'', 'A\'\''),
    'character_table': (
        (1,  1),
        (1, -1),
    ),
    'class_to_rotations_list': [
        # Improper rotation axis: x
        {
            'E'    : ((( 1,  0,  0),
                       ( 0,  1,  0),
                       ( 0,  0,  1),),),
            'sgh'  : (((-1,  0,  0),
                       ( 0,  1,  0),
                       ( 0,  0,  1),),)
        },
        # Improper rotation axis: y
        {
            'E'    : ((( 1,  0,  0),
                       ( 0,  1,  0),
                       ( 0,  0,  1),),),
            'sgh'  : ((( 1,  0,  0),
                       ( 0, -1,  0),
                       ( 0,  0,  1),),)
        },
        # Improper rotation axis: z
        {
            'E'    : ((( 1,  0,  0),
                       ( 0,  1,  0),
                       ( 0,  0,  1),),),
            'sgh'  : ((( 1,  0,  0),
                       ( 0,  1,  0),
                       ( 0,  0, -1),),)
        },
    ]
}
# 5(C_2h)
character_tables['2/m'] = {
    'rotation_labels': ('E', 'C2', 'i', 'sgh'),
    'class_order_list': (1, 1, 1, 1),
    'ir_labels': ('Ag', 'Bg', 'Au', 'Bu'),
    'character_table': (
        (1,  1,  1,  1),
        (1, -1,  1, -1),
        (1,  1, -1, -1),
        (1, -1, -1,  1),
    ),
    'class_to_rotations_list': [
        # Proper rotation axis: x
        {
            'E'    : ((( 1,  0,  0),
                       ( 0,  1,  0),
                       ( 0,  0,  1),),),
            'C2'   : ((( 1,  0,  0),
                       ( 0, -1,  0),
                       ( 0,  0, -1),),),
            'i'    : (((-1,  0,  0),
                       ( 0, -1,  0),
                       ( 0,  0, -1),),),
            'sgh'  : (((-1,  0,  0),
                       ( 0,  1,  0),
                       ( 0,  0,  1),),)
        },
        # Proper rotation axis: y
        {
            'E'    : ((( 1,  0,  0),
                       ( 0,  1,  0),
                       ( 0,  0,  1),),),
            'C2'   : (((-1,  0,  0),
                       ( 0,  1,  0),
                       ( 0,  0, -1),),),
            'i'    : (((-1,  0,  0),
                       ( 0, -1,  0),
                       ( 0,  0, -1),),),
            'sgh'  : ((( 1,  0,  0),
                       ( 0, -1,  0),
                       ( 0,  0,  1),),)
        },
        # Proper rotation axis: z
        {
            'E'    : ((( 1,  0,  0),
                       ( 0,  1,  0),
                       ( 0,  0,  1),),),
            'C2'   : (((-1,  0,  0),
                       ( 0, -1,  0),
                       ( 0,  0,  1),),),
            'i'    : (((-1,  0,  0),
                       ( 0, -1,  0),
                       ( 0,  0, -1),),),
            'sgh'  : ((( 1,  0,  0),
                       ( 0,  1,  0),
                       ( 0,  0, -1),),)
        },
    ]
}
# 6(D_2)
character_tables['222'] = {
    'rotation_labels': ('E', 'C2', 'C2x', 'C2y'),
    'class_order_list': (1, 1, 1, 1),
    'ir_labels': ('A', 'B1', 'B2', 'B3'),
    'character_table': (
        (1,  1,  1,  1),
        (1,  1, -1, -1),
        (1, -1, -1,  1),
        (1, -1,  1, -1),
    )
}
# 7(C_2v)
character_tables['mm2'] = {
    'rotation_labels': ('E', 'C2', 'sgv', 'sgv\''),
    'class_order_list': (1, 1, 1, 1),
    'ir_labels': ('A1', 'A2', 'B1', 'B2'),
    'character_table': (
        (1,  1,  1,  1),
        (1,  1, -1, -1),
        (1, -1,  1, -1),
        (1, -1, -1,  1),
    ),
    'class_to_rotations_list': [
        # Proper rotation axis: x
        {
            'E'    : ((( 1,  0,  0),
                       ( 0,  1,  0),
                       ( 0,  0,  1),),),
            'C2'   : ((( 1,  0,  0),
                       ( 0, -1,  0),
                       ( 0,  0, -1),),),
            'sgv'  : ((( 1,  0,  0),
                       ( 0, -1,  0),
                       ( 0,  0,  1),),),
            'sgv\'': ((( 1,  0,  0),
                       ( 0,  1,  0),
                       ( 0,  0, -1),),)
        },
        # Proper rotation axis: y
        {
            'E'    : ((( 1,  0,  0),
                       ( 0,  1,  0),
                       ( 0,  0,  1),),),
            'C2'   : (((-1,  0,  0),
                       ( 0,  1,  0),
                       ( 0,  0, -1),),),
            'sgv'  : ((( 1,  0,  0),
                       ( 0,  1,  0),
                       ( 0,  0, -1),),),
            'sgv\'': (((-1,  0,  0),
                       ( 0,  1,  0),
                       ( 0,  0,  1),),)
        },
        # Proper rotation axis: z
        {
            'E'    : ((( 1,  0,  0),
                       ( 0,  1,  0),
                       ( 0,  0,  1),),),
            'C2'   : (((-1,  0,  0),
                       ( 0, -1,  0),
                       ( 0,  0,  1),),),
            'sgv'  : (((-1,  0,  0),
                       ( 0,  1,  0),
                       ( 0,  0,  1),),),
            'sgv\'': ((( 1,  0,  0),
                       ( 0, -1,  0),
                       ( 0,  0,  1),),)
        },
    ]
}
# 8(D_2h)
character_tables['mmm'] = {
    'rotation_labels': ('E', 'C2', 'C2x', 'C2y', 'i', 'sgxy', 'sgxz', 'sgyz'),
    'class_order_list': (1, 1, 1, 1, 1, 1, 1, 1),
    'ir_labels': ('Ag', 'B1g', 'B2g', 'B3g', 'Au', 'B1u', 'B2u', 'B3u'),
    'character_table': (
        (1,  1,  1,  1,  1,  1,  1,  1),
        (1,  1, -1, -1,  1,  1, -1, -1),
        (1, -1, -1,  1,  1, -1,  1, -1),
        (1, -1,  1, -1,  1, -1, -1,  1),
        (1,  1,  1,  1, -1, -1, -1, -1),
        (1,  1, -1, -1, -1, -1,  1,  1),
        (1, -1, -1,  1, -1,  1, -1,  1),
        (1, -1,  1, -1, -1,  1,  1, -1),
    ),
    'class_to_rotations_list': [
        {
            'E'   : ((( 1,  0,  0),
                      ( 0,  1,  0),
                      ( 0,  0,  1),),),
            'C2'  : (((-1,  0,  0),
                      ( 0, -1,  0),
                      ( 0,  0,  1),),),
            'C2y' : (((-1,  0,  0),
                      ( 0,  1,  0),
                      ( 0,  0, -1),),),
            'C2x' : ((( 1,  0,  0),
                      ( 0, -1,  0),
                      ( 0,  0, -1),),),
            'i'   : (((-1,  0,  0),
                      ( 0, -1,  0),
                      ( 0,  0, -1),),),
            'sgxy': ((( 1,  0,  0),
                      ( 0,  1,  0),
                      ( 0,  0, -1),),),
            'sgxz': ((( 1,  0,  0),
                      ( 0, -1,  0),
                      ( 0,  0,  1),),),
            'sgyz': (((-1,  0,  0),
                      ( 0,  1,  0),
                      ( 0,  0,  1),),)
        },
    ]
}
# 9(C_4)
character_tables['4'] = {
    'rotation_labels': ('E', 'C4', 'C2', 'C4^3'),
    'class_order_list': (1, 1, 1, 1),
    'ir_labels': ('A', 'B', 'E', 'E'),
    'character_table': (
        (1,   1,  1,   1),
        (1,  -1,  1,  -1),
        (1,  1j, -1, -1j),
        (1, -1j, -1,  1j),
    ),
    'class_to_rotations_list': [
        {
            'E'   : ((( 1,  0,  0),
                      ( 0,  1,  0),
                      ( 0,  0,  1),),),
            'C4'  : ((( 0, -1,  0),
                      ( 1,  0,  0),
                      ( 0,  0,  1),),),
            'C2'  : (((-1,  0,  0),
                      ( 0, -1,  0),
                      ( 0,  0,  1),),),
            'C4^3': ((( 0,  1,  0),
                      (-1,  0,  0),
                      ( 0,  0,  1),),),
        },
    ]
}
# 13(C_4v)
character_tables['4mm'] = {
    'rotation_labels': ('E', 'C4', 'C2', 'sgv', 'sgd'),
    'class_order_list': (1, 2, 1, 2, 2),
    'ir_labels': ('A1', 'A2', 'B1', 'B2', 'E'),
    'character_table': (
        (1,  1,  1,  1,  1),
        (1,  1,  1, -1, -1),
        (1, -1,  1,  1, -1),
        (1, -1,  1, -1,  1),
        (2,  0, -2,  0,  0),
     ),
    'class_to_rotations_list': [
        {
            'E'     : ((( 1,  0,  0),
                        ( 0,  1,  0),
                        ( 0,  0,  1),),),
            'C4'    : ((( 0, -1,  0),
                        ( 1,  0,  0),
                        ( 0,  0,  1),),
                       (( 0,  1,  0),
                        (-1,  0,  0),
                        ( 0,  0,  1),),),
            'C2'    : (((-1,  0,  0),
                        ( 0, -1,  0),
                        ( 0,  0,  1),),),
            'sgv'   : (((-1,  0,  0),
                        ( 0,  1,  0),
                        ( 0,  0,  1),),
                       (( 1,  0,  0),
                        ( 0, -1,  0),
                        ( 0,  0,  1),),),
            'sgd'   : ((( 0,  1,  0),
                        ( 1,  0,  0),
                        ( 0,  0,  1),),
                       (( 0, -1,  0),
                        (-1,  0,  0),
                        ( 0,  0,  1),),)
        },
    ]
}
# 15(D_4h)
character_tables['4/mmm'] = {
    'rotation_labels': ('E', 'C4', 'C2', 'C2\'', 'C2\'\'',
                      'i', 'S4', 'sgh', 'sgv', 'sgd'),
    'class_order_list': (1, 2, 1, 2, 2, 1, 2, 1, 2, 2),
    'ir_labels': ('A1g', 'A2g', 'B1g', 'B2g', 'Eg',
                   'A1u', 'A2u', 'B1u', 'B2u', 'Eu'),
    'character_table': (
        (1,  1,  1,  1,  1,  1,  1,  1,  1,  1),
        (1,  1,  1, -1, -1,  1,  1,  1, -1, -1),
        (1, -1,  1,  1, -1,  1, -1,  1,  1, -1),
        (1, -1,  1, -1,  1,  1, -1,  1, -1,  1),
        (2,  0, -2,  0,  0,  2,  0, -2,  0,  0),
        (1,  1,  1,  1,  1, -1, -1, -1, -1, -1),
        (1,  1,  1, -1, -1, -1, -1, -1,  1,  1),
        (1, -1,  1,  1, -1, -1,  1, -1, -1,  1),
        (1, -1,  1, -1,  1, -1,  1, -1,  1, -1),
        (2,  0, -2,  0,  0, -2,  0,  2,  0,  0),
     ),
    'class_to_rotations_list': [
        {
            'E'     : ((( 1, 0, 0 ),
                        ( 0, 1, 0 ),
                        ( 0, 0, 1 ),),),
            'C4'    : ((( 0,-1, 0 ),
                        ( 1, 0, 0 ),
                        ( 0, 0, 1 ),),
                       (( 0, 1, 0 ),
                        (-1, 0, 0 ),
                        ( 0, 0, 1 ),),),
            'C2'    : (((-1, 0, 0 ),
                        ( 0,-1, 0 ),
                        ( 0, 0, 1 ),),),
            'C2\''  : ((( 1, 0, 0 ),
                        ( 0,-1, 0 ),
                        ( 0, 0,-1 ),),
                       ((-1, 0, 0 ),
                        ( 0, 1, 0 ),
                        ( 0, 0,-1 ),),),
            'C2\'\'': ((( 0, 1, 0 ),
                        ( 1, 0, 0 ),
                        ( 0, 0,-1 ),),
                       (( 0,-1, 0 ),
                        (-1, 0, 0 ),
                        ( 0, 0,-1 ),),),
            'i'     : (((-1, 0, 0 ),
                        ( 0,-1, 0 ),
                        ( 0, 0,-1 ),),),
            'S4'    : ((( 0, 1, 0 ),
                        (-1, 0, 0 ),
                        ( 0, 0,-1 ),),
                       (( 0,-1, 0 ),
                        ( 1, 0, 0 ),
                        ( 0, 0,-1 ),),),
            'sgh'   : ((( 1, 0, 0 ),
                        ( 0, 1, 0 ),
                        ( 0, 0,-1 ),),),
            'sgv'   : (((-1, 0, 0 ),
                        ( 0, 1, 0 ),
                        ( 0, 0, 1 ),),
                       (( 1, 0, 0 ),
                        ( 0,-1, 0 ),
                        ( 0, 0, 1 ),),),
            'sgd'   : ((( 0, 1, 0 ),
                        ( 1, 0, 0 ),
                        ( 0, 0, 1 ),),
                       (( 0,-1, 0 ),
                        (-1, 0, 0 ),
                        ( 0, 0, 1 ),),)
        },
    ]
}
# 19(C_3v)
character_tables['3m'] = {
    'rotation_labels': ('E', 'C3', 'sgv'),
    'class_order_list': (1, 2, 3),
    'ir_labels': ('A1', 'A2', 'E'),
    'character_table': (
        (1,  1,  1),
        (1,  1, -1),
        (2, -1,  0),
    ),
    'class_to_rotations_list': [
        {
            'E'  : ((( 1,  0,  0),
                     ( 0,  1,  0),
                     ( 0,  0,  1),),),
            'C3' : ((( 0, -1,  0),
                     ( 1, -1,  0),
                     ( 0,  0,  1),),
                    ((-1,  1,  0),
                     (-1,  0,  0),
                     ( 0,  0,  1),),),
            'sgv': ((( 0, -1,  0),
                     (-1,  0,  0),
                     ( 0,  0,  1),),
                    ((-1,  1,  0),
                     ( 0,  1,  0),
                     ( 0,  0,  1),),
                    (( 1,  0,  0),
                     ( 1, -1,  0),
                     ( 0,  0,  1),),)
        },
    ]
}
# 20(D_3d)
character_tables['-3m'] = {
    'rotation_labels': ('E', 'C3', 'C2', 'i', 'S6', 'sgd'),
    'class_order_list': (1, 2, 3, 1, 2, 3),
    'ir_labels': ('A1g', 'A2g', 'Eg', 'A1u', 'A2u', 'Eu'),
    'character_table': (
        (1,  1,  1,  1,  1,  1),
        (1,  1, -1,  1,  1, -1),
        (2, -1,  0,  2, -1,  0),
        (1,  1,  1, -1, -1, -1),
        (1,  1, -1, -1, -1,  1),
        (2, -1,  0, -2,  1,  0),
    ),
    'class_to_rotations_list': [
        # Second axis: Proper 2-fold axis
        {
            'E'  : ((( 1,  0,  0),
                     ( 0,  1,  0),
                     ( 0,  0,  1),),),
            'C3' : ((( 0, -1,  0),
                     ( 1, -1,  0),
                     ( 0,  0,  1),),
                    ((-1,  1,  0),
                     (-1,  0,  0),
                     ( 0,  0,  1),),),
            'C2' : ((( 0,  1,  0),
                     ( 1,  0,  0),
                     ( 0,  0, -1),),
                    (( 1, -1,  0),
                     ( 0, -1,  0),
                     ( 0,  0, -1),),
                    ((-1,  0,  0),
                     (-1,  1,  0),
                     ( 0,  0, -1),),),
            'i'  : (((-1,  0,  0),
                     ( 0, -1,  0),
                     ( 0,  0, -1),),),
            'S6' : ((( 0,  1,  0),
                     (-1,  1,  0),
                     ( 0,  0, -1),),
                    (( 1, -1,  0),
                     ( 1,  0,  0),
                     ( 0,  0, -1),),),
            'sgd': ((( 0, -1,  0),
                     (-1,  0,  0),
                     ( 0,  0,  1),),
                    ((-1,  1,  0),
                     ( 0,  1,  0),
                     ( 0,  0,  1),),
                    (( 1,  0,  0),
                     ( 1, -1,  0),
                     ( 0,  0,  1),),)
        },
        # Second axis: Improper 2-fold axis
        {
            'E'  : ((( 1,  0,  0),
                     ( 0,  1,  0),
                     ( 0,  0,  1),),),
            'C3' : ((( 0, -1,  0),
                     ( 1, -1,  0),
                     ( 0,  0,  1),),
                    ((-1,  1,  0),
                     (-1,  0,  0),
                     ( 0,  0,  1),),),
            'C2' : ((( 0, -1,  0),
                     (-1,  0,  0),
                     ( 0,  0, -1),),
                    ((-1,  1,  0),
                     ( 0,  1,  0),
                     ( 0,  0, -1),),
                    (( 1,  0,  0),
                     ( 1, -1,  0),
                     ( 0,  0, -1),),),
            'i'  : (((-1,  0,  0),
                     ( 0, -1,  0),
                     ( 0,  0, -1),),),
            'S6' : ((( 0,  1,  0),
                     (-1,  1,  0),
                     ( 0,  0, -1),),
                    (( 1, -1,  0),
                     ( 1,  0,  0),
                     ( 0,  0, -1),),),
            'sgd': ((( 0,  1,  0),
                     ( 1,  0,  0),
                     ( 0,  0,  1),),
                    (( 1, -1,  0),
                     ( 0, -1,  0),
                     ( 0,  0,  1),),
                    ((-1,  0,  0),
                     (-1,  1,  0),
                     ( 0,  0,  1),),)
        },
    ]
}
# 27(D_6h)
character_tables['6/mmm'] = {
    'rotation_labels': ('E', 'C6', 'C3', 'C2', 'C2\'', 'C2\'\'',
                      'i', 'S3', 'S6', 'sgh', 'sgd', 'sgv'),
    'class_order_list': (1, 2, 2, 1, 3, 3, 1, 2, 2, 1, 3, 3),
    'ir_labels': ('A1g', 'A2g', 'B1g', 'B2g', 'E1g', 'E2g',
                   'A1u', 'A2u', 'B1u', 'B2u', 'E1u', 'E2u'), 
    'character_table': (
        (1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1),
        (1,  1,  1,  1, -1, -1,  1,  1,  1,  1, -1, -1),
        (1, -1,  1, -1,  1, -1,  1, -1,  1, -1,  1, -1),
        (1, -1,  1, -1, -1,  1,  1, -1,  1, -1, -1,  1),
        (2,  1, -1, -2,  0,  0,  2,  1, -1, -2,  0,  0),
        (2, -1, -1,  2,  0,  0,  2, -1, -1,  2,  0,  0),
        (1,  1,  1,  1,  1,  1, -1, -1, -1, -1, -1, -1),
        (1,  1,  1,  1, -1, -1, -1, -1, -1, -1,  1,  1),
        (1, -1,  1, -1,  1, -1, -1,  1, -1,  1, -1,  1),
        (1, -1,  1, -1, -1,  1, -1,  1, -1,  1,  1, -1),
        (2,  1, -1, -2,  0,  0, -2, -1,  1,  2,  0,  0),
        (2, -1, -1,  2,  0,  0, -2,  1,  1, -2,  0,  0),
    ),
    'class_to_rotations_list': [
        {
            'E'     : ((( 1,  0,  0),
                        ( 0,  1,  0),
                        ( 0,  0,  1),),),
            'C6'    : ((( 1, -1,  0),
                        ( 1,  0,  0),
                        ( 0,  0,  1),),
                       (( 0,  1,  0),
                        (-1,  1,  0),
                        ( 0,  0,  1),),),
            'C3'    : ((( 0, -1,  0),
                        ( 1, -1,  0),
                        ( 0,  0,  1),),
                       ((-1,  1,  0),
                        (-1,  0,  0),
                        ( 0,  0,  1),),),
            'C2'    : (((-1,  0,  0),
                        ( 0, -1,  0),
                        ( 0,  0,  1),),),
            'C2\''  : ((( 0, -1,  0),
                        (-1,  0,  0),
                        ( 0,  0, -1),),
                       ((-1,  1,  0),
                        ( 0,  1,  0),
                        ( 0,  0, -1),),
                       (( 1,  0,  0),
                        ( 1, -1,  0),
                        ( 0,  0, -1),),),
            'C2\'\'': ((( 0,  1,  0),
                        ( 1,  0,  0),
                        ( 0,  0, -1),),
                       (( 1, -1,  0),
                        ( 0, -1,  0),
                        ( 0,  0, -1),),
                       ((-1,  0,  0),
                        (-1,  1,  0),
                        ( 0,  0, -1),),),
            'i'     : (((-1,  0,  0),
                        ( 0, -1,  0),
                        ( 0,  0, -1),),),
            'S3'    : (((-1,  1,  0),
                        (-1,  0,  0),
                        ( 0,  0, -1),),
                       (( 0, -1,  0),
                        ( 1, -1,  0),
                        ( 0,  0, -1),),),
            'S6'    : ((( 0,  1,  0),
                        (-1,  1,  0),
                        ( 0,  0, -1),),
                       (( 1, -1,  0),
                        ( 1,  0,  0),
                        ( 0,  0, -1),),),
            'sgh'   : ((( 1,  0,  0),
                        ( 0,  1,  0),
                        ( 0,  0, -1),),),
            'sgd'   : ((( 0,  1,  0),
                        ( 1,  0,  0),
                        ( 0,  0,  1),),
                       (( 1, -1,  0),
                        ( 0, -1,  0),
                        ( 0,  0,  1),),
                       ((-1,  0,  0),
                        (-1,  1,  0),
                        ( 0,  0,  1),),),
            'sgv'   : ((( 0, -1,  0),
                        (-1,  0,  0),
                        ( 0,  0,  1),),
                       ((-1,  1,  0),
                        ( 0,  1,  0),
                        ( 0,  0,  1),),
                       (( 1,  0,  0),
                        ( 1, -1,  0),
                        ( 0,  0,  1),),)
        },
    ]
}
# 31(T_d)
character_tables['-43m'] = {
    'rotation_labels': ('E', 'C3', 'C2', 'S4', 'sgd'),
    'class_order_list': (1, 8, 3, 6, 6),
    'ir_labels': ('A1', 'A2', 'E', 'T1', 'T2'),
    'character_table': (
        (1,  1,  1,  1,  1),
        (1,  1,  1, -1, -1),
        (2, -1,  2,  0,  0),
        (3,  0, -1,  1, -1),
        (3,  0, -1, -1,  1),
    ),
    'class_to_rotations_list': [
        {
            'E'   : ((( 1,  0,  0),
                      ( 0,  1,  0),
                      ( 0,  0,  1),),),
            'C3'  : ((( 0,  0,  1),
                      ( 1,  0,  0),
                      ( 0,  1,  0),),
                     (( 0,  1,  0),
                      ( 0,  0,  1),
                      ( 1,  0,  0),),
                     (( 0,  0, -1),
                      ( 1,  0,  0),
                      ( 0, -1,  0),),
                     (( 0, -1,  0),
                      ( 0,  0, -1),
                      ( 1,  0,  0),),
                     (( 0,  0, -1),
                      (-1,  0,  0),
                      ( 0,  1,  0),),
                     (( 0,  1,  0),
                      ( 0,  0, -1),
                      (-1,  0,  0),),
                     (( 0,  0,  1),
                      (-1,  0,  0),
                      ( 0, -1,  0),),
                     (( 0, -1,  0),
                      ( 0,  0,  1),
                      (-1,  0,  0),),),
            'C2'  : (((-1,  0,  0),
                      ( 0, -1,  0),
                      ( 0,  0,  1),),
                     (( 1,  0,  0),
                      ( 0, -1,  0),
                      ( 0,  0, -1),),
                     ((-1,  0,  0),
                      ( 0,  1,  0),
                      ( 0,  0, -1),),),
            'S4'  : ((( 0,  1,  0),
                      (-1,  0,  0),
                      ( 0,  0, -1),),
                     (( 0, -1,  0),
                      ( 1,  0,  0),
                      ( 0,  0, -1),),
                     ((-1,  0,  0),
                      ( 0,  0,  1),
                      ( 0, -1,  0),),
                     ((-1,  0,  0),
                      ( 0,  0, -1),
                      ( 0,  1,  0),),
                     (( 0,  0, -1),
                      ( 0, -1,  0),
                      ( 1,  0,  0),),
                     (( 0,  0,  1),
                      ( 0, -1,  0),
                      (-1,  0,  0),),),
            'sgd' : ((( 0, -1,  0),
                      (-1,  0,  0),
                      ( 0,  0,  1),),
                     (( 1,  0,  0),
                      ( 0,  0, -1),
                      ( 0, -1,  0),),
                     (( 0,  0, -1),
                      ( 0,  1,  0),
                      (-1,  0,  0),),
                     (( 0,  1,  0),
                      ( 1,  0,  0),
                      ( 0,  0,  1),),
                     (( 1,  0,  0),
                      ( 0,  0,  1),
                      ( 0,  1,  0),),
                     (( 0,  0,  1),
                      ( 0,  1,  0),
                      ( 1,  0,  0),),)
        }
    ]
}
# 32(O_h)
character_tables['m-3m'] = {
   'rotation_labels': ('E', 'C3', 'C2', 'C4', 'C4^2', 'i', 'S4', 'S6', 'sgh', 'sgd'),
   'class_order_list': (1, 8, 6, 6, 3, 1, 6, 8, 3, 6),
   'ir_labels': ('A1g', 'A2g', 'Eg', 'T1g', 'T2g', 'A1u', 'A2u', 'Eu', 'T1u', 'T2u'),
   'character_table': (
       (1,  1,  1,  1,  1,  1,  1,  1,  1,  1),
       (1,  1, -1, -1,  1,  1, -1,  1,  1, -1),
       (2, -1,  0,  0,  2,  2,  0, -1,  2,  0),
       (3,  0, -1,  1, -1,  3,  1,  0, -1, -1),
       (3,  0,  1, -1, -1,  3, -1,  0, -1,  1),
       (1,  1,  1,  1,  1, -1, -1, -1, -1, -1),
       (1,  1, -1, -1,  1, -1,  1, -1, -1,  1),
       (2, -1,  0,  0,  2, -2,  0,  1, -2,  0),
       (3,  0, -1,  1, -1, -3, -1,  0,  1,  1),
       (3,  0,  1, -1, -1, -3,  1,  0,  1, -1),
   ),
   'class_to_rotations_list': [
        {
            'E'   : ((( 1,  0,  0),
                      ( 0,  1,  0),
                      ( 0,  0,  1),),),
            'C3'  : ((( 0,  0,  1),
                      ( 1,  0,  0),
                      ( 0,  1,  0),),
                     (( 0,  1,  0),
                      ( 0,  0,  1),
                      ( 1,  0,  0),),
                     (( 0,  0, -1),
                      ( 1,  0,  0),
                      ( 0, -1,  0),),
                     (( 0, -1,  0),
                      ( 0,  0, -1),
                      ( 1,  0,  0),),
                     (( 0,  0, -1),
                      (-1,  0,  0),
                      ( 0,  1,  0),),
                     (( 0,  1,  0),
                      ( 0,  0, -1),
                      (-1,  0,  0),),
                     (( 0,  0,  1),
                      (-1,  0,  0),
                      ( 0, -1,  0),),
                     (( 0, -1,  0),
                      ( 0,  0,  1),
                      (-1,  0,  0),),),
            'C2'  : ((( 0,  1,  0),
                      ( 1,  0,  0),
                      ( 0,  0, -1),),
                     ((-1,  0,  0),
                      ( 0,  0,  1),
                      ( 0,  1,  0),),
                     (( 0,  0,  1),
                      ( 0, -1,  0),
                      ( 1,  0,  0),),
                     (( 0, -1,  0),
                      (-1,  0,  0),
                      ( 0,  0, -1),),
                     ((-1,  0,  0),
                      ( 0,  0, -1),
                      ( 0, -1,  0),),
                     (( 0,  0, -1),
                      ( 0, -1,  0),
                      (-1,  0,  0),),),
            'C4'  : ((( 0, -1,  0),
                      ( 1,  0,  0),
                      ( 0,  0,  1),),
                     (( 0,  1,  0),
                      (-1,  0,  0),
                      ( 0,  0,  1),),
                     (( 1,  0,  0),
                      ( 0,  0, -1),
                      ( 0,  1,  0),),
                     (( 1,  0,  0),
                      ( 0,  0,  1),
                      ( 0, -1,  0),),
                     (( 0,  0,  1),
                      ( 0,  1,  0),
                      (-1,  0,  0),),
                     (( 0,  0, -1),
                      ( 0,  1,  0),
                      ( 1,  0,  0),),),
            'C4^2': (((-1,  0,  0),
                      ( 0, -1,  0),
                      ( 0,  0,  1),),
                     (( 1,  0,  0),
                      ( 0, -1,  0),
                      ( 0,  0, -1),),
                     ((-1,  0,  0),
                      ( 0,  1,  0),
                      ( 0,  0, -1),),),
            'i'   : (((-1,  0,  0),
                      ( 0, -1,  0),
                      ( 0,  0, -1),),),
            'S4'  : ((( 0,  1,  0),
                      (-1,  0,  0),
                      ( 0,  0, -1),),
                     (( 0, -1,  0),
                      ( 1,  0,  0),
                      ( 0,  0, -1),),
                     ((-1,  0,  0),
                      ( 0,  0,  1),
                      ( 0, -1,  0),),
                     ((-1,  0,  0),
                      ( 0,  0, -1),
                      ( 0,  1,  0),),
                     (( 0,  0, -1),
                      ( 0, -1,  0),
                      ( 1,  0,  0),),
                     (( 0,  0,  1),
                      ( 0, -1,  0),
                      (-1,  0,  0),),),
            'S6'  : ((( 0,  0, -1),
                      (-1,  0,  0),
                      ( 0, -1,  0),),
                     (( 0, -1,  0),
                      ( 0,  0, -1),
                      (-1,  0,  0),),
                     (( 0,  0,  1),
                      (-1,  0,  0),
                      ( 0,  1,  0),),
                     (( 0,  1,  0),
                      ( 0,  0,  1),
                      (-1,  0,  0),),
                     (( 0,  0,  1),
                      ( 1,  0,  0),
                      ( 0, -1,  0),),
                     (( 0, -1,  0),
                      ( 0,  0,  1),
                      ( 1,  0,  0),),
                     (( 0,  0, -1),
                      ( 1,  0,  0),
                      ( 0,  1,  0),),
                     (( 0,  1,  0),
                      ( 0,  0, -1),
                      ( 1,  0,  0),),),
            'sgh' : ((( 1,  0,  0),
                      ( 0,  1,  0),
                      ( 0,  0, -1),),
                     ((-1,  0,  0),
                      ( 0,  1,  0),
                      ( 0,  0,  1),),
                     (( 1,  0,  0),
                      ( 0, -1,  0),
                      ( 0,  0,  1),),),
            'sgd' : ((( 0, -1,  0),
                      (-1,  0,  0),
                      ( 0,  0,  1),),
                     (( 1,  0,  0),
                      ( 0,  0, -1),
                      ( 0, -1,  0),),
                     (( 0,  0, -1),
                      ( 0,  1,  0),
                      (-1,  0,  0),),
                     (( 0,  1,  0),
                      ( 1,  0,  0),
                      ( 0,  0,  1),),
                     (( 1,  0,  0),
                      ( 0,  0,  1),
                      ( 0,  1,  0),),
                     (( 0,  0,  1),
                      ( 0,  1,  0),
                      ( 1,  0,  0),),)
        },
    ]
}
