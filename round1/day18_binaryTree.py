# Q1 530. Minimum Absolute Difference in BST: https://leetcode.com/problems/minimum-absolute-difference-in-bst/description/
'''
order left -> parent -> right  makes sure visit the node in a sorted order
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # initialize variable
    def __init__(self):
        self.pre = None
        self.result = 10**5
    

    def traversal(self, curr: Optional[TreeNode]):
        if not curr:
            return
        # left recurssion
        self.traversal(curr.left)
        # current level logic: check whether new diff < previous diff, move pre pointer to curr pointer place
        if self.pre is not None:
            self.result = min(self.result, abs(self.pre.val - curr.val))
        self.pre = curr
        # right recurssion
        self.traversal(curr.right)

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        self.traversal(root)
        return self.result

# Q2 501. Find Mode in Binary Search Tree: https://leetcode.com/problems/find-mode-in-binary-search-tree/

# utilize character of BST
'''
Similar to Q1, BST values are in ascending order when we use in-order traversal
use 2 pointer to munipulate count and max count to find result in one traversal
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result = []
        # previous value pointer, point to the previous node of curr pointer
        self.pre = None
        self.count = 0
        self.max_count = 0

    def traversal(self,curr):
        # base case logic
        if not curr:
            return
        # recursion on the left subtree
        self.traversal(curr.left)
        # current layer logic: update count, pre pointer, max_count
        if self.pre is None or self.pre.val != curr.val:
            self.count = 1
        else:
            self.count += 1
        self.pre = curr
        if self.count == self.max_count:
            self.result.append(curr.val)
        elif self.count > self.max_count:
            self.result = [curr.val]
            # no need to update max_count untill there is one value > 0 (initial vlaue of max_count)
            self.max_count = self.count
        # recurssion on the right sub tree
        self.traversal(curr.right)


    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.traversal(root)

        return self.result

# Q3 236. Lowest Common Ancestor of a Binary Tree: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if root == q or root == p or root is None:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left is not None and right is not None:
            return root

        if left is None and right is not None:
            return right
        elif left is not None and right is None:
            return left
        else: 
            return None
        
# simplified recursion
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Base case: If we reach a null node, return None
        # If we find either p or q, return root (this can be part of the LCA)
        if root == q or root == p or root is None:
            return root
        
        # Search left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # If both left and right are non-null, root is the LCA
        if left and right:
            return root
        
        # Otherwise, return either the left or right subtree that is non-null
        return left if left else right
