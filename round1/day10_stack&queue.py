#Implement Queue using Stacks: https://leetcode.com/problems/implement-queue-using-stacks/description/

'''
get farmiliar with queue and stack
'''
# Answer
class MyQueue:

    def __init__(self):
        self.stack_in = [] # handle all the item coming in
        self.stack_out = [] # handle all the item coming out

    def push(self, x: int) -> None:
        self.stack_in.append(x)
        

    def pop(self) -> int:
        if self == []:
            return None
        elif self.stack_out:
            return self.stack_out.pop()
        else:
            while self.stack_in:
                # transfer all the element from stack_in to stack_out with order reversed
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out.pop()


    def peek(self) -> int:
        # reuse the pop method we write above
        result = self.pop()
        # add the element back since we are not removing it from queue
        self.stack_out.append(result)
        return result
        

    def empty(self) -> bool:
        # both in and out are empty then we can say the queue is empty
        return not (self.stack_in or self.stack_out)

# 225. Implement Stack using Queues https://leetcode.com/problems/implement-stack-using-queues/description/
'''
If use 2 queue to simulate a stack it is the same as Q1,
Need to realize 1 queue can simulate 1 stack.
Queue is not like stack (add item and access from the same end), queue add item from one end and access from another end.
This character helps us append back the pop item to simulate stack with just 1 Queue
'''

# 1 list simulite
class MyStack:
    def __init__(self):
        self.queue = []
        
    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        if not self.queue:  # Check if the queue is empty
            return None

        i = 0
        # Rotate the queue to bring the last pushed element to the front
        while i <= len(self.queue) - 2:
            self.queue.append(self.queue.pop(0))
            i += 1
        pop_item = self.queue.pop(0)
        # Pop the first element which is the last pushed element
        return pop_item
        
    def top(self) -> int:
        top_item = self.queue.pop()
        # Return the last pushed element without removing it
        self.queue.append(top_item)
        return top_item

    def empty(self) -> bool:
        return not self.queue
        
# use deque()
    def __init__(self):
        self.que = deque()

    def push(self, x: int) -> None:
        self.que.append(x)

    def pop(self) -> int:
        if self.empty():
            return None
        for i in range(len(self.que)-1):
            self.que.append(self.que.popleft())
        return self.que.popleft()

    def top(self) -> int:
        # method 1：
        # if self.empty():
        #     return None
        # return self.que[-1]

        # method2：
        if self.empty():
            return None
        for i in range(len(self.que)-1):
            self.que.append(self.que.popleft())
        temp = self.que.popleft()
        self.que.append(temp)
        return temp

    def empty(self) -> bool:
        return not self.que
# Q3 Valid Parentheses: https://leetcode.com/problems/valid-parentheses/description/
'''
There are 3 senerios:
1. Miss match paratheses
2. Extra paratheses on the left
3. Extra paratheses on the right
'''

# My answer, I did not map open paratheses to close paratheses
class Solution:
    def isValid(self, s: str) -> bool:
        if s == '':
            return True
        if s == ']' or s == '}' or s == ')' or s == '[' or s == '{' or s == '(':
            return False 
        slist = list(s)
        stack = []
        for i in slist:
            if i in [ '(' , '{' , '[' ]: # append if open
                stack.append(i)
            elif i in [ ')' , '}' , ']' ] and stack == []: # I missed this situation in the first try, extra paratheses on the right side
                return False
            elif i == ')' and stack[-1] != '(' or i == ']' and stack[-1] != '[' or i == '}' and stack[-1] != '{': # check if not match return False
                return False
            elif i == ')' and stack[-1] == '(' or i == ']' and stack[-1] == '[' or i == '}' and stack[-1] == '{': # check if match pop
                stack.pop()
        return stack == []

# map open paratheses to close paratheses, code is more concise 
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        slist = list(s)

        for i in slist:
            if i == '(':
                stack.append(')')
            elif i == '[':
                stack.append(']')
            elif i == '{':
                stack.append('}')
            elif not stack or i != stack[-1]:
                return False
            else:
                stack.pop()
        return stack == []
        
# create a new dictionary to map open close paratheses
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        slist = list(s)
        dic = {'(':')', '[': ']', '{': '}'}

        for i in slist:
            if i in dic.keys():
                stack.append(dic[i])
            elif not stack or i != stack[-1]:
                return False
            else:
                stack.pop()
        return stack == []
# Remove All Adjacent Duplicates In String: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/description/
'''
Did not thought about using stack in the first place, but then I realized it is the same as Q2
'''

# use just 2 while loop, barely pass performance, complexity N**2
class Solution:
    def removeDuplicates(self, s: str) -> str:
        slist = list(s)
        i = 0
        while i <= len(slist) - 1:
            while i >= 1 and slist[i] == slist[i-1]:
                slist = slist[0:i - 1] + slist[i + 1:]
                i = i - 2 # go back to the item before removed item to see whether there are new adjacent dup created because of the removal
            i += 1
        return ''.join(slist)


# Use Stack
class Solution:
    def removeDuplicates(self, s: str) -> str:
        sl = list(s)
        stack = []
        for i in sl:
            if stack and stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
        return ''.join(stack)
# fast slow pointer
class Solution:
    def removeDuplicates(self, s: str) -> str:
        res = list(s)
        slow = fast = 0
        length = len(res)

        while fast < length:
            # keep swapping move the different item to slow
            res[slow] = res[fast]
            
            # if same item, slow -= 1
            if slow > 0 and res[slow] == res[slow - 1]:
                slow -= 1
            else:
                slow += 1
            fast += 1
            
        return ''.join(res[0: slow])

        
