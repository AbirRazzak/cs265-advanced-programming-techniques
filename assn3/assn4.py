#!/usr/bin/env python3
# assn4 - Assignment 3 for CS265 (yes you read that correctly). Simulates a cash register
#
# Abir Razzak
# 6/4/2018
#

import sys
import json
import pdb

def init (amt, ones, fives=0, tens=0, twenties=0) :
    try:
        SALES = 0
        TOTAL = int(amt)
        ONES = int(ones)
        FIVES = int(fives)
        TENS = int(tens)
        TWENTIES = int(twenties)
        '''Exit with code 1 if any of the args are negative'''
        if(TOTAL < 0 or ONES < 0 or FIVES < 0 or TENS < 0 or TWENTIES < 0) :
            raise ValueError('Negative number was entered')
    except ValueError:
        '''String that is passed in does not represent an integer'''
        sys.exit(1)

    '''Check that cash in register is equal to the total given'''
    checkTotal = get_value(ONES, FIVES, TENS, TWENTIES)
    if(checkTotal != TOTAL) :
        sys.exit(2)

    '''Now make the file that holds the values'''
    update_file(SALES, TOTAL, ONES, FIVES, TENS, TWENTIES)

def purchase (amt, ones, fives=0, tens=0, twenties=0) :
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
        with open('register.json') as infile :
            data = json.load(infile)
            SALES = int(data['sales'])
            TOTAL = int(data['total'])
            ONES = int(data['ones'])
            FIVES = int(data['fives'])
            TENS = int(data['tens'])
            TWENTIES= int(data['twenties'])
    except:
        '''Cannot find file'''
        sys.exit(4)

    change = get_value(p_ones, p_fives, p_tens, p_twenties) - p_amt
    if (change < 0) :
        '''If change is negative, then cash doesn't add up to >= price'''
        sys.exit(2)
    
    if (change > TOTAL) :
        '''Register does not have enough cash to return change'''
        sys.exit(3)
    
    '''The cash in drawer cannot break into the change amount'''
    change_ones = 0
    change_fives = 0
    change_tens = 0
    change_twenties = 0
    change_total = 0

    if (change != 0) :
        for x in range(TWENTIES):
            if(change_total + 20 > change) :
                break
            else :
                change_twenties += 1
                change_total += 20
        
        for x in range(TENS):
            if(change_total + 10 > change) :
                break
            else :
                change_tens += 1
                change_total += 10

        for x in range(FIVES):
            if(change_total + 5 > change) :
                break
            else :
                change_fives += 1
                change_total += 5

        for x in range(ONES):
            if(change_total + 1 > change) :
                break
            else :
                change_ones += 1
                change_total += 1
    
    if(change_total == change) :
        '''Successful purchase has been made'''
        #Collect the cash
        ONES += p_ones
        FIVES += p_fives
        TENS += p_tens
        TWENTIES += p_twenties
        #Give change to customer
        ONES -= change_ones
        FIVES -= change_fives
        TENS -= change_tens
        TWENTIES -= change_twenties
        output = "{0} {1} {2} {3}".format(change_ones, change_fives, change_tens, change_twenties)
        print(output)
        SALES += p_amt
        TOTAL += p_amt
        update_file(SALES, TOTAL, ONES, FIVES, TENS, TWENTIES)
        return output
    else :
        '''Not enough bills to make enough money for change'''
        sys.exit(3)

def change (statement) :
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
        have_value = get_value(int(have[0]), int(have[1]), int(have[2]), int(have[3]))
        want_value = get_value(int(want[0]), int(want[1]), int(want[2]), int(want[3]))
        if(have_value != want_value) :
            '''Amount given and amount wanted do not match up'''
            sys.exit(2)
    except ValueError:
        '''Non-ints were entered'''
        sys.exit(1)
    
    try :
        with open('register.json') as infile :
            data = json.load(infile)
            SALES = int(data['sales'])
            TOTAL = int(data['total'])
            ONES = int(data['ones'])
            FIVES = int(data['fives'])
            TENS = int(data['tens'])
            TWENTIES= int(data['twenties'])
    except:
        '''Couldn't find or read file properly'''
        sys.exit(4)
    
    if(int(want[0]) > ONES or int(want[1]) > FIVES or int(want[2]) > TENS or int(want[3]) > TWENTIES) :
        '''Cannot make proper change'''
        sys.exit(3)
    else :
        '''Give requested change to customer'''
        ONES -= int(want[0])
        FIVES -= int(want[1])
        TENS -= int(want[2])
        TWENTIES -= int(want[3])
        output = "{0} {1} {2} {3}".format(want[0], want[1], want[2], want[3])
        print(output)
        '''Take customers change and put in register'''
        ONES += int(have[0])
        FIVES += int(have[1])
        TENS += int(have[2])
        TWENTIES += int(have[3])
        update_file(SALES, TOTAL, ONES, FIVES, TENS, TWENTIES)
        return output

def report() :
    try :
        with open('register.json') as infile :
            data = json.load(infile)
            SALES = int(data['sales'])
            TOTAL = int(data['total'])
            ONES = int(data['ones'])
            FIVES = int(data['fives'])
            TENS = int(data['tens'])
            TWENTIES= int(data['twenties'])
    except:
        '''Could not read or find file'''
        sys.exit(4)
    output = "{0} : {1} = {2} {3} {4} {5}".format(SALES, TOTAL, ONES, FIVES, TENS, TWENTIES)
    print(output)
    return output

def update_file(sales, total, ones, fives, tens, twenties) :
    with open('register.json', 'w') as outfile :
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

def get_value(ones, fives, tens, twenties):
    '''Returns the monetary value of the bills'''
    return (ones * 1) + (fives * 5) + (tens * 10) + (twenties * 20)

def main(args):
    #pdb.set_trace()
    args_length = len(sys.argv)
    if args_length < 2:
        print('Forgot your arguments?')
        sys.exit(1)
    
    a = list(sys.argv)
    a.pop(0) #pops off assn4
    cmd = a.pop(0) #pops off command being called

    if (cmd == 'report'):
        report()
        sys.exit(0)

    else :
        if (cmd == 'change') :
            expression = ""
            for i in range(len(a)) :
                expression += str.format('{0} ', a[i])

            change(expression)
            sys.exit(0)

        try:
            if '=' in a :
                a.remove('=') #Take out the equal
            else :
                '''No equal sign found'''
                sys.exit(1)
            while len(a) < 5 :
                a.append(0) #Add 0's if they are not included
        except :
            sys.exit(1)

        if (cmd == 'init') :
            init(a[0], a[1], a[2], a[3], a[4])
            sys.exit(0)

        if (cmd == 'purchase') :
            purchase(a[0], a[1], a[2], a[3], a[4])
            sys.exit(0)

if __name__ == '__main__' :
        sys.exit( main( sys.argv ))
