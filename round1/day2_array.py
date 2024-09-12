# Q1 minimum size subarray sum https://leetcode.com/problems/minimum-size-subarray-sum/

'''
The essence of this problem is the slide window. The essence of slide window (kinda of similar to the the fast and slow pointer)
is determine when to move the fast pointer and when to move the slow pointer. 
In the previous remove element problem (https://leetcode.com/problems/remove-element/description/) fast pointer is moved to the value need to be added to the new array, 
slow pointer is moved to the position of the new element. 
for this problem the "slow pointer" is moved when we find a match, the fast pointer keep moving until we fin a match
'''

# my solution timed out in submition test https://leetcode.com/problems/minimum-size-subarray-sum/submissions/1388009038, 
# I have not understand understand why it times out yet, it is the same logic as the the solutuion
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i, j = 0, 0
        min_len = len(nums)
        while j <= len(nums) - 1:
            if j == len(nums) - 1 and i == 0 and sum(nums[i:j+1]) < target: # this condition must be put in the first place since it has overlap with condition 2
                return 0                                                    # need to remember sub list is left close right open interval, to include right side need to have right + 1
            elif sum(nums[i:j+1]) < target:
                j += 1
            elif sum(nums[i:j+1]) >= target:
                min_len = min(min_len, j - i + 1)
                i += 1
        return min_len
#Solution
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        sum_array = 0
        sub_length = 0
        result = float('inf') # this is how to initialize a float in python3, it helps to store result, since initialize with 0 will always get return in min()
        for j in range(0, len(nums)): # range is also right close left open interval, to iterate through the array, do not len(nums) - 1 just use len(nums)
            sum_array += nums[j]
            while sum_array >= target:
                sub_length = j - i + 1
                if result is None:
                     result = sub_length
                else:
                    result = min(result, sub_length)
                sum_array -= nums[i]
                i += 1
        if result != float('inf'):
            return result
        else: 
            return 0 
