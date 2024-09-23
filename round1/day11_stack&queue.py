# Evaluate Reverse Polish Notation: https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
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

