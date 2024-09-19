# Q1 Reverse String: https://leetcode.com/problems/reverse-string/description/

# Answer 2 pointers
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
# stack
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        stack = []
        for char in s:
            stack.append(char)
        for i in range(len(s)):
            s[i] = stack.pop()
# range
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        for i in range(n // 2):
            s[i], s[n - i - 1] = s[n - i - 1], s[i]
# reversed
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = reversed(s)

# slicing
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1]
      
# List comprehensions
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = [s[i] for i in range(len(s) - 1, -1, -1)]
      
# reverse method
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()
# Q2 Reverse Strin ii: https://leetcode.com/problems/reverse-string-ii/description/
'''
1. Only need to check every 2k and opreate on the first k element, so the pointer should be incremental by 2k
2. I was a bit hesitate and confused on the start point of left pointer and right pointer, it is actually pretty simple:
left is i right is i + k
'''
# Answer 2 pointer:
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        def reverseList(s: str):
            left, right = 0, len(s) - 1
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            return s
        res = list(s)
        for i in range(0,len(s), 2*k):
            res[i: i + k] = reverseList(res[i: i + k])
        return ''.join(res)

# Not using list
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        i = 0

        while i < len(s):
            j = i + k
            s = s[:i] + s[i:j][::-1] + s[j:]
            i += 2*k
        return s
# Q3 substitute number: https://kamacoder.com/problempage.php?pid=1064
'''
extra spce O(n)
'''
class Solution:
    def to_number(self, s: str):
        slist = list(s)
        for i in range(len(slist)):
            if slist[i].isdigit(): # isnumeric() also works here, key difference isdigit return False for fraction number like 1/2 isnumeric return True
                slist[i] = 'number'
        return ''.join(slist)
