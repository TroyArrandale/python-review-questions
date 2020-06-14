
# Your job is to finish the the calculator which evaluates expressions in Reverse Polish notation.

# For example expression 5 1 2 + 4 * + 3 - (which is equivalent to 5 + ((1 + 2) * 4) - 3 in normal notation) should evaluate to 14.
# or a simpler example 2 2 + = 4
# see the tests at the bottom

# For your convenience, the input is formatted such that a space is provided between every token.

# Valid operations are +, -, *, /.

# You may assume that there won't be exceptional situations (like stack underflow or division by zero).

import operator
import unittest
from stack import *


#TODO: Replace ? with correct method or variable name

def calcRPN(expr):

    #TODO: Don't allow empty strings to be entered

    #What type of collection is this? 
    OPERATORS = {'+': operator.add, '*': operator.mul, '/': operator.truediv}
    
    #I need an abstract datatype to hold values with a good name?
    ? = ?
    

    for token in expr.split(" "):

        if token not in OPERATORS: #if its an operand
            stack.?(float(token))
        else: #its an operator
            operand2 = stack.?()
            operand1 = stack.?()

            # Below code will execute OPERATOR on operand2 and operand1
            stack.?(OPERATORS[token](operand1,operand2))


    
    # Return the last item left in my collection
    return stack.?()



Test = unittest.TestCase()


Test.assertEqual(calcRPN("1 3 +"), 4, "Should support addition")
Test.assertEqual(calcRPN("1 3 *"), 3, "Should support multiplication")
Test.assertEqual(calcRPN("1 3 -"), -2, "Should support subtraction")
Test.assertEqual(calcRPN("4 2 /"), 2, "Should support division")
Test.assertEqual(calcRPN("4 2 / 5 +"), 7, "Should support division")
Test.assertEqual(calcRPN("3"), 3, "Should parse numbers")
Test.assertEqual(calcRPN("3.5"), 3.5, "Should parse float numbers")