class Solution(object):
    def numberOfChild(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        children = [i for i in range(n)]
        left_end_right_end = (k // (n-1)) % 2
        order = k % (n-1)
        if left_end_right_end == 0:
            child_with_ball = children[order]
        else:
            child_with_ball = children[-order-1]
        return child_with_ball
    
    '''
    class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        cycle_length = 2 * (n - 1)  # Length of one cycle
        remainder = k % cycle_length  # Remainder after k seconds
    
        if remainder < n:  # Ball is within the range [0, n-1]
            return remainder
        else:  # Ball is within the range [n, 2 * (n - 1)]
            return cycle_length - remainder
    '''

'''
https://leetcode.com/problems/find-the-child-who-has-the-ball-after-k-seconds/description/
'''
