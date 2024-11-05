# Q1 1049. Last Stone Weight II: https://leetcode.com/problems/last-stone-weight-ii/description/
'''
seperate the stone into 2 subset, make the diff of 2 subset difference is minimum
'''
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # Calculate half of the total sum of stones as the target subset sum
        target = sum(stones) // 2

        # Initialize dp array where dp[j] represents the maximum subset sum we can achieve that is <= j
        dp = [0] * (target + 1)

        # Iterate over each stone's weight
        for stone in stones:
            # Update the dp array from the end to avoid using the same stone more than once
            for j in range(target, stone - 1, -1):
                # Maximize dp[j] by either excluding or including the current stone
                dp[j] = max(dp[j], dp[j - stone] + stone)

        # Return the minimum possible difference between the two subsets
        return sum(stones) - 2 * dp[target]

# Q2 494. Target Sum: https://leetcode.com/problems/target-sum/
'''
The hard part of this problem is converting this problem to a 0/1 knapsack problem:
there are negative (-) and positive (+) numbers in the result, it is equivalent to seperating the nums into 2 sets left (with positive nums) and right (with negative nums)

left + right = sum(nums)
-> 1: left = sum(nums) - right

left - right = target
-> 2: left = target + right

1 + 2
-> left = (sum(nums) + target) / 2

The problem become how many ways can we use to fill a backpack which has volume (sum(nums) + target) / 2
'''
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # If (target + sum(nums)) is odd, we cannot split nums to achieve target
        if (target + sum(nums)) % 2 != 0:
            return 0

        # If the absolute value of target is greater than sum(nums), achieving target is impossible
        if abs(target) > sum(nums):
            return 0

        # Calculate the "positive subset sum" required to achieve the target
        l_target = (target + sum(nums)) // 2

        # Initialize dp array where dp[j] represents the number of ways to reach sum j
        dp = [0] * (l_target + 1)
        dp[0] = 1  # Base case: there's one way to reach a sum of 0 (by choosing no elements)

        # Iterate through each number in nums
        for i in range(len(nums)):
            # Update dp array from right to left to avoid overwriting values needed in the same iteration
            for j in range(l_target, nums[i] - 1, -1):
                # Add the number of ways to reach (j - nums[i]) to the ways to reach j
                dp[j] += dp[j - nums[i]]

        # The answer is the number of ways to reach l_target
        return dp[l_target]

# Q3 474. Ones and Zeroes: https://leetcode.com/problems/ones-and-zeroes/description/
'''
This backpack has 2 dimensions m and n need to be both satisfied
The 2 dimension ned to be simulated with 2D array, but this 2 D array is being reuse like the 1D array in clasic 0/1 knapsack problem
'''
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # Initialize a 2D dp array where dp[y][x] represents the maximum number of strings
        # that can be formed with exactly y zeros and x ones
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Iterate over each string in strs
        for i in range(len(strs)):
            # Count the number of '0's and '1's in the current string
            curr_0 = strs[i].count('0')
            curr_1 = strs[i].count('1')

            # Update the dp array backwards to avoid using the same string multiple times
            for y in range(m, curr_0 - 1, -1):  # Iterate over zero capacity from m down to curr_0
                for x in range(n, curr_1 - 1, -1):  # Iterate over one capacity from n down to curr_1
                    # Update dp[y][x] to the maximum of not taking or taking the current string, using dp[y][x] as a part of max to refer to the dp[y][x] for i - 1
                    dp[y][x] = max(dp[y][x], dp[y - curr_0][x - curr_1] + 1)

        # The maximum number of strings we can form with exactly m zeros and n ones
        return dp[m][n]
