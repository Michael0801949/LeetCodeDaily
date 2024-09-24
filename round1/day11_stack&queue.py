# Q1 Evaluate Reverse Polish Notation: https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
'''
1. The operation order is second last item operate on last item, the order maters for dividing operation
2. For dividing, always truncates toward 0, only floor dividing is not enough, ceiling deviding when the result is negative
'''
# my aanswer
def div(x, y):
    # truncates toward zero
    return int(x / y) if x * y > 0 else -(abs(x) // abs(y))

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for i in tokens:
            if i == '+':
                a = s.pop()
                b = s.pop()
                s.append(b + a) # first out item is behind operation sign
            elif i == '-':
                a = s.pop()
                b = s.pop()
                s.append(b - a)
            elif i == '*':
                a = s.pop()
                b = s.pop()
                s.append(b * a)
            elif i == '/':
                a = s.pop()
                b = s.pop()
                s.append(div(b, a))
            else:
                s.append(int(i))
        return s.pop()
      
# using dic and operation
from operator import add, sub, mul

def div(x, y):
    #  truncates toward zero
    return int(x / y) if x * y > 0 else -(abs(x) // abs(y))

class Solution(object):
    op_map = {'+': add, '-': sub, '*': mul, '/': div}
    
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in {'+', '-', '*', '/'}:
                stack.append(int(token))
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(self.op_map[token](op1, op2))  # first out item is behind operation sign
        return stack.pop()

# Q2 Sliding Window Maximum: https://leetcode.com/problems/sliding-window-maximum/description/
'''
This problem need a data structure double end queue (deque), violent list method will exceed time limit.
Key points of deque https://www.geeksforgeeks.org/deque-in-python/:
1. Push:
    * When push a given value compare with the value in the rear, if > rear, pop value from the rear side (left) until value in the rear <= value or deque is empty. 
    Then append the value on the rear (left)
    * In this way, it makes sure the queue is decending from front to rear (ascending from rear to front)
2. Pop:
    * Check whether the given value == value in the front, if yes, pop the value in the front. Else do nothing
    * In this way, we only pop those max value when they are not in the window, do not need to operate every time the window move
* I prefer to use left as rear and right as front
'''
# violent method, complexity O(k*m)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        i = 0
        r = []
        while i + k <= len(nums):
            r.append(max(nums[i:i+k]))
            i += 1
        return r
# deque O(n) complexity
from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()#list will exceed time limit need deque
    #if push value > value in the rear, pop value from rear until push value <= value in the rear
    #in this way, keep the decending order of queue
    def push(self, value: int):
        while self.queue and value > self.queue[0]: # use while, pop until value <= value in the rear
            self.queue.popleft()
        self.queue.appendleft(value)

    #check whether the pop value == value in the front if yes pop it
    #also need to check whether queue is empty
    def pop(self, value: int):
        if self.queue and value == self.queue[-1]: #list.pop() complexity is O(n),need collections.deque()
            self.queue.pop()
    
    #find queue max return value in thr front   
    def front(self):
        return self.queue[-1]

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = Queue()
        r = []
        for i in nums[0:k]:#put first k value in the queue
            q.push(i)
        r.append(q.front()) #record the mac value in first k value
        s = k
        while s <= len(nums) - 1:
            q.pop(nums[s - k]) #remove the last value in the window
            q.push(nums[s]) #add the next value in window
            r.append(q.front()) #record max value
            s += 1
        return r

# deque, right as queue rear, left as front
from collections import deque

class MyQueue:
    def __init__(self):
        self.queue = deque() 
    
    #check whether the pop value == value in the front if yes pop it
    #also need to check whether queue is empty
    def pop(self, value):
        if self.queue and value == self.queue[0]:
            self.queue.popleft()#list.pop() complexity is O(n),need collections.deque()
            
    #if push value > value in the rear, pop value from rear until push value <= value in the rear
    #in this way, keep the decending order of queue
    def push(self, value):
        while self.queue and value > self.queue[-1]:
            self.queue.pop()
        self.queue.append(value)
        
    #find queue max return value in thr front
    def front(self):
        return self.queue[0]
    
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        que = MyQueue()
        result = []
        for i in range(k): #put first k value in the queue
            que.push(nums[i])
        result.append(que.front()) #record the mac value in first k value
        for i in range(k, len(nums)):
            que.pop(nums[i - k]) #remove the last value in the window
            que.push(nums[i]) #add the next value in window
            result.append(que.front()) #record max value
        return result
