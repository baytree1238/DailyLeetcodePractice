class Solution(object):
    def smallestRangeI(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        maximum, minimum = max(nums), min(nums)
        difference_max_min = max(nums) - min(nums)
        if difference_max_min <= 2 * k:
            return 0
        else:
            return difference_max_min - 2 * k
        # max(nums) - k 
        # min(nums) + k
'''
https://leetcode.com/problems/smallest-range-i/description/
'''
