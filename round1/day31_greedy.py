# Q1: 455. Assign Cookies https://leetcode.com/problems/assign-cookies/description/

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # Sort both the greed factor list 'g' and the cookie size list 's'
        g.sort()  # g represents the greed factor of children
        s.sort()  # s represents the size of the cookies
        
        # Initialize result counter 'r' to track the number of content children
        # 'i' is used to track the index of the greed factor list 'g'
        r = 0
        i = 0
        
        # Iterate through each cookie size 'c' in the sorted list 's'
        for c in s:
            # If all children are satisfied, break the loop
            if i >= len(g):
                break
            
            # If the current cookie 'c' can satisfy the child with greed factor g[i]
            if c >= g[i]:
                r += 1  # Increment the count of satisfied children
                i += 1  # Move to the next child (increment 'i')
            
            # If the current cookie is smaller than the greed factor of the child,
            # continue to the next cookie without satisfying the child.
            # This is done implicitly since the next iteration will run if 'if' condition fails.
        
        # Return the number of satisfied children
        return r

# Q2 376. Wiggle Subsequence https://leetcode.com/problems/wiggle-subsequence/

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # If the list has fewer than 2 elements, return its length as the result
        if len(nums) < 2:
            return len(nums)
        
        # Calculate the initial difference between the first two numbers
        prev_diff = nums[1] - nums[0]
        
        # Initialize result: if the initial difference is non-zero, we have a wiggle, so start with 2.
        # Otherwise, if the first two numbers are the same, start with 1.
        result = 2 if prev_diff != 0 else 1

        # Iterate over the list starting from the third element (index 2)
        for i in range(2, len(nums)):
            # Calculate the current difference between consecutive elements
            curr_diff = nums[i] - nums[i-1]
            
            # If there is a change in the direction of the sequence (i.e., from increasing to decreasing
            # or from decreasing to increasing), increment the result (as it's a valid wiggle)
            if (prev_diff <= 0 and curr_diff > 0) or (prev_diff >= 0 and curr_diff < 0):
                result += 1
                # Update the previous difference to the current difference
                prev_diff = curr_diff

        # Return the total count of wiggles (result)
        return result
    
# Q3 53. Maximum Subarray https://leetcode.com/problems/maximum-subarray/description/
'''
The local optimum solution: a consecutive sum > 0, so it can contribute positive number to later 
sum. For example: [2, -1, 3, -7] 2 + -1 = 1 > 0 it will contribute +1 to the sequence sum.
'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        count = 0  # This variable stores the running sum of the current subarray
        result = float('-inf')  # Initialize the result with the smallest possible value to track the maximum sum
        
        # Loop through each element in the input array
        for i in nums:
            count += i  # Add the current element to the running sum (current subarray sum)
            
            # If the current subarray sum (count) is greater than the maximum result found so far, update the result
            if count > result:
                result = count
            
            # If the current subarray sum becomes negative, reset it to 0
            # (since starting a new subarray from the next element might result in a higher sum)
            if count < 0:
                count = 0
        
        # Return the maximum sum of a contiguous subarray found
        return result



