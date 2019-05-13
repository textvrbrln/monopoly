#!/usr/bin/env python3.3
# -*- coding: utf-8 -*-
"""This module throws dice."""

import random

onfield = [0]
double = [0]
move_fwd = 0
dice_result = [0]

def throw_dice():
    '''Throw two dice, add result and return'''
    dice1 = random.randrange(1, 7)
    dice2 = random.randrange(1, 7)
    result_of_dices = ((dice1 + dice2))
    # check for double
    
    if dice1 == dice2:
        double[0] = 1
    else:
        double[0] = 0
    return result_of_dices

def move_forward():
    dice_result[0] = throw_dice()
    move_fwd = ((onfield[0] + dice_result[0]))
    if move_fwd > 12:
        move_fwd = ((onfield[0] + dice_result[0] - 12))
        onfield[0] = move_fwd
        return move_fwd
    else:
        onfield[0] = move_fwd
        return move_fwd

def get_field_type(from_dice_number):
    fieldtypes = 'street', 'community', 'street', 'taxes', 'station', 'street', 'event', 'street', 'street', 'visiting', 'street', 'plant', 'station'
    return fieldtypes[from_dice_number]