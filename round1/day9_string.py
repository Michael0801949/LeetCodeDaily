# Q1 Reverse Words in a String https://leetcode.com/problems/reverse-words-in-a-string/description/
'''
Python string.split() is powerful, it remove all the space and slice string according to space
There is no extra space O(1) solution for Python
'''

# 2 pointers
class Solution:
    def reverseWords(self, s: str) -> str:
        slist = s.split()

        left = 0
        right = len(slist) - 1
        while left < right:
            slist[left], slist[right] = slist[right], slist[left]
            left += 1
            right -= 1
        return ' '.join(slist)

# list comprehension
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s[::-1]
        s = ' '.join(word[::-1] for word in s.split())
        return s
