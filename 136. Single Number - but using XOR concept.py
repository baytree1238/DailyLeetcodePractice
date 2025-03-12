class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Solution by Pratik 
        # concept using XOR
        unique_number = 0
        for number in nums:
            unique_number ^= number
        return unique_number

'''
https://leetcode.com/problems/single-number/description/
'''
