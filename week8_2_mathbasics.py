

#TODO: add library to get math values



import unittest

#TODO set my PI value using library
pi = 3.14

class TestForBasicMath(unittest.TestCase):

    def test_pi(self):
        self.assertGreater(pi , 3.14, "Should be bigger than 3.14")

if __name__ == '__main__':
  unittest.main()
