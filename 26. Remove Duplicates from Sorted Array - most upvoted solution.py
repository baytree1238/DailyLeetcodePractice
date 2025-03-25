Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution(object):
...     def removeDuplicates(self, nums):
...         """
...         :type nums: List[int]
...         :rtype: int
...         """
...         nums[:] = sorted(set(nums))
...         return len(nums)
...         '''
...         Note that without [:], we're creating a new list object.
...         '''
... '''
... https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
