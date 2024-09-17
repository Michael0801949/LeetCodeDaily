# Q1 Valid Anagram https://leetcode.com/problems/valid-anagram/description/

# Answer
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        i = 0
        j = 0
        if len(s) != len(t):
            return False
        while i < len(s):
            if s[i] in dic: # need to be more farmiliar with condiction whether a key is in a dic
                dic[s[i]] += 1
            else:
                dic[s[i]] = 1
            i += 1
        while j < len(t):
            if t[j] in dic:
                dic[t[j]] -= 1
                if t[j] in dic and dic[t[j]] == 0:
                    del dic[t[j]] # how to delete a key from a dic
            else:
                return False
            j += 1
        return dic == {}
# More simple answer
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import defaultdict
        
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)
        for x in s:
            s_dict[x] += 1
        
        for x in t:
            t_dict[x] += 1
        return s_dict == t_dict
      
# use array as hash table
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        record = [0] * 26
        for i in s:
            # record ASCII number relevant to "a"
            record[ord(i) - ord("a")] += 1
        for i in t:
            record[ord(i) - ord("a")] -= 1
        for i in range(26):
            if record[i] != 0:
                return False
        return True

# Q2 Intersection of Two Arrays https://leetcode.com/problems/intersection-of-two-arrays/description/

# Set Answer
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        inter = set1 & set2 # intersaction of 2 sets, Union (set1 | set2): Combines both sets. Left Join (set1 - set2): Elements in set1 but not in set2. Right Join (set2 - set1): Elements in set2 but not in set1. Outer Join (set1 ^ set2): Elements in either set, but not in both.
        return inter

# Even can be shorter
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))
        
# hash table
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    # store all element in one list into a hash table
        table = {}
        for num in nums1:
            table[num] = table.get(num, 0) + 1
        
        # use set to store result
        res = set()
        for num in nums2:
            if num in table:
                res.add(num)
                del table[num]
        
        return list(res)
