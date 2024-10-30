# Q1  0/1 knapsack https://kamacoder.com/problempage.php?pid=1046

# 2D array method
# Read two integers, m and n, from input
m, n = map(int, input().split(" "))

# Read the weights and values arrays from input
weight = list(map(int, input().split(" ")))
value = list(map(int, input().split(" ")))

# 1. meaning of the dp array: when bag carry capacity is j, select any thing from item 0 to item i, the max value is dp[j][i]
# 3. Initialize DP array: Initialize a 2D dp array with (n+1) rows and m columns, all elements set to 0
dp = [[0] * m for _ in range(n + 1)]
# 3. Initialize DP array: Initialize the first column of the dp array, setting the values for the first item
# If the capacity 'j' is greater than or equal to the weight of the first item, set dp[j][0] to its value
for j in range(weight[0], n + 1):
    dp[j][0] = value[0]
print(dp)  # Debug print to observe the dp array after initialization

# 4. iteration order: from top left to lower right: fill in the dp array starting from the second item
for j in range(1, n + 1):  # Loop over capacities from 1 to n (becasue capability is not an array, no need to -1)
    for i in range(1, m):  # Loop over items from 1 to m-1 (becasue m is the length of array ned to -1 for indexing)
        # 2. recurrence function: whether add the item i or not
        if j < weight[i]:  # If the current capacity is less than the weight of the item
            dp[j][i] = dp[j][i - 1]  # Cannot include the item, so use the previous value
            print(dp)  # Debug print to observe dp array after each update
        else:
            # Include the item: max of (value including the item, excluding the item, or previous dp value)
            dp[j][i] = max(dp[j - weight[i]][i - 1] + value[i], dp[j][i - 1], dp[j][i])
            print(dp)  # Debug print to observe dp array after each update

# Print the maximum value that can be achieved with capacity 'n' and all items
print(dp[n][m - 1])

# 1D array
'''
1. must iterate item first then iterate capacity (2-D is interchangable): the recurrence function is getting the current dp[i] from dp[j - weight[i]]
by deciding to add the item[i] or not, need to refer to item[i-1] to make decision. The meaning of recurrence function changed, items are not isolated considered
2. iterate capacity need to be backward: with 1-D array, if iterating forward, our dp[j - weight[i]] value is already overwirte by the current capacity 
there is no [i - 1] dimension in dp[j - weight[i]][i - 1] to reference to without item[i], and it would not be overwriten if we iterate backward
'''
m, n = map(int, input().split(" "))  # m is the number of items, n is the max weight capacity
weight = list(map(int, input().split(" ")))  # list of item weights
value = list(map(int, input().split(" ")))  # list of item values

# Initialize a 1D DP array for storing maximum values for each weight capacity up to `n`
dp = [0] * (n + 1)

# Iterate over each item
for i in range(m):
    # Traverse the dp array backwards to ensure each item is only considered once per weight capacity
    for j in range(n, weight[i] - 1, -1):
        dp[j] = max(dp[j], dp[j - weight[i]] + value[i])

# The result is the maximum value we can achieve with full capacity `n`
print(dp[n])

# Q2 416. Partition Equal Subset Sum: https://leetcode.com/problems/partition-equal-subset-sum/
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Check if the total sum of the array is odd; if so, partitioning equally is impossible
        if sum(nums) % 2 != 0:
            return False
        
        # Calculate the target sum for each subset, which is half of the total sum
        target = sum(nums) // 2

        # Initialize a 1D dp array where dp[j] represents whether we can reach sum j
        dp = [0] * (target + 1)

        # Iterate over each number in nums
        for i in range(len(nums)):
            # Traverse the dp array backwards from target to nums[i]
            for j in range(target, nums[i] - 1, -1):
                # If the current sum j is less than nums[i], retain the previous value in dp[j]
                if j < nums[i]:
                    dp[j] = max(dp[j], dp[j + 1])
                else:
                    # Update dp[j] by including the current number if it results in a closer sum to target
                    dp[j] = max(dp[j], dp[j - nums[i]] + nums[i])
        
        # Check if we can reach exactly the target sum
        return dp[target] == target

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Calculate the total sum of the array elements
        total_sum = sum(nums)

        # If the total sum is odd, it's impossible to partition it into two equal subsets
        if total_sum % 2 != 0:
            return False

        # Define the target sum for each subset, which should be half of the total sum
        subset_sum = total_sum // 2

        # Initialize a dp array where dp[j] indicates whether a subset with sum j is possible
        dp = [False] * (subset_sum + 1)
        dp[0] = True  # A subset with sum 0 is always achievable (empty subset)

        # Process each number in the array to see whether possible to achieve, when j == curr it will return True or dp[j - curr] is True it will also return True
        for curr in nums:
            # Traverse the dp array backwards from subset_sum to curr
            for j in range(subset_sum, curr - 1, -1):
                # Update dp[j] to True if a subset with sum j is achievable by including curr
                dp[j] = dp[j] or dp[j - curr]

        # Return whether a subset with the target sum (subset_sum) is achievable
        return dp[subset_sum]

# 2D
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        # Calculate the total sum of the array
        total_sum = sum(nums)

        # If the total sum is odd, it's impossible to partition into two equal subsets
        if total_sum % 2 != 0:
            return False

        # Define the target sum for each subset, which should be half of the total sum
        target_sum = total_sum // 2

        # Initialize a 2D dp array where dp[i][j] indicates whether a subset with sum j can be achieved 
        # using the first i elements
        dp = [[False] * (target_sum + 1) for _ in range(len(nums) + 1)]

        # Initialize the first column (sum of 0) as True, since an empty subset can achieve a sum of 0
        for i in range(len(nums) + 1):
            dp[i][0] = True

        # Process each number in the list
        for i in range(1, len(nums) + 1):
            for j in range(1, target_sum + 1):
                if j < nums[i - 1]:
                    # If the current number is greater than the target sum, we cannot include it
                    dp[i][j] = dp[i - 1][j]
                else:
                    # If the current number is less than or equal to the target sum, we have the option
                    # to include it or exclude it
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]

        # Return whether it's possible to achieve a subset with the target sum using all elements
        return dp[len(nums)][target_sum]