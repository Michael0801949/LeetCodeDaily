# Q1 House Robbing: https://leetcode.com/problems/house-robber/
class Solution:
    def rob(self, nums: List[int]) -> int:
        # If there is only one house, return its value as the max amount we can rob
        if len(nums) < 2:
            return nums[0]
        
        # Initialize a dp array where dp[i] represents the maximum amount we can rob up to house i
        dp = [0] * len(nums)
        dp[0] = nums[0]  # Base case: robbing the first house
        dp[1] = max(nums[0], nums[1])  # Base case: robbing either the first or second house, whichever is larger

        # Fill the dp array using the recurrence relation
        for i in range(2, len(nums)):
            # dp[i] is the maximum of either:
            # - Not robbing the current house (dp[i - 1])
            # - Robbing the current house (dp[i - 2] + nums[i])
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        # The last element in dp represents the maximum amount we can rob from all houses
        return dp[len(nums) - 1]

# Q2 213. House Robber II: https://leetcode.com/problems/house-robber-ii/description/
class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        
        # If there's only one house, return its value
        if length < 2:
            return nums[0]
        
        # Divide the problem into two cases:
        # Case 1: Rob from the first house to the second-to-last house (exclude the last)
        nums1 = nums[:length - 1]
        
        # Case 2: Rob from the second house to the last house (exclude the first)
        nums2 = nums[1:]
        
        # Debug prints to see the two subproblems
        # print(nums1)
        # print(nums2)
        
        # Return the maximum value from robbing in either case
        return max(self.robHouse(nums1, length - 1), self.robHouse(nums2, length - 1))
    
    def robHouse(self, nums: List[int], length: int) -> int:
        # If there's only one house in this subset, return its value
        if length < 2:
            return nums[0]
        
        # Initialize dp array where dp[i] represents the max amount that can be robbed up to house i
        dp = [0] * length
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        # Fill dp array using the same logic as in the linear House Robber problem
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
            # Debug print to observe dp array updates
            # print(dp)

        # The last element in dp represents the maximum amount that can be robbed in this subset
        return dp[length - 1]


# Q3 House Robbing 3: https://leetcode.com/problems/house-robber-iii/description/
# DP
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # Call helper function `recurssion` and return the maximum value between robbing or not robbing the root
        return max(self.recurssion(root))

    def recurssion(self, root: Optional[TreeNode]) -> [int, int]:
        # Base case: if the node is None, return [0, 0]
        # [0] -> max amount if we don't rob this node, [1] -> max amount if we rob this node
        if not root:
            return [0, 0]

        # Recursively calculate the maximum values for left and right subtrees
        left = self.recurssion(root.left)
        right = self.recurssion(root.right)
        
        # The meaning of DP array here is [val0, val1], val0: the max value not robing current node, val1: the max value robbing current node
        # Calculate the value if we rob this node (val1)
        # We can only add the values from not robbing the left and right children (left[0] and right[0])
        val1 = root.val + left[0] + right[0]

        # Calculate the value if we don't rob this node (val0)
        # We take the max of robbing or not robbing each child
        val0 = max(left[0], left[1]) + max(right[0], right[1])

        # Return both possibilities [not robbing this node, robbing this node]
        return [val0, val1]
