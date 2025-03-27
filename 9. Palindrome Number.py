class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x)[::-1] == str(x)
    '''
    slower solution
    '''
    '''
    https://leetcode.com/problems/palindrome-number/
    '''
