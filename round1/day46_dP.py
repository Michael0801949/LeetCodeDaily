# 188. Best Time to Buy and Sell Stock IV: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/description/
# my answer
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        # Initialize the dp table
        # dp[i][j]: the maximum profit on day i with j transactions (where j is 1-indexed)
        # 2*k columns: odd indices represent holding a stock, even indices represent not holding
        dp = [[0] * ((2 * k) + 1) for _ in range(len(prices))]

        # Initialize the first day's states
        for i in range(2 * k):
            if i % 2 != 0:  # Odd indices represent holding a stock
                dp[0][i] = -prices[0]

        # Fill the dp table
        for i in range(1, len(prices)):  # Iterate through each day
            for j in range(1, 2 * k + 1):  # Iterate through each state
                if j % 2 != 0:  # Odd states: holding a stock
                    # Either keep holding the stock or buy a new one
                    dp[i][j] = max(dp[i - 1][j - 1] - prices[i], dp[i - 1][j])
                else:  # Even states: not holding a stock
                    # Either keep not holding or sell the stock
                    dp[i][j] = max(dp[i - 1][j - 1] + prices[i], dp[i - 1][j])

        # The maximum profit is in the last day, last state (not holding any stock after all transactions)
        return dp[-1][-1]
# optimized
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0

        # Initialize a 2D dp array where dp[i][j] represents:
        # The maximum profit on day i with state j
        dp = [[0] * (2 * k + 1) for _ in range(len(prices))]

        # Base case: On day 0, initialize odd indices (holding a stock after the j-th transaction)
        for j in range(1, 2 * k, 2):
            dp[0][j] = -prices[0]

        # Fill the dp array for the rest of the days
        for i in range(1, len(prices)):  # Loop through each day
            for j in range(0, 2 * k - 1, 2):  # Loop through transaction states
                # Transition for holding a stock (odd state)
                dp[i][j + 1] = max(dp[i - 1][j + 1], dp[i - 1][j] - prices[i])

                # Transition for not holding a stock (even state)
                dp[i][j + 2] = max(dp[i - 1][j + 2], dp[i - 1][j + 1] + prices[i])

        # The maximum profit achievable is in dp[-1][2*k] (not holding stock after k transactions)
        return dp[-1][2 * k]

# 1-D DP
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # If there are no prices, no transactions can be made, so return 0
        if len(prices) == 0:
            return 0

        # Initialize dp array for `2*k + 1` states
        # dp[j] represents the maximum profit with state `j`
        dp = [0] * (2 * k + 1)

        # Initialize odd indices (holding a stock after the j-th transaction)
        for i in range(1, 2 * k, 2):
            dp[i] = -prices[0]

        # Iterate over each day
        for i in range(1, len(prices)):
            # Update dp array for all states
            for j in range(1, 2 * k + 1):
                if j % 2:  # Odd indices: holding a stock
                    # Either keep holding the stock or buy on day i
                    dp[j] = max(dp[j], dp[j - 1] - prices[i])
                else:  # Even indices: not holding a stock
                    # Either keep not holding the stock or sell on day i
                    dp[j] = max(dp[j], dp[j - 1] + prices[i])

        # The maximum profit achievable is stored in dp[2*k] (not holding any stock after k transactions)
        return dp[2 * k]

# 309. Best Time to Buy and Sell Stock with Cooldown: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Initialize dp array where:
        # dp[i][0]: Maximum profit on day i if holding a stock after any purchase
        # dp[i][1]: Maximum profit on day i if selling a stock
        # dp[i][2]: Maximum profit on day i if not holding a stock after selling (stay idle)
        # dp[i][3]: Maximum profit on day i if buying a second stock (transitional state)
        dp = [[0] * 4 for _ in range(len(prices))]
        
        # Base case: On day 0
        dp[0][0] = -prices[0]  # First purchase
        dp[0][3] = -prices[0]  # Buying a stock for the second transaction (if allowed)

        # Fill dp array for subsequent days
        for i in range(1, len(prices)):
            # Max profit after purchasing a stock on day i
            dp[i][0] = max(-prices[i], dp[i - 1][0], dp[i - 1][2] - prices[i])

            # Max profit after selling a stock on day i
            dp[i][1] = dp[i - 1][0] + prices[i]

            # Max profit after staying idle (not holding stock) on day i
            dp[i][2] = max(dp[i - 1][1], dp[i - 1][2])

        # Return the maximum profit on the last day
        # Either we have sold the stock (dp[-1][1]) or stayed idle (dp[-1][2])
        return max(dp[-1][1], dp[-1][2])

# Alternative Approach
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        
        # Initialize the dp array with 4 states for each day:
        # dp[i][0]: Maximum profit on day i if holding a stock
        # dp[i][1]: Maximum profit on day i if not holding a stock and in cooldown
        # dp[i][2]: Maximum profit on day i if not holding a stock and not in cooldown
        # dp[i][3]: Maximum profit on day i if selling a stock and entering cooldown
        dp = [[0] * 4 for _ in range(n)]
        
        # Base case: On the first day
        dp[0][0] = -prices[0]  # If holding a stock, profit is -prices[0]
        
        # Fill the dp array for subsequent days
        for i in range(1, n):
            # Maximum profit on day i if holding a stock
            dp[i][0] = max(dp[i - 1][0], max(dp[i - 1][3], dp[i - 1][1]) - prices[i])
            
            # Maximum profit on day i if not holding a stock and in cooldown
            dp[i][1] = dp[i - 1][0] + prices[i]
            
            # Maximum profit on day i if not holding a stock and not in cooldown
            dp[i][2] = max(dp[i - 1][1], dp[i - 1][3])
            
            # Maximum profit on day i if selling a stock and entering cooldown
            dp[i][3] = dp[i - 1][2]
        
        # The maximum profit on the last day without holding a stock
        return max(dp[n - 1][1], dp[n - 1][2], dp[n - 1][3])

# 714. Best Time to Buy and Sell Stock with Transaction Fee https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/description/
class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        # Initialize dp array:
        # dp[i][0]: Maximum profit on day i if holding a stock
        # dp[i][1]: Maximum profit on day i if not holding a stock
        dp = [[0, 0] for _ in range(len(prices))]
        
        # Base case: On the first day
        dp[0][0] = -prices[0]  # If holding a stock, profit is -prices[0]
        dp[0][1] = 0  # If not holding a stock, profit is 0

        # Fill dp array for subsequent days
        for i in range(1, len(prices)):
            # Max profit on day i if holding a stock
            # Either keep holding the stock or buy on day i
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices[i])

            # Max profit on day i if not holding a stock
            # Either keep not holding or sell the stock on day i (subtract transaction fee)
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i] - fee)

        # The maximum profit on the last day without holding a stock
        return dp[-1][1]
