class Solution(object):
    def prefixesDivBy5(self, nums):
        """
        :type nums: List[int]
        :rtype: List[bool]
        """
        bool_list = []
        binary_to_decimal = 0
        for i, num in enumerate(nums):
            binary_to_decimal = binary_to_decimal * 2 + num
            bool_list.append(binary_to_decimal % 5 == 0)
        return bool_list

'''
https://leetcode.com/problems/binary-prefix-divisible-by-5/
'''
