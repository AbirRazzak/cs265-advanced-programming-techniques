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
    FILE_NAME = "register.json"

    SALES = 0
    TOTAL = 0
    ONES = 0
    FIVES = 0
    TENS = 0
    TWENTIES = 0

    def __init__ (self, amt, ones, fives=0, tens=0, twenties=0) :
        try:
            self.SALES = 0
            self.TOTAL = int(amt)
            self.ONES = int(ones)
            self.FIVES = int(fives)
            self.TENS = int(tens)
            self.TWENTIES = int(twenties)
            '''Exit with code 1 if any of the args are negative'''
            if(amt < 0 or ones < 0 or fives < 0 or tens < 0 or twenties < 0) :
                raise ValueError('Negative number was entered')
        except ValueError:
            '''String that is passed in does not represent an integer'''
            sys.exit(1)
        
        '''Check that cash in register is equal to the total given'''
        checkTotal = self.get_value(self.ONES, self.FIVES, self.TENS, self.TWENTIES)
        if(checkTotal != self.TOTAL) :
            sys.exit(2)

        '''Now make the file that holds the values'''
        self.update_file(self.SALES, self.TOTAL, self.ONES, self.FIVES, self.TENS, self.TWENTIES)

    def purchase (self, amt, ones, fives=0, tens=0, twenties=0) :
        try:
            p_amt = int(amt)
            p_ones = int(ones)
            p_fives= int(fives)
            p_tens = int(tens)
            p_twenties = int(twenties)
            if(p_amt < 0 or p_ones < 0 or p_fives < 0 or p_tens < 0 or p_twenties < 0) :
                raise ValueError('Negative number was entered')
        except ValueError:
            '''String that is passed in does not represent an integer'''
            sys.exit(1)

        try:
            self.read_file()
        except:
            '''Cannot find file'''
            sys.exit(4)

        change = self.get_value(p_ones, p_fives, p_tens, p_twenties) - p_amt
        if (change < 0) :
            '''If change is negative, then cash doesn't add up to >= price'''
            sys.exit(2)
        
        if (change > self.TOTAL) :
            '''Register does not have enough cash to return change'''
            sys.exit(3)
        
        '''The cash in drawer cannot break into the change amount'''
        change_ones = 0
        change_fives = 0
        change_tens = 0
        change_twenties = 0
        change_total = 0

        if (change != 0) :
            for x in range(self.TWENTIES):
                if(change_total + self.TWENTIES_VALUE > change) :
                    break
                else :
                    change_twenties += 1
                    change_total += self.TWENTIES_VALUE
            
            for x in range(self.TENS):
                if(change_total + self.TENS_VALUE > change) :
                    break
                else :
                    change_tens += 1
                    change_total += self.TENS_VALUE

            for x in range(self.FIVES):
                if(change_total + self.FIVES_VALUE > change) :
                    break
                else :
                    change_fives += 1
                    change_total += self.FIVES_VALUE

            for x in range(self.ONES):
                if(change_total + self.ONES_VALUE > change) :
                    break
                else :
                    change_ones += 1
                    change_total += self.ONES_VALUE
        
        if(change_total == change) :
            '''Successful purchase has been made'''
            #Collect the cash
            self.ONES += p_ones
            self.FIVES += p_fives
            self.TENS += p_tens
            self.TWENTIES += p_twenties
            #Give change to customer
            self.ONES -= change_ones
            self.FIVES -= change_fives
            self.TENS -= change_tens
            self.TWENTIES -= change_twenties
            output = "{0} {1} {2} {3}".format(change_ones, change_fives, change_tens, change_twenties)
            print(output)
            self.SALES += p_amt
            self.TOTAL += p_amt
            self.update_file(self.SALES, self.TOTAL, self.ONES, self.FIVES, self.TENS, self.TWENTIES)
            return output
        else :
            '''Not enough bills to make enough money for change'''
            sys.exit(3)

    def change (self, statement) :
        partition = statement.partition(' = ')
        if(not partition[1]) :
            '''The arguments were bad, could not find a ='''
            sys.exit(1)
        have = partition[0].split()
        want = partition[2].split()
        if(len(have) > 4 or len(want) > 4) :
            '''More than 4 numbers were given on a side'''
            sys.exit(1)
        
        '''Fill in 0's if less than 4 numbers were given'''
        have = list(have)
        want = list(want)
        while len(have) < 4 :
            have.append(0)
        while len(want) < 4 :
            want.append(0)
        
        try:
            have_value = self.get_value(int(have[0]), int(have[1]), int(have[2]), int(have[3]))
            want_value = self.get_value(int(want[0]), int(want[1]), int(want[2]), int(want[3]))
            if(have_value != want_value) :
                '''Amount given and amount wanted do not match up'''
                sys.exit(2)
        except ValueError:
            '''Non-ints were entered'''
            sys.exit(1)
        
        try :
            self.read_file()
        except:
            '''Couldn't find or read file properly'''
            sys.exit(4)
        
        if(int(want[0]) > self.ONES or int(want[1]) > self.FIVES or int(want[2]) > self.TENS or int(want[3]) > self.TWENTIES) :
            '''Cannot make proper change'''
            sys.exit(3)
        else :
            '''Give requested change to customer'''
            self.ONES -= int(want[0])
            self.FIVES -= int(want[1])
            self.TENS -= int(want[2])
            self.TWENTIES -= int(want[3])
            output = "{0} {1} {2} {3}".format(want[0], want[1], want[2], want[3])
            print(output)
            '''Take customers change and put in register'''
            self.ONES += int(have[0])
            self.FIVES += int(have[1])
            self.TENS += int(have[2])
            self.TWENTIES += int(have[3])
            self.update_file(self.SALES, self.TOTAL, self.ONES, self.FIVES, self.TENS, self.TWENTIES)
            return output

    def report(self) :
        try :
            self.read_file()
        except:
            '''Could not read or find file'''
            sys.exit(4)
        output = "{0} : {1} = {2} {3} {4} {5}".format(self.SALES, self.TOTAL, self.ONES, self.FIVES, self.TENS, self.TWENTIES)
        print(output)
        return output

    def read_file(self) :
        with open(str(self.FILE_NAME)) as infile :
            data = json.load(infile)
            self.SALES = data['sales']
            self.TOTAL = data['total']
            self.ONES = data['ones']
            self.FIVES = data['fives']
            self.TENS = data['tens']
            self.TWENTIES = data['twenties']

    def update_file(self, sales, total, ones, fives, tens, twenties) :
        with open(self.FILE_NAME, 'w') as outfile :
            data = {}
            data['sales'] = sales
            data['total'] = total
            data['ones'] = ones
            data['fives'] = fives
            data['tens'] = tens
            data['twenties'] = twenties

            outfile.seek(0)
            json.dump(data, outfile)
            outfile.truncate()

    def get_value(self, ones, fives, tens, twenties):
        '''Returns the monetary value of the bills'''
        return (ones * self.ONES_VALUE) + (fives * self.FIVES_VALUE) + (tens * self.TENS_VALUE) + (twenties * self.TWENTIES_VALUE)

def main(args):
    args_length = len(sys.argv)
    if args_length < 2:
        print('Forgot your arguments?')
    
    a = list(sys.argv)
    a.pop(0) #pops off assn4
    cmd = a.pop(0) #pops off command being called

    if (cmd == 'report'):
            Register.report()
    else :
        if (cmd == 'change') :
            expression = ""
            for i in range(len(a)) :
                expression += str.format('{0} ', a[i])

            return Register.change(expression)

        try:
            a.pop('=') #Take out the equal
            while len(a) < 5 :
                a.append(0) #Add 0's if they are not included
            except :
                sys.exit(1)

        if (cmd == 'init') :
            return Register(a[0], a[1], a[2], a[3], a[4])

        if (cmd == 'purchase') :
            return Register.purchase(a[0], a[1], a[2], a[3], a[4])

if __name__ == '__main__' :
        sys.exit( main( sys.argv ))