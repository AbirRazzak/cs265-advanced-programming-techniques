#!/usr/bin/env python3
# assn4 - Assignment 3 for CS265 (yes you read that correctly). Simulates a cash register
#
# Abir Razzak
# 6/4/2018
#

import sys
import json

class Register:
    '''Simulates a cash register'''
    #Class variables
    ONES_VALUE = 1
    FIVES_VALUE = 5
    TENS_VALUE = 10
    TWENTIES_VALUE = 20
    FILE_NAME = "Register.tmp"

    def __init__ (self, amt, ones, fives=0, tens=0, twenties=0) :
        try:
            self.sales = 0
            self.total = int(amt)
            self.ones = int(ones)
            self.fives = int(fives)
            self.tens = int(tens)
            self.twenties = int(twenties)
            '''Exit with code 1 if any of the args are negative'''
            if(amt < 0 or ones < 0 or fives < 0 or tens < 0 or twenties < 0) :
                raise ValueError('Negative number was entered')
        except ValueError:
            '''String that is passed in does not represent an integer'''
            sys.exit(1)
        
        '''Check that cash in register is equal to the total given'''
        checkTotal = (self.ones * Register.ONES_VALUE) + (self.fives * Register.FIVES_VALUE) + (self.tens * Register.TENS_VALUE) + (self.twenties * Register.TWENTIES_VALUE)
        if(checkTotal != self.total) :
            sys.exit(2)

        '''Now make the file that holds the values'''
        data = {}
        data['sales'] = self.sales
        data['total'] = self.total
        data['ones'] = self.ones
        data['fives'] = self.fives
        data['tens'] = self.tens
        data['twenties'] = self.twenties

        with open('register.json', 'w') as outfile :
            json.dump(data, outfile)

    def purchase (amt, ones, fives=0, tens=0, twenties=0) :
        try:
            a = int(amt)
            o = int(ones)
            f= int(fives)
            t = int(tens)
            tw = int(twenties)
            if(a < 0 or o < 0 or f < 0 or t < 0 or tw < 0) :
                raise ValueError('Negative number was entered')
        except ValueError:
            '''String that is passed in does not represent an integer'''
            sys.exit(1)
