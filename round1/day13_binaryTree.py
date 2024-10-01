# q1 226. Invert Binary Tree: https://leetcode.com/problems/invert-binary-tree/description/

# the method I prefer: bfs

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: # input validation

            return None
        q = deque([root]) # queue point to the root at begining

        while q: # untill no element in queue
            curr = q.pop() # curr is a pointer point to the earliest node leftappended to q
            if curr.left or curr.right: # if the curr node have a left or right child, swap them
                curr.left, curr.right = curr.right, curr.left
            if curr.left: # if ahve a left child, append to queue
                q.appendleft(curr.left)
            if curr.right: # if ahve a right child, append to queue
                q.appendleft(curr.right)
        return root

# q2 101. Symmetric Tree: https://leetcode.com/problems/symmetric-tree/description/
'''
Key Points of recursive:
1. Parameter and return value: specify which parameters need to be processed in the recursion, add as parameter. 
   Specify what need to be return in each level of recursion, confirm the return data type of recursive function
2. Specify recursion end condition: if encounter stack overflow, it is usually caused by wrong end condition. Recursion depend on
   stack to store information on each recursive layer
3. Specify single layer logic: specify what logic need to be implimented on each single layer
'''
# Recursive (post order iteration):
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        leftNode = root.left
        rightNode = root.right
        return self.isEqual(leftNode, rightNode)
    

    def isEqual(self, leftNode, rightNode) -> bool: # parameters are the leftNode and rightNode, take one node from right and left see whether tehy are the same to determine symmetric
        if not leftNode and not rightNode: # End Condition 1: left and right node are both None
            return True
        elif not leftNode and rightNode is not None or not rightNode and leftNode is not None: # End Condition 2: left and right node are both None
            return False
        elif leftNode.val != rightNode.val: # End Condition 3: left and right value are different
            return False
        # Continue recursion if does not meet end condition, add logic move to the next Node
        # Need to eveluate whether outside equal and inside equal
        outside = self.isEqual(leftNode.left, rightNode.right)
        inside = self.isEqual(leftNode.right, rightNode.left)
        # return the final boolean from when the end condition meet, if both True return True, else return False
        return outside and inside

# q3 104. Maximum Depth of Binary Tree：https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

# recursicive (post order iteration):
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.depth(root)
        
    def depth(self, node:Optional[TreeNode]) -> int:
        if not node: # end condition return 0 when node does not exsit
            return 0
        # need to process the info from both left and right and add 1 for the current layer
        leftDepth = self.depth(node.left) + 1
        rightDepth = self.depth(node.right) + 1
        
        # return the max of left and right as final value
        return max(leftDepth, rightDepth)
# q4 111. Minimum Depth of Binary Tree: https://leetcode.com/problems/minimum-depth-of-binary-tree/description/

# recursicive (post order iteration):
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        return self.depth(root)
    
    def depth(self, node: Optional[TreeNode]) -> int:
        if not node:  # end condition return 0 when node does not exsit
            return 0 
        leftNode = self.depth(node.left)
        rightNode = self.depth(node.right)
        if not node.left and node.right:
           return  rightNode + 1 # need to return a different recursive logic here becasue the leaf node has not been reach
        elif not node.right and node.left:
           return leftNode + 1 # need to return a different recursive logic here becasue the leaf node has not been reach
        else:
            return min(leftNode, rightNode) + 1  # same logic as q3, compare lef and right return the min