# Q1 122. Best Time to Buy and Sell Stock II: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize variables to store the total profit (diff_sum)
        # and the difference between consecutive prices (diff)
        diff_sum = 0
        diff = 0

        # Loop through the list of prices starting from the second element
        for i in range(1, len(prices)):
            # Calculate the difference between the current price and the previous one
            diff = prices[i] - prices[i - 1]
            
            # If the price increased (i.e., diff is positive), add the difference to diff_sum
            if diff > 0:
                diff_sum += diff
            else:
                # If the price decreased or stayed the same, skip this iteration
                continue
        
        # Return the total profit which is the sum of all positive price differences
        return diff_sum

# simplified version
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diff_sum = 0

        for i in range(1, len(prices)):
            diff_sum += max(prices[i] - prices[i - 1], 0)
        return diff_sum

# Q2 55. Jump Game: https://leetcode.com/problems/jump-game/description/
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Initialize 'i' as the current position and 'cover' as the furthest position we can reach
        i = 0
        cover = 0

        # If the list has only one element, we are already at the last index, so return True
        if len(nums) == 1:
            return True
        
        # Iterate while the current index 'i' is within the reachable range ('cover')
        # can not use for loop here becasue python for loop does not support dynamic modify variable such as covor
        while i <= cover:
            # Update the furthest position we can reach by checking the current position and jump range
            cover = max(i + nums[i], cover)
            print(cover)  # Debugging: print the current value of 'cover'
            
            # If the furthest reachable position is greater than or equal to the last index, return True
            if cover >= len(nums) - 1:
                return True
            
            # Move to the next position
            i += 1
        
        # If we exit the loop, it means we couldn't reach the last index, so return False
        return False
    
# for loop version
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Initialize 'cover' to track the furthest position we can reach
        cover = 0
        
        # If there's only one element, we're already at the last index, return True
        if len(nums) == 1:
            return True
        
        # Iterate through the list
        for i in range(len(nums)):
            # Check if the current index 'i' is within the reach of 'cover'
            if i <= cover:
                # Update 'cover' to the maximum of the current reach and the furthest reachable index from current position
                cover = max(i + nums[i], cover)
                
                # If 'cover' reaches or exceeds the last index, return True
                if cover >= len(nums) - 1:
                    return True
        
        # If loop finishes and 'cover' couldn't reach the last index, return False
        return False

# Q3 45. Jump Game II: https://leetcode.com/problems/jump-game-ii/description/
class Solution:
    def jump(self, nums: List[int]) -> int:
        # If the input list has less than 2 elements, no jump is needed.
        if len(nums) < 2:
            return 0
        
        # `curr_jump` tracks the farthest index we can reach with the current jump
        curr_jump = 0
        
        # `next_jump` tracks the farthest index we can reach with the next jump
        next_jump = 0
        
        # `result` counts the minimum number of jumps needed to reach the end
        result = 0
        
        # `i` is the index we are currently examining
        i = 0
        
        # Loop through the array until we reach the end
        while i < len(nums):
            # Update `next_jump` to the farthest we can reach from the current index
            next_jump = max(i + nums[i], next_jump)
            print(next_jump)  # This print statement can be removed; it helps in debugging by showing the farthest index reachable at each step
            
            # If we've reached the end of the current jump (i == curr_jump), we need to make a new jump
            if i == curr_jump:
                # If the current jump doesn't reach the end, increment the jump count
                if curr_jump < len(nums) - 1:
                    result += 1  # Increment the number of jumps
                    curr_jump = next_jump  # Update `curr_jump` to `next_jump`
                    
                    # If the current jump reaches or exceeds the last index, we can stop
                    if curr_jump >= len(nums) - 1:
                        break
                else:
                    break  # Break if we have already reached the end
            i += 1  # Move to the next index
        
        # Return the total number of jumps required to reach the end
        return result

# simplified version
class Solution:
    def jump(self, nums):
        cur_distance = 0  # The farthest index that can be reached with the current jump
        ans = 0  # Record the number of jumps made
        next_distance = 0  # The farthest index that can be reached with the next jump
        
        # Loop through the array, but note that the loop runs until len(nums) - 1
        # because we don't need to jump from the last element
        for i in range(len(nums) - 1):  # Note the key detail: we stop before the last element
            # Update the farthest index that can be reached with the next jump
            next_distance = max(nums[i] + i, next_distance)
            
            # When we reach the farthest point that can be covered by the current jump
            if i == cur_distance:
                # Update the current jump's farthest reachable index
                cur_distance = next_distance
                # Increment the number of jumps made
                ans += 1
        
        return ans

# Q4 1005. Maximize Sum Of Array After K Negations: https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/description/
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        while k > 0 and i < len(nums):
            # if there are negative numbers, make the bigger negative number positive first
            # while condition need to be carry forward to prevent out of boundary
            while i < len(nums) and nums[i] < 0 and k > 0:
                nums[i] = -nums[i]
                i += 1
                k -= 1
            # sort number make smallest postive number negative
            nums.sort()
            # if make the smallest number even number of times negative, it will still be positive
            if nums[0] == 0 or k % 2 == 0:
                return sum(nums)
            # if make it odd number of times negative, it will be negative
            else:
                return sum(nums[1:]) - nums[0]
