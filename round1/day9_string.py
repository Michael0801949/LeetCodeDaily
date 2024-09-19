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

#Q2 right rotate string: https://kamacoder.com/problempage.php?pid=1065

'''
for python this is a list problem, need extra space
'''
k = int(input())
s = input()

s = s[len(s)-k:] + s[:len(s)-k]
print(s)

#Q3 Find the Index of the First Occurrence in a String

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        hlen = len(haystack)
        nlen = len(needle)
        i = 0
        while i <= hlen - nlen: # blundary here need to be <=, need to continue even if rest h = n, extre case h == n == 'a'
            if haystack[i] == needle[0]:
                if haystack[i:i+nlen] == needle:
                    return i
            i += 1
        return -1
