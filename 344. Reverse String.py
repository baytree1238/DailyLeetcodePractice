class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        s.reverse()
        '''
        or we can use s[:] = s[::-1] method
        s = ... replaces the reference (a new box),
        s[:] = ... replaces the contents (same box, new stuff inside).
        '''
'''
https://leetcode.com/problems/reverse-string/description/
'''
