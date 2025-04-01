class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romans = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        total, prev = 0, 0
        for char in s[::-1]: # !!! 
            if romans[char] >= prev:
                total += romans[char]
            else:
                total -= romans[char]
            prev = romans[char]
        return total
        '''
        https://leetcode.com/problems/roman-to-integer/
        '''
