#!/usr/bin/env python3
# assn4 - Assignment 3 for CS265 (yes you read that correctly). Simulates a cash register
#
# Abir Razzak
# 6/4/2018
#

import sys

class Register:
    '''Simulates a cash register'''
    #Global variables
    ONES_VALUE = 1
    FIVES_VALUE = 5
    TENS_VALUE = 10
    TWENTIES_VALUE = 20

    def __init__ (self, amt, ones, fives=0, tens=0, twenties=0) :
        '''Immediately exit with code 1 if any of the args are negative'''
        if(amt < 0 or ones < 0 or fives < 0 or tens < 0 or twenties < 0) :
            sys.exit(1)
        
        try:
            self.sales = 0
            self.total = int(amt)
            self.ones = int(ones)
            self.fives = int(fives)
            self.tens = int(tens)
            self.twenties = int(twenties)
        except ValueError:
            '''String that is passed in does not represent an integer'''
            sys.exit(1)
        
        '''Check that cash in register is equal to the total given'''
        checkTotal = (self.ones * Register.ONES_VALUE) + (self.fives * Register.FIVES_VALUE) + (self.tens * Register.TENS_VALUE) + (self.twenties * Register.TWENTIES_VALUE)
        if(checkTotal != self.total) :
            sys.exit(2)
