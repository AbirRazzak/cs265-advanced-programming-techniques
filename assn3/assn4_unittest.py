#!/usr/bin/env python3
# test.script - unit tests for assn4
#
# Abir Razzak
# 6/4/2018
#

import unittest
import sys
import json


from assn4 import Register

class RegisterTests(unittest.TestCase) :
    '''Tests for Register class'''

    def setUp(self):
        self.x = Register(200, 20, 4, 6, 5)

    def test_init_norm(self) :
        '''Test a normal case of initializing'''
        '''Test a normal case of initializing with only 1's'''
        test = Register(5, 5)
        self.assertEqual(test.total, 5)

        '''Test a normal case of initializing with 1's & 5's'''
        test = Register(10, 5, 1)
        self.assertEqual(test.total, 10)

        '''Test a normal case of initializing with 1's, 5's, & 10's'''
        test = Register(52, 2, 0, 5)
        self.assertEqual(test.total, 52)

        '''Test a normal case of initializing with 1's, 5's, 10's & 20's'''
        test = Register(42, 2, 2, 1, 1)
        self.assertEqual(test.total, 42)

        '''Test if file was written correctly'''
        self.setUp()
        with open('register.json') as file :
            data = json.load(file)
            self.assertEqual(data['sales'], 0)
            self.assertEqual(data['total'], 200)
            self.assertEqual(data['ones'], 20)
            self.assertEqual(data['fives'], 4)
            self.assertEqual(data['tens'], 6)
            self.assertEqual(data['twenties'], 5)


    def test_init_badargs(self):
        '''Test bad arguements for init - negative numbers & non-ints'''
        '''Test bad arguements - negative numbers'''
        with self.assertRaises(SystemExit) as cm :
            Register(5, -5)
        self.assertEqual(cm.exception.code, 1)

        with self.assertRaises(SystemExit) as cm :
            Register(10, 5, -5)
        self.assertEqual(cm.exception.code, 1)

        with self.assertRaises(SystemExit) as cm :
            Register(52, 2, 0, -5)
        self.assertEqual(cm.exception.code, 1)

        with self.assertRaises(SystemExit) as cm :
            Register(42, 2, 2, 1, -1)
        self.assertEqual(cm.exception.code, 1)

        '''Test bad arguments - non-numbers'''
        with self.assertRaises(SystemExit) as cm :
            Register(5, "a")
        self.assertEqual(cm.exception.code, 1)

    def test_init_logic(self):
        '''Test if change and total amount are not equal for init'''
        with self.assertRaises(SystemExit) as cm :
            Register(52, 2, 0, 1)
        self.assertEqual(cm.exception.code, 2)

    def test_purchase_read(self):
        '''Test if purchase() handles not finding data file'''
        with self.assertRaises(SystemExit) as cm :
            self.x.FILE_NAME = "gibberish"
            self.x.purchase(1, 1)
        self.assertEqual(cm.exception.code, 4)

    def test_purchase_badargs(self) :
        '''Test bad arguments for purchase()'''
        '''Test for negative ints'''
        with self.assertRaises(SystemExit) as cm :
            self.x.purchase(-100, 10, 2, 2, 3)
        self.assertEqual(cm.exception.code, 1)

        with self.assertRaises(SystemExit) as cm :
            self.x.purchase(100, -10, 2, 2, 3)
        self.assertEqual(cm.exception.code, 1)

        with self.assertRaises(SystemExit) as cm :
            self.x.purchase(100, 10, -2, 2, 3)
        self.assertEqual(cm.exception.code, 1)

        with self.assertRaises(SystemExit) as cm :
            self.x.purchase(100, 10, 2, -2, 3)
        self.assertEqual(cm.exception.code, 1)

        with self.assertRaises(SystemExit) as cm :
            self.x.purchase(100, 10, 2, 2, -3)
        self.assertEqual(cm.exception.code, 1)

        '''Test for non-ints'''
        with self.assertRaises(SystemExit) as cm :
            self.x.purchase(100, "hi", 2, 2, 3)
        self.assertEqual(cm.exception.code, 1)

    def test_purchase_jibe(self) :
        '''Test to see if args don't jibe with amount for purchase()'''
        with self.assertRaises(SystemExit) as cm :
            self.x.purchase(100, 100, 2, 2, 3)
        self.assertEqual(cm.exception.code, 2)
    
    def test_purchase_notEnoughChange(self) :
        '''Test to check if program catches when there is not enough change in the drawer to refund in the puchase function'''
        with self.assertRaises(SystemExit) as cm :
            self.x.purchase(450, 100, 2, 2, 3)
        self.assertEqual(cm.exception.code, 3)

    def test_purchase(self) :
        '''Test if purchase is properly running'''
        pass

if __name__ == '__main__' :
   sys.argv.append( '-v' )
   unittest.main()