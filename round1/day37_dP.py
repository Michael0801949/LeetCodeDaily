# Q1 509. Fibonacci Number https://leetcode.com/problems/fibonacci-number/description/
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 2 or n == 1:
            return 1
        # 1. meaning of dp[i] is the i + 1th fibonacci number
        i = 2
        # 3. initialize dp array
        result = [1, 1]

        while i + 1 <= n:
            # 2. recurrence function
            result.append(result[i - 1]+result[i - 2])
            # 4. iteration direction
            i += 1
        return result[i - 1]       
    
class Solution:
    def fib(self, n: int) -> int:
       
       # 1. According to prompt dp[i] is the ith fibonacci number
        # Handle the corner case where n is 0
        if n == 0:
            return 0
        
        # 3. Create a dp table (array) to store Fibonacci values up to n
        dp = [0] * (n + 1)

        # Initialize the base cases for the Fibonacci sequence
        dp[0] = 0
        dp[1] = 1

        # 4. Fill in the dp array from the bottom up, as each state depends on previous states
        for i in range(2, n + 1):
            # 2. Use the recurrence relation for Fibonacci: F(n) = F(n-1) + F(n-2)
            dp[i] = dp[i - 1] + dp[i - 2]
        
        # Return the nth Fibonacci number
        return dp[n]
# shorter
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        
        dp = [0, 1]
        
        for i in range(2, n + 1):
            total = dp[0] + dp[1]
            dp[0] = dp[1]
            dp[1] = total
        
        return dp[1]
# recurssion
class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        return self.fib(n - 1) + self.fib(n - 2)

# Q2 70. Climbing Stairs https://leetcode.com/problems/climbing-stairs/description/
'''
it is essentailly the same problem as 509. Fibonacci Number, the only difference initialization array is [1, 2]
Also the prompt did not tell you the recurrence function, it is actually the same as 509. Fibonacci Number
'''
# space complexity O[n]
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        # 1. meaning of dp[i] is the i + 1th fibonacci number
        i = 2
        # 3. initialize dp array
        result = [1, 2]

        while i + 1 <= n:
            # 2. recurrence function
            result.append(result[i - 1]+result[i - 2])
            # 4. iteration direction
            i += 1
        return result[i - 1] 

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return n
        
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]

# space complexity O[3]
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return n
        
        dp = [0] * 3
        dp[1] = 1
        dp[2] = 2
        
        for i in range(3, n + 1):
            total = dp[1] + dp[2]
            dp[1] = dp[2]
            dp[2] = total
        
        return dp[2]

# Q3 746. Min Cost Climbing Stairs https://leetcode.com/problems/min-cost-climbing-stairs/description/
# Recurrence
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # 1. Initialize dp array with two elements to represent the minimum cost of the previous two step
        # 3. initialize a array [0, 0] as dp array
        dp = [0, 0]

        # 4. Iterate from step 2 to the end of the cost array plus one (the top of the stairs)
        for i in range(2, len(cost) + 1):

            # 2. Recurrence Formula: calculate the minimum cost to reach the current step, either from the previous step or from the step before that
            dp[0] = min(cost[i - 1] + dp[1], cost[i - 2] + dp[0])
            # Update dp array to shift dp[1] to dp[0] for the next iteration
            dp[0], dp[1] = dp[1], dp[0]
        # Return the minimum cost to reach the top of the stairs
        return dp[1]

# Recursive (time out on leetcode)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Determine the length of the cost array (number of steps)
        i = len(cost)
        
        # Initialize the dp array with zeros to store minimum costs for each step
        dp = [0] * (len(cost) + 1)
        
        # Start recursive traversal from the top of the stairs
        return self.traversal(cost, i, dp)

    def traversal(self, cost, i, dp):
        # Base case: if at the ground or the first step, no cost to start climbing
        if i == 0 or i == 1:
            return 0

        # Recursively calculate the minimum cost for each step
        # Single layer logic: by considering the previous one or two steps and adding their costs
        dp[i] = min(self.traversal(cost, i - 1, dp) + cost[i - 1], 
                    self.traversal(cost, i - 2, dp) + cost[i - 2])

        # Return result to current level: Return the computed minimum cost to reach the current step i
        return dp[i]

# Recursive with Memorization (pass on leectcode)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        i = len(cost)
        dp = [-1] * (i + 1)  # Initialize dp array with -1 for memoization
        return self.traversal(cost, i, dp)

    def traversal(self, cost, i, dp):
        if i == 0 or i == 1:
            return 0

        # Check if dp[i] has already been computed
        if dp[i] != -1:
            return dp[i]

        # Recursive computation with memoization
        dp[i] = min(self.traversal(cost, i - 1, dp) + cost[i - 1], 
                    self.traversal(cost, i - 2, dp) + cost[i - 2])

        return dp[i]

