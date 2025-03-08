class Solution(object):
    def distinctAverages(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        average_list = []
        while len(nums) != 0:
            minimum = nums[0]
            maximum = nums[-1]
            average = (minimum + maximum)/2.0
            nums.pop(0)
            nums.pop(-1)
            if average not in average_list:
                average_list.append(average)
        return len(average_list)

'''
https://leetcode.com/problems/number-of-distinct-averages/description/
'''
