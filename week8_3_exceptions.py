import unittest

#TODO: Broken function should raise an exception with a message 'This is broken'
def broken_function():
    pass

def add_function(first_arg, second_arg):
    result = first_arg + second_arg
    return result

class MyTestCase(unittest.TestCase):
    def test_broken_function(self):
        with self.assertRaises(Exception) as context:
            broken_function()

        self.assertTrue('This is broken' in context.exception)
    
    #TODO: Types of exceptions given test_function('2',1) what type of exception is expected to be thrown? Fix the test below to check for the specific type?
    def test_add_function(self):
        with self.assertRaises(Exception) as context:
            add_function('1',2)
    #TODO explain why Exception is assertRaises?

if __name__ == '__main__':
    unittest.main()


