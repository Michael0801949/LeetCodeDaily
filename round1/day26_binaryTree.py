# Q1 669. Trim a Binary Search Tree: https://leetcode.com/problems/trim-a-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        # base case 1: if it works on a node is null return null
        if not root:
            return root
        # base case 2: continue work on the right subtree and remove left sub tree if find root.val < low
        if root.val < low:
            return self.trimBST(root.right, low, high)
        # base case 3: continue work on the left subtree and remove right sub tree if find root.val > high
        if root.val > high:
            return self.trimBST(root.left, low, high)
        
        # current level right will take the node tree return fron recursion on right, same for left
        root.right = self.trimBST(root.right, low, high) 
        root.left = self.trimBST(root.left, low, high)

        return root

# Q2 108. Convert Sorted Array to Binary Search Tree： https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/

# recursion 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traversal(self, left, right, nums):
        # base case logic
        if left > right:
            return None
        # current level logic: find the mid point, make it a node
        n = left+(right-left)//2
        node = TreeNode(nums[n])
        # current level logic: node left/right = previous level return (recursion)
        node.left = self.traversal(left, left + (right-left)//2 - 1, nums)
        node.right = self.traversal(left + (right-left)//2 + 1, right, nums)
        
        # Not return to previous level until all recurssions are done
        return node

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.traversal(0, len(nums) - 1, nums)

# simplified recurssion

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # base case logic 1 
        if not nums:
            return
        # base case logic 2: when there is only one value, imporve performance
        if len(nums) == 1:
            return TreeNode(nums[0])
        
        # current level logic: find the mid point, make it a node
        mid = (len(nums) - 1)//2
        node = TreeNode(nums[mid])
        # current level logic: node left/right = previous level return (recursion)
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid + 1:])
        
        # Not return to previous level until all recurssions are done
        return node 


# Q3 538. Convert BST to Greater Tree: https://leetcode.com/problems/convert-bst-to-greater-tree/description/

# recurssion
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.pre = None
    
    def traversal(self, curr):
        if not curr:
            return
        # start from right first, to accumulate as move from right to left
        self.traversal(curr.right)      
        if self.pre is not None:
            curr.val += self.pre.val
        self.pre = curr
        self.traversal(curr.left)     

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.traversal(root)
        return root
# recurssion v2: set pre as int, initialize in covertBST method
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.pre = 0 
        self.traversal(root)
        return root
    def traversal(self, cur):
        if cur is None:
            return        
        self.traversal(cur.right)
        cur.val += self.pre
        self.pre = cur.val
        self.traversal(cur.left)