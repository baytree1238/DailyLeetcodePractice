class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # ideas by "Lokesh Senthilkumar" from Leetcode
        '''
        Explanation:
        set the prefix as the first string of the list
        if any of the strings does not have the prefix, remove the last character and
        repeat step2 and step3

        Key : removal of the last letter after each letter
        '''
        prefix = strs[0]
        for string in strs:
            while not string.startswith(prefix):
                prefix = prefix[:-1]
        return prefix
'''
https://leetcode.com/problems/longest-common-prefix/description/
'''
