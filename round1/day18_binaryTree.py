#Q1: 235. Lowest Common Ancestor of a Binary Search Tree: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
'''
the key is understanding: if a node.val is between p.val and q.val, 
then the node is the Lowest Common Ancestor
'''
# Recurssion:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if not root:
            return root
        ceil = max(p.val,q.val)
        floor = min(p.val,q.val)

        if root.val <= ceil and root.val >= floor:
            return root
        elif root.val > ceil:
                    return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < floor:
                    return self.lowestCommonAncestor(root.right, p, q)

#Q2: 701. Insert into a Binary Search Tree: https://leetcode.com/problems/insert-into-a-binary-search-tree/description/
'''
add to any node is OK, so we just need find a leaf place:
if node < parent check node.left to find leaf
if node > parent check node.right to find leaf
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.parent = None

    def traversal(self, cur, val):
        if cur is None:
            node = TreeNode(val)
            if val > self.parent.val:
                self.parent.right = node
            else:
                self.parent.left = node
            return

        self.parent = cur
        if cur.val > val:
            self.traversal(cur.left, val)
        if cur.val < val:
            self.traversal(cur.right, val)

    def insertIntoBST(self, root, val):
        self.parent = TreeNode(0)
        if root is None:
            return TreeNode(val)
        self.traversal(root, val)
        return root

# simplified recurssion
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)
        return root

# Q3 450. Delete Node in a BST: https://leetcode.com/problems/delete-node-in-a-bst/description/

'''
if the node has both left and right subtree need to move the left subtree to the very 
left of right subtree. 
'''
# Recurssion
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # end conditions, if node is null, if node has one child, if node has both child
        if not root:
            return root
        if root.val == key and root.left and not root.right:
            return root.left
        elif root.val == key and root.right and not root.left:
            return root.right
        elif root.val == key and root.right and root.left:
            curr = root.right
            while curr.left:
                curr = curr.left
            curr.left = root.left
            return root.right
        elif root.val == key and not root.right and not root.left:
            return None
        
        # current level logic is hiden here: "root.left =", "root.right =". The do recursion
        root.left = self.deleteNode(root.left, key)
        root.right = self.deleteNode(root.right, key)

        # return to current level
        return root
    
# simplified recurssion:
class Solution:
    def deleteNode(self, root, key):
        if root is None:
            return root
        if root.val == key: 
            if root.right is None:  # if right is None just return left
                return root.left
            cur = root.right
            while cur.left:  # if right is not None, then this will only be executed if left is also not None
                cur = cur.left
            # exchange the value of the node to delete and the value of root, int this way it also form a valid BST instead of deletion, and the leaf node (match val) will be remove in the next level 
            root.val, cur.val = cur.val, root.val
        root.left = self.deleteNode(root.left, key) 
        root.right = self.deleteNode(root.right, key)
        return root