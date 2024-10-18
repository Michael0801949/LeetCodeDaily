# Q1 93. Restore IP Addresses: https://leetcode.com/problems/restore-ip-addresses/description/
class Solution:
    def backTracking(self, path: str, result: list, s: str, sIndex: int, segment: int):
        # Base case: If we have 4 segments and have processed all characters
        if segment == 4 and sIndex == len(s):
            result.append(path[:-1])  # Remove trailing dot before adding
            return
        
        # If we've formed 4 segments but there are still characters left, stop
        if segment == 4 or sIndex == len(s):
            return
        
        # Try forming segments of length 1, 2, or 3 digits
        for i in range(1, 4):  # Segment lengths must be between 1 and 3
            if sIndex + i <= len(s):  # Make sure we don't go beyond the string length
                segment_part = s[sIndex: sIndex + i]  # Get the next segment
                
                # Check if the segment is within the valid IP range (0-255) and has no leading zeros
                if int(segment_part) <= 255 and (segment_part == "0" or segment_part[0] != '0'):
                    # Recursively backtrack, passing a new path string
                    self.backTracking(path + segment_part + '.', result, s, sIndex + i, segment + 1)

    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        self.backTracking('', result, s, 0, 0)  # Start with an empty path and 0 segments
        return result


# Q2 78. Subsets: https://leetcode.com/problems/subsets/description/
class Solution:
    def generateSubsets(self, nums: List[int], result: List[List[int]], startIndex: int, path: List[int]) -> None:
        result.append(path[:])  # Add a copy of the current path, add on the top or the path in current instancewill not be append
        # if startIndex >= len(nums):  # no need for a end condition becasue for loop will stop
        #     return
        for i in range(startIndex, len(nums)):
            path.append(nums[i])  # Include the current element
            self.generateSubsets(nums, result, i + 1, path)  # Recur for the next element
            path.pop()  # Backtrack by removing the current element
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.generateSubsets(nums, result, 0, [])
        return result


# Q3 90. Subsets II: https://leetcode.com/problems/subsets-ii/description/
'''
refer to Combination Sum II: https://leetcode.com/problems/combination-sum-ii/description/?source=submission-ac
it need tree-level deduplication
'''
class Solution:
    # Main function to return all subsets, including handling duplicates
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []  # This will store all the subsets
        nums.sort()  # Sort the list to easily handle duplicates
        self.generateSubsets(nums, result, 0, [])  # Call the recursive function to generate subsets
        return result  # Return the final result of subsets
    
    # Recursive function to generate subsets
    def generateSubsets(self, nums: List[int], result: List[List[int]], startIndex: int, path: List[int]) -> None:
        result.append(path[:])  # Add the current subset (copy of path) to result
        
        # Loop through the numbers starting from startIndex to generate further subsets
        for i in range(startIndex, len(nums)):
            # If current element is the same as the previous one (and not the first in the loop), skip it to avoid duplicates
            if i > startIndex and nums[i] == nums[i - 1]:
                continue
            
            path.append(nums[i])  # Include the current element in the subset
            
            # Recurse with the next index and the updated path (subset)
            self.generateSubsets(nums, result, i + 1, path)
            
            # Backtrack by removing the last element added to explore other subsets
            path.pop()
        
        return
