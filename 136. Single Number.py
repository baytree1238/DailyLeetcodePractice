Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution(object):
...     def singleNumber(self, nums):
...         """
...         :type nums: List[int]
...         :rtype: int
...         """
...         numbers = list(set(nums))
...         for number in numbers:
...             count = nums.count(number)
...             if count == 1:
...                 result = number
...         return result
... 
...     
>>> '''
... https://leetcode.com/problems/single-number/
