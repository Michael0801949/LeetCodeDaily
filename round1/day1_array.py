# Q1 binary search leetcode link: https://leetcode.com/problems/binary-search/description/

# left and right close interval answer, submition https://leetcode.com/problems/binary-search/submissions/1386992489

'''
What I did wrong before I got the correct answer: right and left should be the condition whether this loop should continue or not, not the mid
The end point would be very hard to deal with if mid is the condition to determine whether the while loop continue
It would have all kind of situation such as 3 item left in the array on the orignal array left, 2 item left on the left, etc.
wrong submition link: https://leetcode.com/problems/binary-search/submissions/1386969733
With left and right as while loop condition it would not have the problem becasue left /right pointer will move to the answer if it exist 
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while right >= left:
            mid = left + ((right-left)//2) #Used int() in the first place, floor divide is more stable int(0.99999) is equal = 1 https://www.geeksforgeeks.org/how-to-convert-float-to-int-in-python/
            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            elif target == nums[mid]:
                return mid
        return -1

# left close right open interval answer
'''
essentially it takes right (from the previous method) and + 1 as the new right
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        while right > left:
            mid = left + ((right-left)//2)
            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid
            elif target == nums[mid]:
                return mid
        return -1
# Q2 remove element leetcode link: https://leetcode.com/problems/remove-element/description/

'''
Aware of the fast slow pointer method, just need to give more attention on the detail of implimentation
The key to do a fast slow index is creating the diff between fast and slow pointer when condition met in this case there is num
when fast index = val only fast index move forward, or both of them should move forward
https://leetcode.com/problems/remove-element/submissions/1387146023
'''


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slowIndex = 0
        fastIndex = 0
        while fastIndex < len(nums):
            if nums[fastIndex] != val:
                nums[slowIndex] = nums[fastIndex]
                slowIndex += 1
            fastIndex += 1
        return slowIndex

  '''
  When visualize and impliment the the answer, need to understand: there is no different behavior of fast slow pointer when fast pointer not mach val,
  no mater there was a val match before or not. If there was no val match before, in case fastindex == slowindex, it swap with itself. That is a tricky part.
  Documenting one of my interesting answer here:
  https://leetcode.com/problems/remove-element/submissions/1387142482
  '''
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = 0
        while j + 1 <= len(nums): # changed this condition multiple times need to make sure line 80 is in range
            if nums[j] != val:
                j += 1
                i += 1
            elif nums[j] == val:
                j += 1
                while j + 1 <= len(nums) and nums[j] != val: # realized I need to pass the same condition j + 1 <= len(nums) from outer while loop to make sure in range
                    nums[i] = nums[j]
                    j += 1
                    i += 1
        return i
 '''
 logic is similar to the first answer, but it enter a while loop after find a match with val, as I mentioned before: there is not essential difference behavion when fast index not match with val
 before or after fast index find a match with val. If I delete the while loop and add nums[i] = nums[j] to the first if condition, it is the same as the first answer: https://leetcode.com/problems/remove-element/submissions/1387149571
 '''

#Q3 Squares of a Sorted Array leetcode: https://leetcode.com/problems/squares-of-a-sorted-array/description/

'''
easy built in sort method
'''
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] = nums[i]**2
        nums.sort()
        return nums
'''
2 pointer method ( I did not think about this method at first), the essential is that bigger values are at 2 ends. It also cost extra space O(n)
'''
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        k = len(nums) - 1 
        new_nums = [0] * len(nums) # can not use k here becasue k is len -1, no -1 here
        i = 0
        j = k

        while j >= i: # when j = i it show still in the loop or the number can not get append to the new list
            if nums[j]**2 >= nums[i]**2:
                new_nums[k] = nums[j]**2
                j -= 1
                k -= 1
            elif nums[j]**2 < nums[i]**2:
                new_nums[k] = nums[i]**2
                i += 1
                k -= 1
        return new_nums

  
