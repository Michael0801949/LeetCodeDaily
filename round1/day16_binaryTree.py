# Q1 654. Maximum Binary Tree: https://leetcode.com/problems/maximum-binary-tree/description/

# recursion almost same as https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        
        # find the max var in current input array, assign as parent
        root_val = max(nums)
        root = TreeNode(root_val)
        
        # find the index of max val
        idx = nums.index(root_val)

        # remove the max val from input, continue recurssion to left part and right part of the array, build left and rightsub tree
        root.left = self.constructMaximumBinaryTree(nums[:idx])
        root.right = self.constructMaximumBinaryTree(nums[idx+1:]) 
        
        return root    

# Q2  617. Merge Two Binary Trees: https://leetcode.com/problems/merge-two-binary-trees/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        if not root2:
            return root1
        root_val = root1.val + root2.val

        root = TreeNode(root_val)

        root.left = self.mergeTrees(root1.left, root2.left)
        root.right = self.mergeTrees(root1.right, root2.right)
        return root

# Q3 98. Validate Binary Search Tree: https://leetcode.com/problems/validate-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        # set the smallest val as maxVar, so that we will replace it in the following code operation when it backtrace from leaf to root
        self.maxVar = float('-inf')

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        # Order left->parent->right: only in this order we should always get a node.val > maxVar it is a binary search tree
        # recursion on the left node, assume my code opreation on the level resolve current level 
        left = self.isValidBST(root.left)
        # my current level opreation: update the maxVar if root.val > max, else return False
        if root.val > self.maxVar:
            self.maxVar = root.val
        else:
            return False
        # recursion on the right node, assume my code opreation on the level resolve current level 
        right = self.isValidBST(root.right)

        # return value to the current level
        return left and right  