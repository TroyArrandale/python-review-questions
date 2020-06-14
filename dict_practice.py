

# Your job is to finish the method which returns a dictionary with each unique word and count of unique words passed in.
# You can expect words to only be seperated by spaces and all on one line, you should be case insensitive and return all lower case



import unittest


def countWords(expr):

    result = {}
    

    # Return the dictionary
    return result


# 3 Marks, one for case, one for correct count of words, one for correct amount of unique words returned.

# Revises collections, and string manupilation

Test = unittest.TestCase()

Test.assertEqual(countWords("fuck fuck fuck"), {"fuck":3 } , "Should be a a count of 3")
Test.assertEqual(countWords("HOLY FUCK").__len__(), 2 , "Should have 2 unique words ")
Test.assertEqual(countWords("HOLY FUCK"), {holy:1, fuck:1} , "Should have 2 unique words ")
Test.assertEqual(countWords("HOLY holy").__len__(), 1 , "Should have 1 unique words as its case insesitive")

