# Q1 513. Find Bottom Left Tree Value: https://leetcode.com/problems/find-bottom-left-tree-value/description/

# recurssion:
'''
I first thought I need to some how firgure a condition to identify the most left value in the last level of the tree
There is no specific condition for a most left node in fact. 
This is how the answer achieve：
1. work on left node first, if find a leaf node, record the level, check whether it is the deepest value, if yes use as result record level as maxLevel
2. if not a leave node, go to the next level, if find a new leaf node compare the level with maxLevel, if > maxlevel, sub current result with it
3. work on the right node after left node, repeat the same logic
4. because we work on left node first, if there is a leaf node on the same level, the leaf on the left will be recorded, and will not be sub by node on the same level
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.max_depth = float('-inf')
        self.result = 0
        self.traversal(root, 0)
        return self.result
    
    def traversal(self, node: Optional[TreeNode], depth: int):
        # condition pushing the final answer to the previous level
        if not node.left and not node.right and depth > self.max_depth:
            self.max_depth = depth
            self.result = node.val
            return
        if node.left:
            depth += 1 # current level logic: deepth += 1 for the next level
            self.traversal(node.left, depth) # recurssion 
            depth -= 1 # current level logic: backtrack to the previous level after the next level return
        if node.right:
            depth += 1 # current level logic: deepth += 1 for the next level
            self.traversal(node.right, depth) # recurssion 
            depth -= 1 # current level logic: backtrack to the previous level after the next level return

# recurssion simplified version:

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        self.max_depth = float('-inf')
        self.result = None
        self.traversal(root, 0)
        return self.result
    
    def traversal(self, node, depth):
        if not node.left and not node.right:
            if depth > self.max_depth:
                self.max_depth = depth
                self.result = node.val
            return
        
        if node.left:
            self.traversal(node.left, depth+1) # use depth + 1 as param, it does not change depth in the current level
        if node.right:
            self.traversal(node.right, depth+1) # use depth + 1 as param, it does not change depth in the current level

# iteration:
'''
it utilize level iteration:
For range in each level:
result is assign to the first val(left-est val)
until it reach the last node in the tree
in this way the result var will be the first(left-est) var in the last level
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque()
        q.appendleft(root)
        result = int
        while q:
            size = len(q)
            for i in range(size):
                node = q.pop()
                if i == 0:
                    result = node.val
                if node.left:
                    q.appendleft(node.left)
                if node.right:
                    q.appendleft(node.right)
        return result               
            
# Q2 112. Path Sum: https://leetcode.com/problems/path-sum/description/

# recurssion: 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        return self.traversal(root, 0 + root.val, targetSum)

    def traversal(self, node: Optional[TreeNode], total: int, targetSum: int):

        if total == targetSum and not node.left and not node.right: # stop case 1: valid path
            return True
        if not node.left and not node.right: # stop case 2: not a valid path
            return False
        if node.left and self.traversal(node.left, total + node.left.val, targetSum): # layer logic for left
            return True # return True to the previous layer if find a valid path
        if node.right and self.traversal(node.right, total + node.right.val, targetSum):# layer logic on the right
            return True # return True to the previous layer if find a valid path
        return False # no valid path find after recurssion

# recursive simplified:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        
        result = []
        self.traversal(root, targetSum, [], result)
        return result
    def traversal(self,node, count, path, result):
            if not node:
                return
            path.append(node.val)
            count -= node.val
            if not node.left and not node.right and count == 0:
                result.append(list(path))
            self.traversal(node.left, count, path, result)
            self.traversal(node.right, count, path, result)
            path.pop()
#itereation 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        # node, node.val per
        st = [(root, root.val)]
        while st:
            node, path_sum = st.pop()
            # if meet condition return true
            if not node.left and not node.right and path_sum == sum:
                return True
            # if right or left, record the node and the sum in the path
            if node.right:
                st.append((node.right, path_sum + node.right.val))
            if node.left:
                st.append((node.left, path_sum + node.left.val))
        return False
    
# Q3: 106. Construct Binary Tree from Inorder and Postorder Traversal: https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/
'''
inorder: left, parent(mid), right
postorder: left, right, parent(mid)
1. Find the parent node value from post order, it is always at the end of the array
2. Find the index of the parent node value, use it to slice the inorder array, define left and right
3. Because both post order and inorder are for the same tree, use the len(inorder_left) and len(inorder_right)
to slice the post order array
4. recursivly work on the left sub tree and right sub tree, append to parent node left and right
5. return parent node
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None
        root_val = postorder[-1]
        root = TreeNode(root_val)
        
        # Find index with root node var
        idx = inorder.index(root_val)
        
        # Slice inorder array to left and right sub array
        inorder_left = inorder[:idx]
        inorder_right = inorder[idx + 1:]
        
        # Slice postorder array to left and right sub array
        postorder_left = postorder[:len(inorder_left)]
        postorder_right = postorder[len(inorder_left): len(postorder) - 1]
        
        # recursively work on right and left sub array to build on the right and left sub tree
        root.left = self.buildTree(inorder_left, postorder_left)
        root.right = self.buildTree(inorder_right, postorder_right)

        return root
