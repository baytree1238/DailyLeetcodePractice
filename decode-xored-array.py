Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution(object):
...     def decode(self, encoded, first):
...         """
...         :type encoded: List[int]
...         :type first: int
...         :rtype: List[int]
...         """
...         arr = [first]
...         for i in range(1, len(encoded)+1):
...                 arr.append(arr[i-1] ^ encoded[i-1])
...         return arr
...         # arr -- 0, 1, .. , n
...         # encoded = 0,1,..,n-2  xor 1,2,..,n-1
...         # encoded[i] = arr[i] XOR arr[i+1]
...         # encoded[i] is either arr[i] or arr[i+1],but not both
...         # Tip from discussion - draw out the truth table and then treat the output as input
...         # and one of the inputs as output
...         # | arr[i] | arr[i+1] | encoded[i]
...         # | 1      | 0        | 1
...         # | 1      | 1        | 0
...         # | 0      | 0        | 0
...         # | 0      | 1        | 1 
...         # arr[i] = arr[i-1] ^ encoded[i-1]
...     '''
...     Python 3 (lambda)
...     def decode(self, A, first):
...         return list(accumulate([first] + A, lambda x, y: x ^ y))
...     '''
...     # https://leetcode.com/problems/decode-xored-array/description/
