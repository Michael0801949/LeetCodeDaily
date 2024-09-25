# Q1 Binary Tree Preorder Traversal: https://leetcode.com/problems/binary-tree-preorder-traversal/description/
'''
Root → Left → Right
'''
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        r = []
        def dfs(node):
            if node is None:
                return
            r.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
      
        return r
      
# do not define dfs
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        r = []
        if root is None:
            return r  # Return an empty list instead of None 
        # Add the root's value
        r.append(root.val)   
        # Recursively traverse the left subtree and append the result
        r += self.preorderTraversal(root.left)      
        # Recursively traverse the right subtree and append the result
        r += self.preorderTraversal(root.right)
    
        return r
      
# Q2 94. Binary Tree Inorder Traversal: https://leetcode.com/problems/binary-tree-inorder-traversal/description/
'''
Left → Root → Right
'''
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        r = []
        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            r.append(node.val)
            dfs(node.right)
        dfs(root)
      
        return r
      
# do not define dfs
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        r = []
        if root is None:
            return r  # Return an empty list instead of None
        # Recursively traverse the left subtree and append the result
        r += self.inorderTraversal(root.left) 
        # Add the root's value
        r.append(root.val)        
        # Recursively traverse the right subtree and append the result
        r += self.inorderTraversal(root.right)
    
        return r

#Q3 145. Binary Tree Postorder Traversal https://leetcode.com/problems/binary-tree-postorder-traversal/description/
'''
Left → Right → Root
'''
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        r = []
        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            dfs(node.right)
            r.append(node.val)
        dfs(root)
      
        return r
      
# do not define dfs
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        r = []
        if root is None:
            return r  # Return an empty list instead of None
        # Recursively traverse the left subtree and append the result
        r += self.postorderTraversal(root.left) 
        # Recursively traverse the right subtree and append the result
        r += self.postorderTraversal(root.right)
        # Add the root's value
        r.append(root.val) 
    
        return r
