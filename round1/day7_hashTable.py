# Q1 4sum ii: https://leetcode.com/problems/4sum-ii/description/
'''
keys:
1. Iterate arrays 2 by 2 and store the sum result of first 2 arrays in hash table then find target-sum in the second 2 arrays. In this way time complexity = 2*n^2 == n^2
2. When find a match, result need += the value to the key not +=1. If there is a match, the number comnbination should be + the number of combination of in first 2 arrays not just + 1
'''
# Answer
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        dic = {}
        result = 0

        for n1 in nums1:
           for n2 in nums2:
            if n1+n2 not in dic:
                dic[n1+n2] = 1
            else:
                dic[n1+n2] += 1
        
        for n3 in nums3:
           for n4 in nums4:
            if 0-n3-n4 not in dic:
                continue
            else:
               result += dic[0-n3-n4]
        return result
      
# use dictionary.get(n1+n2, 0)
class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4)
        hashmap = dict()
        for n1 in nums1:
            for n2 in nums2:
                hashmap[n1+n2] = hashmap.get(n1+n2, 0) + 1
        
        count = 0
        for n3 in nums3:
            for n4 in nums4:
                key = - n3 - n4
                if key in hashmap:
                    count += hashmap[key]
        return count
      
# use defaul dictionary
from collections import defaultdict 
class Solution:
    def fourSumCount(self, nums1: list, nums2: list, nums3: list, nums4: list) -> int:
        rec, cnt = defaultdict(lambda : 0), 0
        for i in nums1:
            for j in nums2:
                rec[i+j] += 1
        for i in nums3:
            for j in nums4:
                cnt += rec.get(-(i+j), 0) 
        return cnt
# Q2 Ransom Note: https://leetcode.com/problems/ransom-note/description/
'''
very similar to valid-anagram
'''
# Answer
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic = {}
        for i in range(len(magazine)):
            dic[magazine[i]] = dic.get(magazine[i], 0) + 1
        for j in range(len(ransomNote)):
            if ransomNote[j] in dic:
                dic[ransomNote[j]] -= 1
                if dic[ransomNote[j]] == 0:
                    del dic[ransomNote[j]]
            else: return False
        return True
# Use count
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for char in ransomNote:
            if char in magazine and ransomNote.count(char) <= magazine.count(char): # string.count(char, startIndex, endIndex) return the number of a character in a string
                continue
            else:
                return False
        return True
# even shorter answer
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return all(ransomNote.count(c) <= magazine.count(c) for c in set(ransomNote)) # The all() function returns True if all items in an iterable are true, otherwise it returns False. If the iterable object is empty, the all() function also returns True.
