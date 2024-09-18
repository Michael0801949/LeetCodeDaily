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


# Q3 3 Sums: https://leetcode.com/problems/3sum/description/
'''
Thought Process:
    1. Sort list
    2. Set var1 at i
    3. j and k as 2 pointers iterate from left to right, right to left
Details:
    Remove Duplication:
        1. Remove duplication for i when nums[i] == nums[i - 1], it is i - 1 not i + 1 becasue the same element can duplicate in a result but not duplicate in 2 or more result
        2. Remove j and k duplications when find a match: not using -1 here becasue all duplications need to be remove which is not the same situation as i
    Boundary:
        when remove duplication with i-1, k+1 ,j+1, do not forget the boundary of them
    Optimization:
        1. check whether len(array) < 3
        2. if nums[i] > 0 and nums[i] is the smallest number, there sum is not possible = 0
'''
# 2 pointers Answer1
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        i = 0
        if len(nums) < 3:
            return result
        

        while i < len(nums) - 2:
            if nums[i] > 0:
                break

            while i >= 1 and nums[i] == nums[i - 1] and i < len(nums) - 2 : # boundary i
                i += 1

            j = i + 1
            k = len(nums) - 1

            while j < k:
                sums3 = nums[i] +  nums[j] + nums[k]

                if sums3 > 0:
                    k -= 1
                elif sums3 < 0:
                    j += 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    while nums[j] == nums[j+1] and j + 1 < k: # boundary j + 1
                        j += 1
                    while nums[k] == nums[k-1] and j < k - 1: # boundary k - 1
                        k -= 1
                    j += 1 # do not forget to move pointers aftermatch
                    k -= 1
            i += 1
        return result
# 2 pointers answer 2 use range
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        
        for i in range(len(nums)):
            # if first element > 0 no need to check
            if nums[i] > 0:
                return result
            
            # skip same i, prevent dup
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            left = i + 1
            right = len(nums) - 1
            
            while right > left:
                sum_ = nums[i] + nums[left] + nums[right]
                
                if sum_ < 0:
                    left += 1
                elif sum_ > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # skip same element, prevent dup
                    while right > left and nums[right] == nums[right - 1]:
                        right -= 1
                    while right > left and nums[left] == nums[left + 1]:
                        left += 1
                        
                    right -= 1
                    left += 1
                    
        return result
        
# use dictionary
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        # find a + b + c = 0
        # a = nums[i], b = nums[j], c = -(a + b)
        for i in range(len(nums)):
            # if first element > 0 no need to check
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]: # dedup element a 
                continue
            d = {}
            for j in range(i + 1, len(nums)):
                if j > i + 2 and nums[j] == nums[j-1] == nums[j-2]: # dedup element b
                    continue
                c = 0 - (nums[i] + nums[j])
                if c in d:
                    result.append([nums[i], nums[j], c])
                    d.pop(c) # dedup element c
                else:
                    d[nums[j]] = j
        return result
#Q4 4sum: https://leetcode.com/problems/4sum/description/
'''
1. compared with 3 sum the oprimization is different: nums[i] > target is not enough because negative number can less the result, target > 0 and nums[i] > 0 and nums[i] > target then we can break
2. boundary: see detail inline comment
3. In the whole, it is the same thought process as 3 sum, jsut need to fix 2 number first, add one more loop out side
'''

# answer 1
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        i = 0
        if len(nums) < 4:
            return result
        while i < len(nums) - 3:
            if nums[i] > target and target > 0 and nums[i] > 0:
                break
            while nums[i] == nums[i-1] and i < len(nums) - 3 and i > 0:
                i += 1
            j = i + 1
            while j < len(nums) - 2:
                while nums[j] == nums[j-1] and j < len(nums) - 2 and j >  i + 1: # boundary of j > i + 1
                    j += 1
                left = j + 1
                right = len(nums) - 1
                while left < right:
                    sum4 = nums[i] + nums[j] + nums[left] + nums[right]
                    if sum4 < target:
                        left += 1
                    elif sum4 > target:
                        right -= 1
                    else:
                        result.append([ nums[i], nums[j], nums[left], nums[right]])
                        while nums[left] == nums[left + 1] and left + 1 < right: # boundary of left + 1
                            left += 1
                        while nums[right] == nums[right - 1] and left < right - 1: # boundary of right -1
                            right -= 1
                        left += 1
                        right -= 1
                j += 1
            i += 1
        return result
        
# answer2 use range
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []
        for i in range(n):
            if nums[i] > target and nums[i] > 0 and target > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, n):
                if nums[i] + nums[j] > target and target > 0:
                    break
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                left, right = j+1, n-1
                while left < right:
                    s = nums[i] + nums[j] + nums[left] + nums[right]
                    if s == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        while left < right and nums[right] == nums[right-1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif s < target:
                        left += 1
                    else:
                        right -= 1
        return result
# answer 3 use dictionary
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # create a dic to store the frequency of each number
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        # create a set to store final answer
        ans = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    val = target - (nums[i] + nums[j] + nums[k])
                    if val in freq:
                        # make sure no repeat
                        count = (nums[i] == val) + (nums[j] == val) + (nums[k] == val)
                        if freq[val] > count:
                            ans.add(tuple(sorted([nums[i], nums[j], nums[k], val])))
        
        return [list(x) for x in ans]
