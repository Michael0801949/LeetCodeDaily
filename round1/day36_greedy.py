# Q1 56. Merge Intervals: https://leetcode.com/problems/merge-intervals/description/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort intervals based on the starting times
        intervals.sort()
        
        # Initialize the right boundary of the current interval and the current interval itself
        r_boundary = intervals[0][1]
        curr = intervals[0]
        
        # Initialize the result list to store merged intervals
        result = []
        
        # Start from the second interval and iterate through the list
        i = 1
        while i < len(intervals):
            # If the current interval overlaps with the previous one (current right boundary)
            if intervals[i][0] <= r_boundary:
                # Update the right boundary to the farthest end of the overlapping intervals
                r_boundary = max(intervals[i][1], r_boundary)
                # Update the end of the current interval to the new right boundary
                curr[1] = r_boundary
                i += 1
            else:
                # If no overlap, add the current interval to the result list
                result.append(curr)
                # Move to the next interval and update the current interval and right boundary
                curr = intervals[i]
                r_boundary = intervals[i][1]
                i += 1
        
        # Add the last merged interval to the result list
        result.append(curr)
        
        return result
    
# simplified
class Solution:
    def merge(self, intervals):
        result = []

        # If the list of intervals is empty, return an empty result
        if len(intervals) == 0:
            return result

        # Sort intervals by the starting boundary of each interval
        intervals.sort(key=lambda x: x[0])

        # Add the first interval to the result as the initial merged interval
        result.append(intervals[0])

        # Iterate over the intervals starting from the second one
        for i in range(1, len(intervals)):
            # If the current interval overlaps with the last interval in result
            if result[-1][1] >= intervals[i][0]:
                # Merge the intervals by updating the end of the last interval
                # in result to the farthest end point of the two overlapping intervals
                result[-1][1] = max(result[-1][1], intervals[i][1])
            else:
                # If there is no overlap, add the current interval to the result
                result.append(intervals[i])

        return result



# Q2 738. Monotone Increasing Digits: https://leetcode.com/problems/monotone-increasing-digits/description/
'''
1. make the previous digit -1, and the current digit 9 to max the number
2. iterate from back to front to utilize the result from last round iteration, make sure the current digit > previous dight
'''
# method 1
class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        # Convert the integer to a list of its digits for easy manipulation
        l = list(map(int, str(n)))
        
        # First pass: make adjustments where the digits decrease from left to right
        for i in range(len(l) - 1, 0, -1):
            # If a digit is smaller than the previous one, adjust to maintain non-decreasing order
            if l[i] < l[i - 1]:
                l[i] = 9  # Set the current digit to 9
                l[i - 1] -= 1  # Decrease the previous digit by 1

        # Second pass: ensure all digits after a change are set to '9' to maximize the result
        for i in range(1, len(l)):
            # If a digit is less than the previous digit, set it to 9 to maintain monotone increase
            if l[i] < l[i - 1]:
                l[i] = 9

        # Convert the list of digits back to an integer and return the result
        return int("".join(map(str, l)))

    
# method 2:
class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        # Convert the integer to a list of characters for easier manipulation
        strNum = list(str(N))

        # Traverse the list from right to left
        for i in range(len(strNum) - 1, 0, -1):
            # If the current digit is smaller than the previous one,
            # it means the number is no longer monotone increasing
            if strNum[i - 1] > strNum[i]:
                # Decrease the previous digit by 1 to maintain monotone increasing order
                strNum[i - 1] = str(int(strNum[i - 1]) - 1)
                # Set all digits after the current position to '9' to maximize the result
                # while preserving the monotone increasing property
                strNum[i:] = '9' * (len(strNum) - i)

        # Convert the list back to a string, then to an integer, and return
        return int(''.join(strNum))

# simplified:
class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        # Convert the integer to a string for easy manipulation of each digit
        strNum = str(N)
        
        # Traverse the string from right to left to check for decreasing pairs
        for i in range(len(strNum) - 1, 0, -1):
            # If the current digit is less than the previous one, adjust the previous digit
            if strNum[i - 1] > strNum[i]:
                # Decrease the previous digit by 1 to ensure monotone increasing property
                # Use string slicing to concatenate the adjusted part with '9's to maximize result
                strNum = strNum[:i - 1] + str(int(strNum[i - 1]) - 1) + '9' * (len(strNum) - i)
        
        # Convert the modified string back to an integer and return
        return int(strNum)
