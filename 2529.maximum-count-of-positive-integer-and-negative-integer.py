class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count_negative = 0
        count_positive = 0
        for number in nums:
            if number > 0:
                count_positive += 1
            if number < 0:
                count_negative += 1
        return max(count_positive, count_negative)



        
'''
https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/description/
'''
