class Solution(object):
    def smallestRangeI(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        minimum = min(nums)
        maximum = max(nums)
        return max(0, max(nums) - min(nums) - 2 * k)'''
https://leetcode.com/problems/smallest-range-i/description/
'''
