#!/usr/bin/env python3
# test_gInt - Unit Test for gInt class
#
# Abir Razzak
# 6/03/2018
#

import sys
import unittest

from gInt import gInt

class gIntTests( unittest.TestCase ) :
    '''Tests for gInt class'''

    def setUp (self) :
        self.x = gInt(3, -2)
        self.y = gInt(2, 5)
        self.z = gInt(13, 0)

    def test_add( self ) :
        '''Return a new gInt, self + rsh'''
        '''Pre-condition: both number are gInts'''
        expected = gInt(5, 3)
        result =  self.x.__add__(self.y)
        self.assertEqual(expected, result)

        expected = gInt(16, -2)
        result =  self.x.__add__(self.z)
        self.assertEqual(expected, result)

        expected = gInt(15, 5)
        result =  self.y.__add__(self.z)
        self.assertEqual(expected, result)
        '''Post-condition: a gInt is returned as the sum of the two gInts'''

    def test_mul( self ) :
        '''Return a new gInt, self * rhs'''
        '''Pre-condition: both numbers are gInts'''
        expected = gInt(6, -10)
        result =  self.x.__mul__(self.y)
        self.assertEqual(expected, result)

        expected = gInt(39, 0)
        result =  self.x.__mul__(self.z)
        self.assertEqual(expected, result)

        expected = gInt(26, 0)
        result =  self.y.__mul__(self.z)
        self.assertEqual(expected, result)
        '''Post-condition: a gInt is returned as the product of the two gInts'''

    def test_norm( self ) :
        '''Return real^2 + imag^2 as an int'''
        '''Pre-condition: the number is a gInt'''
        self.assertEqual(13, self.x.norm())
        self.assertEqual(29, self.y.norm())
        self.assertEqual(169, self.z.norm())
        '''Post-condition: an Int is returned as the sum of the coefficents squared'''

if __name__ == '__main__' :
   sys.argv.append( '-v' )
   unittest.main()