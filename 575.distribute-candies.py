class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        '''
        candy_type_count = []
        for candy in candyType:
            if candy not in candy_type_count:
                candy_type_count.append(candy)
        '''
        # we can use set to count the number of unique candies
        unique_candies = set(candyType)
        
        return min(len(unique_candies),len(candyType)/2)

'''
https://leetcode.com/problems/distribute-candies/description/
'''
