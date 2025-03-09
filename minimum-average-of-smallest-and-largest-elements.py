class Solution(object):
    def minimumAverage(self, nums):
        """
        :type nums: List[int]
        :rtype: float
        """
        nums.sort()  
        minimum_average = (nums[-1]+nums[0])/ 2.0
        for i in range(len(nums)//2):
            new_average = (nums[i]+nums[len(nums)-i-1])/2.0
            if new_average < minimum_average:
                minimum_average = new_average
            # When I try to remove if statement and use min(minimum_average, new_average), 
            #   for some reason I got an error. 
        return minimum_average
    # Python uses Banker's rounding. It might be better to use 2.0

'''
https://leetcode.com/problems/minimum-average-of-smallest-and-largest-elements/
'''
