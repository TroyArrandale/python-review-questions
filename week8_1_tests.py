
# 4 Levels of testing


# System
# Acceptance
# Unit
# Integration



# Sort the levels of testing by order in which they would be performed in a typical SDLC




#Types of test cases



#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#the solution returns the sum of all the multiples of 3 or 5 below the number passed in.

import unittest

def solution(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)
 

class TestForBasicMath(unittest.TestCase):

  def test_sum(self):
      self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")
    
  #TODO:Add a test Valid Positive Cases 

  #TODO:Add a test Invalid (negative) 

  #TODO:Add a Boundary Test

if __name__ == '__main__':
  unittest.main()



