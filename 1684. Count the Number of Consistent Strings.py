class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        # Tip : you can use .issubset() code for this
        allowed_chars = set(allowed)
        count = 0
        for word in words:
            word_chars = set(word)
            if word_chars.issubset(allowed_chars):
                count += 1
        return count

'''
https://leetcode.com/problems/count-the-number-of-consistent-strings/description/?envType=problem-list-v2&envId=2lykzrqv&
'''
