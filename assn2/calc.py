#!/usr/bin/env python
import sys

#converts the infix to a postfix
def infix2postfix( expression ):
    output = ""
    stack = []
    elements = expression.split()

    for value in elements:
        if is_number(value):
            output += value + " "
        elif value == ")":
            a = stack.pop()
            while a != "(":
                output += a + " "
                a = stack.pop()
        elif value == "(":
            stack.append(value)
        else:
            if len(stack) > 0:
                last_stack_item = stack[-1]
                if last_stack_item in "*/+-%" and is_more_pemdas(last_stack_item, value):
                    a = stack.pop()
                    output += a + " "
            stack.append(value)

    for operand in reversed(stack):
        output += operand + " "
        stack.remove(operand)

    return output;

#takes in a postfix and evaluates its numeric value
def evalPostfix( expression):
    postfix = expression.split()
    stack = []

    for value in postfix:
        if is_number(value):
            stack.append(int(value))
        else:
            op2 = stack.pop()
            op1 = stack.pop()
            answer = operation(value, op1, op2)
            stack.append(answer)

    return stack.pop() #last number remaining in the stack is the answer

#performs an operation
def operation( op, v1, v2 ):
    if op == "+":
        return v1 + v2
    elif op == "*":
        return v1 * v2
    elif op == "-":
        return v1 - v2
    elif op == "/":
        return v1 / v2
    elif op == "%":
        return v1 % v2

#returns whether the string is a number or not
def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

#determines the priority of operations
def is_more_pemdas(op1, op2):
    if op1 == "+" or op1 == "-" or op1 == "%":
        op1 = 1
    if op1 == "*" or op1 == "/":
        op1 = 2
    if op2 == "+" or op2 == "-" or op2 == "%":
        op2 = 1
    if op2 == "*" or op2 == "/":
        op1 = 2

    return op1 >= op2

def main( args ):
    args_length = len(sys.argv)
    if args_length > 2:
        print("Too many arguments were passed. Please only supply 1 target file.")
        return 1
    elif args_length == 2: #read in a file
        f = open(sys.argv[1], "r")
        for line in f:
            infix = line.strip('\n')
            postfix = infix2postfix(infix)
            answer = str(evalPostfix(postfix))
            print(postfix + "= " + answer)
        return 0
    elif args_length == 1: #read in from stdin
        for line in sys.stdin:
            postfix = infix2postfix(line)
            answer = str(evalPostfix(postfix))
            print(postfix + "= " + answer)
        return 0

if __name__ == '__main__' :
        sys.exit( main( sys.argv ))
