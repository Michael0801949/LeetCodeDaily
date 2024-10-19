# Q1 491. Non-decreasing Subsequences: https://leetcode.com/problems/non-decreasing-subsequences/description/

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result = []  # This will hold all valid subsequences
        self.backTracking(nums, [], result, 0)
        return result
    
    def backTracking(self, nums: List[int], path: List[int], result: List[List[int]], sIndex: int) -> None:
        # If the current path has more than 1 element, it is a valid subsequence
        if len(path) > 1:
            result.append(path[:])
        
        used = set()  # To track the elements used in the current recursion level
        
        for i in range(sIndex, len(nums)):
            # Skip if the current element has already been used in this recursive level, in the next recursion level used will be set to empty again
            if nums[i] in used:
                continue
            
            # Ensure non-decreasing order: add nums[i] only if it's >= last element in the path or path is empty
            if not path or nums[i] >= path[-1]:
                path.append(nums[i])  # Add current number to the path
                used.add(nums[i])  # Mark the current number as used at this recursion level
                
                # Recur to explore the next numbers starting from i + 1
                self.backTracking(nums, path, result, i + 1)
                
                # Backtrack by removing the last added number
                path.pop()
# Q2 46. Permutations: https://leetcode.com/problems/permutations/description/

# solution 1 skip if in path
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.backTracking(nums, [], result)
        return result

    def backTracking(self, nums, path, result):
        if len(path) == len(nums):
            result.append(path[:])  # Append a copy of the path
            return
        for i in range(len(nums)):
            if nums[i] in path:  # Skip if the element is already in the path
                continue
            path.append(nums[i])
            self.backTracking(nums, path, result)  # No need to slice nums
            path.pop()  # Backtrack

# solution 2 used list
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        used = [False] * len(nums)  # Keep track of which elements are used
        self.backtrack(nums, [], used, result)
        return result

    def backtrack(self, nums: List[int], path: List[int], used: List[bool], result: List[List[int]]):
        if len(path) == len(nums):
            result.append(path[:])  # Add a copy of the current path to the result
            return
        for i in range(len(nums)):
            if used[i]:  # Skip already used elements
                continue
            path.append(nums[i])  # Choose the number
            used[i] = True  # Mark the element as used
            self.backtrack(nums, path, used, result)  # Recurse with the chosen element
            path.pop()  # Backtrack by removing the last element
            used[i] = False  # Mark the element as unused to explore other possibilities

# Q3 47. Permutations II https://leetcode.com/problems/permutations-ii/description/

from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # Sort the input list to handle duplicates easily
        nums.sort()
        # Initialize a 'used' list to keep track of elements that are used in the current permutation
        used = len(nums) * [False]
        result = []  # To store the unique permutations
        # Start backtracking to generate all unique permutations
        self.backTracking(nums, [], result, used)
        return result
    
    def backTracking(self, nums, path, result, used):
        # Base case: if the current path has the same length as nums, we've formed a valid permutation
        if len(path) == len(nums):
            result.append(path[:])  # Append a copy of the current permutation (path) to result
            return
        
        # Iterate over the numbers in the list
        for i in range(0, len(nums)):
            # Skip duplicates: if the current number is the same as the previous one and the previous one wasn't used
            # (i > 0 ensures we're not checking the first element)
            if (i > 0 and nums[i] == nums[i - 1] and not used[i - 1]) or used[i]:
                continue  # Skip to the next iteration if the number is already used or is a duplicate
            
            # Include nums[i] in the current permutation (path)
            path.append(nums[i])
            used[i] = True  # Mark the element as used in the current path
            
            # Recurse to build the next level of the permutation
            self.backTracking(nums, path, result, used)
            
            # Backtrack: remove the last element from the current path to explore other possibilities
            path.pop()
            used[i] = False  # Mark the element as unused so it can be used in future permutations
            