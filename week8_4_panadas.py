import pandas as pd
import unittest

nested_dict = {'white_wine': {1998:1, 1999:1, 2000:2},
'red_wine': {1998:3, 1999:2, 2000:0}}

df = pd.DataFrame(nested_dict)

class TestForBasicMath(unittest.TestCase):

    def test_df_white_wine_1998(self):
        pass
        #TODO: Test the value of white wine is expect in the dataframe of 1998 is 1
        #self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")
        #

if __name__ == '__main__':
    unittest.main()
