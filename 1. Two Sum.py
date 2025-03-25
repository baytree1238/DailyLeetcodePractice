class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index, value in enumerate(nums):
            if target - value in nums and index != nums.index(target - value):
                return index, nums.index(target - value)
'''
https://leetcode.com/problems/two-sum/
'''
