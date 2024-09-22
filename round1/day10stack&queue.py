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
