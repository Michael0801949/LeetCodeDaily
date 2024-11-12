# Q1 322. Coin Change: https://leetcode.com/problems/coin-change/description/
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Initialize a dp array where dp[j] represents the minimum number of coins to make amount j
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0  # Base case: zero coins are needed to make amount 0

        # Loop over each coin
        for coin in coins:
            # Update dp array for each amount j from coin value up to the target amount
            for j in range(coin, amount + 1):
                # Choose the minimum number of coins between not using the coin and using it
                dp[j] = min(dp[j], dp[j - coin] + 1)
                # Uncomment the next line to see the dp array at each step
                # print(dp)
        
        # If dp[amount] is still infinity, it means the amount cannot be formed by any combination of coins
        if dp[amount] == float('inf'):
            return -1
        
        # Otherwise, return the minimum number of coins to make the target amount
        return dp[amount]

# Q2 279. Perfect Squares: https://leetcode.com/problems/perfect-squares/
'''
Very similar to Q1 322. Coin Change
'''
class Solution:
    def numSquares(self, n: int) -> int:
        # Find the largest integer whose square is <= n
        r = math.floor(math.sqrt(n))
        
        # Generate a list of all perfect squares up to n
        itemList = [i**2 for i in range(1, r + 1)]
        print(itemList)  # Debug print to show the list of perfect squares

        # Initialize a dp array where dp[j] represents the minimum number of perfect squares to sum up to j
        dp = [float('inf')] * (n + 1)
        dp[0] = 0  # Base case: zero squares are needed to reach sum 0

        # Loop over each perfect square in itemList
        for i in itemList:
            # Update dp array for each amount j from i up to n
            for j in range(i, n + 1):
                # Update dp[j] to the minimum number of squares between not using or using the square i
                dp[j] = min(dp[j], dp[j - i] + 1)

        # If dp[n] is still infinity, it means n cannot be formed by any combination of squares
        if dp[n] == float('inf'):
            return -1
        
        # Return the minimum number of squares to reach the target number n
        return dp[n]
#Q3 139.Word Break: https://leetcode.com/problems/word-break/
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Initialize a dp array where dp[j] indicates if s[:j] can be segmented into words from wordDict
        dp = [False] * (len(s) + 1)
        dp[0] = True  # Base case: an empty string can be segmented

        # Iterate over each position j in the string s
        for j in range(1, len(s) + 1):
            # Check each word in wordDict
            for i in wordDict:
                # Check if the current word can fit into the substring ending at j
                if j >= len(i) and dp[j - len(i)] and s[j - len(i): j] == i:
                    dp[j] = True  # Mark dp[j] as True if s[:j] can be segmented
                print(dp)  # Debug print to observe the state of dp after each iteration
        return dp[len(s)]  # Return whether the entire string can be segmented
# Method 2:
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Initialize dp array where dp[j] represents if s[:j] can be segmented using words from wordDict
        dp = [False] * (len(s) + 1)
        dp[0] = True  # Base case: an empty string can always be segmented

        # Iterate over each possible length j of substring s[:j]
        for j in range(1, len(s) + 1):  # Traverse all possible substring endpoints
            # For each position j, check all words in wordDict
            for word in wordDict:  # Traverse each word in the dictionary
                # Check if the word can fit at the end of the substring s[:j]
                if j >= len(word):
                    # Update dp[j] to True if the word matches the end of s[:j] and s[:j-len(word)] can be segmented
                    dp[j] = dp[j] or (dp[j - len(word)] and word == s[j - len(word):j])
        
        # Return whether the entire string can be segmented
        return dp[len(s)]
    
# Use set
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Convert wordDict to a set for faster lookup
        wordSet = set(wordDict)
        n = len(s)
        
        # Initialize dp array where dp[i] indicates if the substring s[:i] can be segmented into words from wordDict
        dp = [False] * (n + 1)
        dp[0] = True  # Base case: an empty string can be segmented

        # Iterate over each possible substring length i from 1 to n
        for i in range(1, n + 1):  # Traverse all possible substring endpoints
            # For each i, check all possible starting points j
            for j in range(i):  # Traverse all possible starting points for the substring ending at i
                # Check if s[j:i] is a word in wordSet and if s[:j] can be segmented
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True  # Mark dp[i] as True if s[:i] can be segmented
                    break  # Stop early since we found a valid segmentation for s[:i]

        # Return whether the entire string can be segmented
        return dp[n]