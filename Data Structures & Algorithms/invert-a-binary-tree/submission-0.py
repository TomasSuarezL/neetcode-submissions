# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        nodes = [root]
        while nodes:
            node = nodes.pop()
            print(node)
            if node.left:
                left = node.left
                nodes.append(left)
            else:
                left = None
            if node.right:
                right = node.right
                nodes.append(right)
            else:
                right = None

            node.right = left
            node.left = right        
            print("node: ", node.val, " left:", node.left.val if node.left else None, " right:", node.right.val if node.right else None)
    
        return root


