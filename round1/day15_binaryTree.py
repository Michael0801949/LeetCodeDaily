# Q1 110. Balanced Binary Tree https://leetcode.com/problems/balanced-binary-tree/description/

# My Answer （post order recursive + iteration with queue)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        queue = deque()
        queue.appendleft(root)
        while queue: # while there is still node in the queue
            node = queue.pop()
            heightDiff = abs(self.height(node.left) - self.height(node.right)) # calcualte the height difference
            if heightDiff > 1: # if difference > 1 return False no need farther iteration
                return False
            # add node to queue
            if node.left:
                queue.appendleft(node.left)
            if node.right:
                queue.appendleft(node.right)
        return True
    
    # calculate height of node post order iteration
    def height(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        leftHeight = self.height(node.left) + 1
        rightHeight = self.height(node.right) + 1

        height = max(leftHeight, rightHeight)

        return height

        
# recursive solution, using the trick return -1 when diff > 1

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if self.get_height(root) != -1:
            return True
        else:
            return False

    def get_height(self, root: TreeNode) -> int:
        # the start value when reach end of tree
        if not root:
            return 0
        # if there is already a imbalance on the left side
        if (left_height := self.get_height(root.left)) == -1:
            return -1
        # if there is already a imbalance on the right side
        if (right_height := self.get_height(root.right)) == -1:
            return -1
        # process the information return from left and right side
        # if there is a imbalance in the current node level return -1
        if abs(left_height - right_height) > 1:
            return -1
        # else continue recursion 
        height = 1 + max(left_height, right_height)
        return height

# Q2 257. Binary Tree Paths https://leetcode.com/problems/binary-tree-paths/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []
        path = []
        if not root:
            return result
        self.traval(path, result, root)
        return result

    def traval(self, path: list, result: list, curr:Optional[TreeNode]):
        path.append(curr.val)
        # stop condition when reach the end of the tree
        if not curr.left and not curr.right:
            pathString = '->'.join(map(str, path))
            result.append(pathString)
            return
        if curr.left:
            # recursion move to the next level when there is a left/right child
            self.traval(path, result, curr.left)
            # backtracking with pop, remove the node append in the recursion and continue move to the right child
            path.pop()
        if curr.right:
            self.traval(path, result, curr.right)
            path.pop()

# simplified 1: copy path list not change path list

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        result = []
        self.traversal(root, [], result)
        return result
    
    def traversal(self, cur: TreeNode, path: List[int], result: List[str]) -> None:
        if not cur:
            return
        path.append(cur.val)
        if not cur.left and not cur.right:
            result.append('->'.join(map(str, path)))
        if cur.left:
            # it makes a copy of the path list, the original list does not change so not need to pop
            self.traversal(cur.left, path[:], result)
        if cur.right:
            self.traversal(cur.right, path[:], result)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        path = ''
        result = []
        if not root: return result
        self.traversal(root, path, result)
        return result
    
    def traversal(self, cur: TreeNode, path: str, result: List[str]) -> None:
        path += str(cur.val)
        # if reach leave append path to result
        if not cur.left and not cur.right:
            result.append(path)

        if cur.left:
            # + '->' hide backtracking
            self.traversal(cur.left, path + '->', result)
        
        if cur.right:
            self.traversal(cur.right, path + '->', result)

# Q3: 404. Sum of Left Leaves: https://leetcode.com/problems/sum-of-left-leaves/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root):
        if root is None:
            return 0
        
        leftValue = 0
        # Check if the left node is a leaf
        if root.left and not root.left.left and not root.left.right:
            leftValue = root.left.val
        else:
            # If it's not a leaf, continue to sum the left leaves in the left subtree
            leftValue = self.sumOfLeftLeaves(root.left)
        
        # Always check the right subtree for left leaves
        rightValue = self.sumOfLeftLeaves(root.right)

        return leftValue + rightValue

# itereation

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root):
        if root is None:
            return 0
        st = [root]
        result = 0
        while st:
            node = st.pop()
            if node.left and node.left.left is None and node.left.right is None:
                result += node.left.val
            if node.right:
                st.append(node.right)
            if node.left:
                st.append(node.left)
        return result

# Q4: 222. Count Complete Tree Nodes https://leetcode.com/problems/count-complete-tree-nodes/description/

# My first answer: main logic use iteration, helper function using recursion

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        stack = [root]
        count = 0
        if not root:
            return count
        
        while stack:
            node = stack.pop()
            if self.leftHeight(node) != self.rightHeight(node):
                stack.append(node.right)
                stack.append(node.left)
                count += 1
            elif self.leftHeight(node) == self.rightHeight(node):
                height = self.leftHeight(node)
                count += 2**height-1

        return count 

    # Calculate left height by traversing left child nodes
    def leftHeight(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        return 1 + self.leftHeight(node.left)
    
    # Calculate right height by traversing right child nodes
    def rightHeight(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        return 1 + self.rightHeight(node.right)
