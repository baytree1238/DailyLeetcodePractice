class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        
        # Use the shortest string as the reference
        shortest = min(strs, key=len)
        
        for i, char in enumerate(shortest):
            for s in strs:
                if s[i] != char:
                    return shortest[:i]
        return shortest
'''
https://leetcode.com/problems/longest-common-prefix/
'''
