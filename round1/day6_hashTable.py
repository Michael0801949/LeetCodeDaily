# Valid Anagram https://leetcode.com/problems/valid-anagram/description/

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

