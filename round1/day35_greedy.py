# Q1 452. Minimum Number of Arrows to Burst Balloons https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # If the input list is empty, return 0 as no arrows are needed
        if not points:
            return 0
        
        # Sort the points based on the x-coordinates of their starting positions
        points.sort()
        
        # Initialize min_upper with the end of the first balloon's range (the rightmost coordinate)
        min_upper = points[0][1]
        
        # Initialize the result to 1 since we need at least one arrow to burst the first balloon
        result = 1
        
        # Iterate through the sorted list of balloons, starting from the second one
        for i in range(1, len(points)):
            # If the current balloon's start position is beyond the current range (min_upper),
            # it means we need a new arrow to burst this balloon
            if points[i][0] > min_upper:
                result += 1  # Increment the arrow count
                # Update min_upper to the end of the current balloon's range
                min_upper = points[i][1]
            else:
                # If the current balloon overlaps with the previous one, update min_upper
                # to the smaller end of the two overlapping balloons
                min_upper = min(min_upper, points[i][1])
        
        # Return the total number of arrows needed
        return result

# Q2 435. Non-overlapping Intervals https://leetcode.com/problems/non-overlapping-intervals/
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # If there are fewer than 2 intervals, there's no overlap, so return 0
        if len(intervals) < 2:
            return 0
        
        # Sort the intervals by their starting point
        intervals.sort()
        
        # Initialize min_upper with the end of the first interval
        min_upper = intervals[0][1]
        
        # Initialize result to count the number of overlapping intervals to be removed
        result = 0
        
        # Iterate through the sorted list of intervals, starting from the second one
        for i in range(1, len(intervals)):
            # If the current interval starts before the end of the previous interval (overlap)
            if intervals[i][0] < min_upper:
                result += 1  # Increment the count of overlaps to be removed
                # If there's an overlap, we update min_upper to the smaller end of the overlapping intervals
                # This minimizes the chance of overlapping with future intervals
                min_upper = min(min_upper, intervals[i][1])
            else:
                # If no overlap, update min_upper with the end of the current interval
                min_upper = intervals[i][1]
        
        # Return the number of intervals that need to be removed to eliminate all overlaps
        return result


# Q3 763. Partition Labels https://leetcode.com/problems/partition-labels/description/
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Create a dictionary to store the last occurrence of each character in the string
        last_occurrence = {}
        for i, ch in enumerate(s):
            last_occurrence[ch] = i  # Store the index of the last occurrence of the character

        # Initialize an empty list to store the lengths of partitions
        result = []
        
        # Initialize 'start' and 'end' to mark the start and end of the current partition
        start = 0
        end = 0

        # Iterate over the string to determine the partitions
        for i, ch in enumerate(s):
            # Update the 'end' of the current partition to the furthest last occurrence of the current character
            end = max(end, last_occurrence[ch])
            
            # If the current index reaches the furthest position for this partition
            if i == end:
                # Append the size of the partition to the result list
                result.append(end - start + 1)
                
                # Update 'start' to the beginning of the next partition
                start = i + 1

        # Return the list of partition lengths
        return result
