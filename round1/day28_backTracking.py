# 39. Combination Sum: https://leetcode.com/problems/combination-sum/description/

class Solution:
    def __init__(self):
        self.result = []
        self.path = []

    def backtracking(self, candidates: List[int], target: int, current_sum: int, start_index: int):
        if current_sum > target:
            return  # Terminate early if the current sum exceeds the target

        if current_sum == target:
            self.result.append(self.path[:])  # Add a copy of the current path to the result
            return

        for i in range(start_index, len(candidates)):
            self.path.append(candidates[i])
            # Recur with updated current sum and starting index to allow reuse of the same element
            self.backtracking(candidates, target, current_sum + candidates[i], i)
            self.path.pop()  # Backtrack and remove the last element

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.backtracking(candidates, target, 0, 0)  # Initialize with sum = 0 and starting index = 0
        return self.result
    
# 40. Combination Sum II: https://leetcode.com/problems/combination-sum-ii/description/?source=submission-ac

class Solution:
    def __init__(self):
        self.path = []
        self.result = []
    def traversal(self, candidates: List[int], index: int, path_sum: int, target: int,):
        # stop condition
        if path_sum > target:
            return

        if path_sum == target:
            self.result.append(self.path[:])
            return
        # current level logic 
        for i in range(index, len(candidates)):
            # skip dup
            if i > index and candidates[i] == candidates[i - 1]:
                continue
            # skip number if > target
            if candidates[i] > target:
                break 
            self.path.append(candidates[i])
            path_sum += candidates[i]
            # recursion
            self.traversal(candidates, i + 1, path_sum, target)
            # backtrack
            path_sum -= candidates[i]
            self.path.pop()

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # sort to help dedup
        candidates.sort()
        self.traversal(candidates, 0, 0, target)
        return self.result
    
#Q3 131. Palindrome Partitioning: https://leetcode.com/problems/palindrome-partitioning/

class Solution:
    def backTracking(self, index: int, s: str, path: List[str], result: List[List[str]]):
        # when index ( start point of the divider ) is more than len(s) - 1 append to result
        # do not use len(path) because there are elements with length > 1, so the path length can be < len(s)
        if index == len(s):
            result.append(path[:])
            return
        
        # index is the star point of each division 
        for i in range(index, len(s)):
            # filter out non palindrome, use i + 1 not i becasue sub string is left close right open
            if s[index: i + 1] == s[index: i + 1][::-1]:
                path.append(s[index: i + 1])
                # new start index is i + 1, division string only on the right side after s[i]
                self.backTracking(i + 1, s, path, result)
                path.pop()

    def partition(self, s: str) -> List[List[str]]:
        result = []
        self.backTracking(0, s, [], result)
        return result
