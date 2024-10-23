# Q1 134. Gas Station: https://leetcode.com/problems/gas-station/
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_tank = 0  # Tracks overall gas availability vs cost.
        curr_tank = 0   # Tracks current gas level as we traverse stations.
        start_index = 0 # Tracks the starting point of the journey.

        for i in range(len(gas)):
            # Calculate the difference between available gas and cost at station i
            total_tank += gas[i] - cost[i]
            curr_tank += gas[i] - cost[i]
            
            # If at any point, current gas (curr_tank) becomes negative,
            # it means we can't continue from the current start_index to the next station.
            if curr_tank < 0:
                # We need to reset the starting index to the next station (i + 1)
                start_index = i + 1
                curr_tank = 0  # Reset the current tank because we will try starting from the next station.
        
        # If total_tank is negative, there isn't enough gas overall to complete the circuit.
        # If total_tank >= 0, then we know there is enough gas in total, and the start_index we found will work.
        return start_index if total_tank >= 0 else -1

# Q2 135. Candy: https://leetcode.com/problems/candy/description/
class Solution:
    def candy(self, ratings: List[int]) -> int:
        # initialize a result list to collect number of candy of each student
        result = [1] * len(ratings)

        # iterate rating list from left to right, compare rating value with value on the left
        # if > value on the left, reuslt = left result + 1
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                result[i] = result[i - 1] + 1
        # iterate rating list from left to right, compare rating value with value on the right
        # if > value on the right, reuslt = max ( right result + 1, the value we already given compared with value on left)
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                result[i] = max(result[i + 1] + 1, result[i])
        # retun total sum
        return sum(result)

# Q3 860. Lemonade Change: https://leetcode.com/problems/lemonade-change/description/
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # Initialize counters for the number of $5 and $10 bills
        five = 0
        ten = 0
        
        # Loop through each bill in the bills list
        for bill in bills:
            # If the customer gives a $5 bill, no change is needed, so just increment the $5 count
            if bill == 5:
                five += 1
                
            # If the customer gives a $10 bill, give back one $5 bill as change
            elif bill == 10:
                five -= 1  # Decrease the $5 count since we give one as change
                ten += 1   # Increase the $10 count as we received one
                # If we don't have enough $5 bills to give change, exit the loop
                if five < 0:
                    break
            
            # If the customer gives a $20 bill, we prefer to give one $10 and one $5 as change
            elif bill == 20:
                if ten > 0:  # If we have a $10 bill, give it along with a $5 bill
                    ten -= 1
                    five -= 1
                else:  # If no $10 bill is available, give three $5 bills
                    five -= 3
                
                # If we don't have enough $5 or $10 bills to give the correct change, exit the loop
                if five < 0 or ten < 0:
                    break
        
        # Return True if we successfully gave change to all customers, False otherwise
        return five >= 0 and ten >= 0

# Q4 406. Queue Reconstruction by Height https://leetcode.com/problems/queue-reconstruction-by-height/description/
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # First, sort the list of people by height in descending order (h), 
        # and if two people have the same height, sort by the number of people in front (k) in ascending order.
        # The lambda function returns a tuple: 
        # -x[0] ensures the height (h) is sorted from high to low, and x[1] sorts k from low to high if heights are the same.
        people.sort(key=lambda x: (-x[0], x[1]))
        
        # Initialize an empty queue to reconstruct the order
        que = []
        
        # Insert each person into the queue at the index specified by their second dimension k.
        # Since the list is sorted, we can safely insert each person at their k position,
        # because all taller people (or people with lower k) are already placed in the queue.
        for p in people:
            que.insert(p[1], p)  # Insert person p at index p[1] in the queue.
        
        # Return the reconstructed queue
        return que