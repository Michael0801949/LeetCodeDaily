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
        
# iterative method：same as iteration order, append to result as we pop node from stack
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root]
        result = []
        if root is None:
            
            return result
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right) # add right node first, when pop right node comes out last
            if node.left:
                stack.append(node.left) # add left node last, when pop left node comes out first

        return result
        
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
# iterative method: different from iteration order, need curr as pointer 
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        result = []
        curr = root
        while curr or stack:
            if curr: # if curr point to a node not None, continue move to the left until pointing to None, meanwhile append all the node to stack
                stack.append(curr)
                curr = curr.left
            # when point to None, go back to the last node (stack.pop()), and try to find right child, 
            # if no right child (curr is None), if will go back to the second last node whith the stack pop one more time etc.
            else: 
                curr = stack.pop()
                result.append(curr.val)
                curr = curr.right
        return result

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
# iterative method: same as the preorder but reverse result and change left and right order
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root]
        result = []
        if root is None:
            
            return result
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.left:
                stack.append(node.left) # left in first, out last
            if node.right:
                stack.append(node.right) # right in last, out first

        return result[::-1] # reverse the list to get the correct order
