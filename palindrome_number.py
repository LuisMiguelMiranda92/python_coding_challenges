"""
Given an integer x, return true if x is a palindrome, and false otherwise.
"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        string_x = str(x)
        if string_x == string_x[::-1]:
            return True
        else:
            return False