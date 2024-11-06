# Q1 complete knapsack: https://kamacoder.com/problempage.php?pid=1052
# item -> capacity
def test_CompletePack(weight, value, bagWeight):
    # Initialize a dp array where dp[j] represents the maximum value achievable with capacity j
    dp = [0] * (bagWeight + 1)

    # Iterate over each item
    for i in range(len(weight)):  # Traverse each item
        # Traverse the backpack capacities from weight[i] up to bagWeight
        # This allows us to consider including the item multiple times
        for j in range(weight[i], bagWeight + 1):
            # Update dp[j] to the maximum value by either excluding or including the current item
            dp[j] = max(dp[j], dp[j - weight[i]] + value[i])

    # The maximum value for the full backpack capacity is stored in dp[bagWeight]
    return dp[bagWeight]

if __name__ == "__main__":
    # Define the weights and values of items and the capacity of the backpack
    weight = [1, 3, 4]
    value = [15, 20, 30]
    bagWeight = 4

    # Calculate the maximum value achievable with the given items and backpack capacity
    result = test_CompletePack(weight, value, bagWeight)
    print(result)

# capacity -> item
def test_CompletePack(weight, value, bagWeight):
    # Initialize a dp array where dp[j] represents the maximum value achievable with capacity j
    dp = [0] * (bagWeight + 1)

    # Iterate over each capacity from 0 to bagWeight
    for j in range(bagWeight + 1):  # Traverse each capacity of the backpack
        # For each capacity, check each item to see if it can fit
        for i in range(len(weight)):  # Traverse each item
            # If the current item can fit in the backpack at this capacity
            if j - weight[i] >= 0:
                # Update dp[j] to the maximum value by either excluding or including the current item
                dp[j] = max(dp[j], dp[j - weight[i]] + value[i])

    # The maximum value for the full backpack capacity is stored in dp[bagWeight]
    return dp[bagWeight]

if __name__ == "__main__":
    # Define the weights and values of items and the capacity of the backpack
    weight = [1, 3, 4]
    value = [15, 20, 30]
    bagWeight = 4

    # Calculate the maximum value achievable with the given items and backpack capacity
    result = test_CompletePack(weight, value, bagWeight)
    print(result)

# Q2 518. Coin Change II https://leetcode.com/problems/coin-change-ii/description/
'''
recurrence function: dp[j] += dp[j - coin]

For this problem the for loop order matters because we are asked to find the # of combination not the max value:
if we have the capacity as outer loop and coin as inner loop the result is # of arrangement not # of combination
Using capacity as outer loop coin as inner loop result in same combination different arrangement get counted

eg:
amount =
5
coins =
[1,2,5]

print(j)
print(coin)
print(dpprint(dp):
1
1
[1, 1, 0, 0, 0, 0] only coin 1 fit 1 comb
1
2
[1, 1, 0, 0, 0, 0] only coin 1 fit 1 comb
1
5
[1, 1, 0, 0, 0, 0] only coin 1 fit 1 comb
2
1
[1, 1, 1, 0, 0, 0] comb [1, 1] fit
2
2
[1, 1, 2, 0, 0, 0] comb [1, 1] and [2] fit
2
5
[1, 1, 2, 0, 0, 0] comb [1, 1] and [2,0] fit 5 does not fit
3
1
[1, 1, 2, 2, 0, 0] comb [1, 1, 1] and [2, 1] fit
3
2
[1, 1, 2, 3, 0, 0] <- here there is a double counting: comb [1, 1, 1] and [2, 1] fit and it will also count [1, 2]
3
5
[1, 1, 2, 3, 0, 0] comb 
4
1
[1, 1, 2, 3, 3, 0] comb [1, 1, 1] and [2, 1] and [1, 2], 5 does not fit
4
2
[1, 1, 2, 3, 5, 0] it will snowball and increase the final answer: comb [1, 1, 1, 1] and [2, 1, 1] and [1, 2, 1] and [1, 1, 2] and [2, 2]
4
5
[1, 1, 2, 3, 5, 0] comb [1, 1, 1, 1] and [2, 1, 1] and [1, 2, 1] and [1, 1, 2] and [2, 2], 5 does not fit
5
1
[1, 1, 2, 3, 5, 5] comb [1, 1, 1, 1, 1] and [2, 1, 1, 1] and [1, 2, 1, 1] and [1, 1, 2, 1] and [2, 2, 1]
5
2
[1, 1, 2, 3, 5, 8] comb [1, 1, 1, 1, 1] and [2, 1, 1, 1] and [1, 2, 1, 1] and [1, 1, 2, 1] and [2, 2, 1] and [1, 1, 1, 2] and [2, 1, 2] fit and  [1, 2,]
5
5
[1, 1, 2, 3, 5, 9] comb [1, 1, 1, 1, 1] and [2, 1, 1, 1] and [1, 2, 1, 1] and [1, 1, 2, 1] and [2, 2, 1] and [1, 1, 1, 2] and [2, 1, 2] fit and  [1, 2,] and [5]

If we use coin as outer loop there is no such problem becasue it isolate consider each coin adding to the combination:

print(j)
print(coin)
print(dp):

1
1
[1, 1, 0, 0, 0, 0] comb [1]
2
1
[1, 1, 1, 0, 0, 0] comb [1, 1]
3
1
[1, 1, 1, 1, 0, 0] comb [1, 1, 1]
4
1
[1, 1, 1, 1, 1, 0] comb [1, 1, 1, 1]
5
1
[1, 1, 1, 1, 1, 1] comb [1, 1, 1, 1, 1]
2
2
[1, 1, 2, 1, 1, 1] comb [1, 1], [2]
3
2
[1, 1, 2, 2, 1, 1] comb [1, 1, 1], [1, 2]
4
2
[1, 1, 2, 2, 3, 1] comb [2, 2], [1, 1, 2], [1, 1, 1, 1]
5
2
[1, 1, 2, 2, 3, 3] comb [1, 1, 1, 2], [1, 2, 2], [1, 1, 1, 1, 1]
5
5
[1, 1, 2, 2, 3, 4] comb [1, 1, 1, 2], [1, 2, 2], [1, 1, 1, 1, 1], [5]

'''

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Initialize dp array where dp[j] represents the number of ways to make amount j
        dp = [0] * (amount + 1)
        dp[0] = 1  # Base case: there's one way to make amount 0, by choosing no coins.

        # Iterate over each coin in the coins list
        for coin in coins:
            # For each coin, update dp array from current coin value up to amount
            for j in range(coin, amount + 1):
                # Add the number of ways to make (j - coin) to dp[j]
                dp[j] += dp[j - coin]
                print(dp)
                
        # Return the number of ways to make the specified amount
        return dp[amount]

# Q3 377. Combination Sum IV https://leetcode.com/problems/combination-sum-iv/description/
'''
This problem ask for # of arrangement not # of combination, use capacity as outer loop
'''

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # Initialize a dp array where dp[j] represents the number of ways to reach sum j
        dp = [0] * (target + 1)
        dp[0] = 1  # Base case: there's one way to make target 0, by choosing no elements.

        # Iterate over each sub-target from 1 to target
        for j in range(1, target + 1):
            # For each number in nums, check if it can be used to reach the current sub-target j
            for num in nums:
                if j >= num:
                    # If num can be used, add ways to make up (j - num) to dp[j]
                    dp[j] += dp[j - num]
                    
        # Return the number of ways to reach the target
        return dp[target]

# Q4 https://kamacoder.com/problempage.php?pid=1067
'''
it is a twist of 377. Combination Sum IV 
'''
def climbing_stairs(n, m):
    # Initialize a dp array where dp[j] represents the number of ways to reach step j
    dp = [0] * (n + 1)
    dp[0] = 1  # Base case: there is one way to stay at the ground (step 0), which is by doing nothing.

    # Since this is a permutation problem, the outer loop should iterate over the "target" (total steps)
    for j in range(1, n + 1):  # Loop over each step up to n
        for i in range(1, m + 1):  # Loop over each possible step size from 1 up to m
            if j >= i:  # Only proceed if the current step j is greater than or equal to step size i
                dp[j] += dp[j - i]  # i represents the step size, not an index, so we add ways from dp[j - i]

    # Return the number of ways to reach the nth step
    return dp[n]

if __name__ == '__main__':
    # Read input values for n (total steps) and m (maximum step size)
    n, m = list(map(int, input().split(' ')))
    print(climbing_stairs(n, m))
