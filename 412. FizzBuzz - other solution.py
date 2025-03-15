class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        answer = []
        for i in range(1, n + 1):
            answer.append(
                "FizzBuzz" if i % 15 == 0 else
                "Buzz" if i % 5 == 0 else
                "Fizz" if i % 3 == 0 else
                str(i)
            )
        return answer
''' Solution using terminary operator '''

''' https://leetcode.com/problems/fizz-buzz/description/ '''
