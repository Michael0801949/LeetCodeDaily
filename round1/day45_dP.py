# Q1 121. Best Time to Buy and Sell Stock: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
# Greedy
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize `low` as infinity to track the minimum price encountered so far
        low = float('inf')
        
        # Initialize `r` to store the maximum profit
        r = 0

        # Iterate over each price in the prices list
        for i in range(0, len(prices)):
            # Update `low` to be the minimum price seen up to day i
            low = min(prices[i], low)
            
            # Calculate the profit if selling on day i and update `r` to the max profit so far
            r = max(r, prices[i] - low)
        
        # Return the maximum profit achievable
        return r
    
# 2-D DP
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize dp array with two states for each day:
        # dp[i][0]: Maximum profit on day i if holding a stock
        # dp[i][1]: Maximum profit on day i if not holding a stock
        dp = [[0, 0] for i in range(len(prices))]
        
        # Base case: If we buy on the first day, profit is -prices[0] for holding the stock
        dp[0][0] = -prices[0]

        # Iterate over each day starting from day 1
        for i in range(1, len(prices)):
            # Update dp[i][1] for the maximum profit if not holding a stock on day i
            # It could be either the profit of selling on day i (dp[i - 1][0] + prices[i])
            # or the profit of not holding from the previous day (dp[i - 1][1])
            dp[i][1] = max(dp[i - 1][0] + prices[i], dp[i - 1][1])
            
            # Update dp[i][0] for the maximum profit if holding a stock on day i
            # It could be either the profit from holding the stock from the previous day (dp[i - 1][0])
            # or buying a stock on day i (-prices[i])
            dp[i][0] = max(dp[i - 1][0], -prices[i])

            # Uncomment the next line to observe dp array updates for each day
            # print(dp)
        
        # Return the maximum profit achievable if not holding any stock on the last day
        return dp[len(prices) - 1][1]

# 1-D DP
'''
updating dp[1] does not affect dp[0]
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize dp array with two states:
        # dp[0] represents the max profit on day i if holding a stock
        # dp[1] represents the max profit on day i if not holding a stock
        dp = [0, 0]
        dp[0] = -prices[0]  # Buying on the first day, so profit is -prices[0]

        # Iterate over each price in the list
        for i in range(0, len(prices)):
            # Update dp[1] to the maximum profit if not holding stock on day i
            # This could be either the previous dp[1] or selling the stock on day i (dp[0] + prices[i])
            dp[1] = max(dp[0] + prices[i], dp[1])
            
            # Update dp[0] to the maximum profit if holding stock on day i
            # This could be either the previous dp[0] or buying stock on day i (-prices[i])
            dp[0] = max(dp[0], -prices[i])
        
        # Return the max profit achievable if not holding stock by the end of the last day
        return dp[1]

# Q2 122. Best Time to Buy and Sell Stock II: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
# DP
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize dp array with two states for each day:
        # dp[i][0]: Maximum profit on day i if holding a stock
        # dp[i][1]: Maximum profit on day i if not holding a stock
        dp = [[0, 0] for i in range(len(prices))]
        
        # Base case: If we buy on the first day, profit is -prices[0] for holding the stock
        dp[0][0] = -prices[0]

        # Iterate over each day starting from day 1
        for i in range(1, len(prices)):
            # Update dp[i][1] for the maximum profit if not holding a stock on day i
            # It could be either the profit of not holding from the previous day (dp[i - 1][1])
            # or selling the stock on day i (dp[i - 1][0] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])
            
            # Update dp[i][0] for the maximum profit if holding a stock on day i
            # It could be either the profit from holding the stock from the previous day (dp[i - 1][0])
            # or buying a stock on day i (dp[i - 1][1] - prices[i])
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices[i]) # <- this is the only place different from Q1, dp[i][0] can come from dp[i - 1][1]

        # The maximum profit achievable on the last day without holding any stock
        return dp[-1][1]
# Greedy
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diff_sum = 0

        for i in range(1, len(prices)):
            # only add the increasing part of the stock price
            diff_sum += max(prices[i] - prices[i - 1], 0)
        return diff_sum
    
# Q3 123. Best Time to Buy and Sell Stock III: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize dp array with four states for each day:
        # dp[i][0]: Maximum profit on day i after the first buy
        # dp[i][1]: Maximum profit on day i after the first sell
        # dp[i][2]: Maximum profit on day i after the second buy
        # dp[i][3]: Maximum profit on day i after the second sell
        dp = [[0, 0, 0, 0] for i in range(len(prices))]
        
        # Initial states
        dp[0][0] = -prices[0]  # First buy
        dp[0][2] = -prices[0]  # Second buy (could be the same as the first if buying twice is allowed)

        # Iterate over each day starting from day 1
        for i in range(1, len(prices)):
            # Maximum profit after the first buy (either keep the previous buy or buy today)
            dp[i][0] = max(-prices[i], dp[i - 1][0])
            
            # Maximum profit after the first sell (either keep the previous sell or sell today)
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])
            
            # Maximum profit after the second buy (either keep the previous second buy or buy again today)
            dp[i][2] = max(dp[i - 1][2], dp[i - 1][1] - prices[i])
            
            # Maximum profit after the second sell (either keep the previous second sell or sell today)
            dp[i][3] = max(dp[i - 1][3], dp[i - 1][2] + prices[i])

        # The maximum profit achievable after the second sell on the last day
        return dp[-1][3]
