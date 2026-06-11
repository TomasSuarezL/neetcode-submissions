# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def checkSubtree(node: Optional[TreeNode], subRoot: Optional[TreeNode]):
            sub_nodes = [(node, subRoot)]
            while sub_nodes:
                p, q = sub_nodes.pop()
                if not p and q or p and not q or p.val != q.val:
                    return False
                if q.left or p.left:
                    sub_nodes.append((p.left, q.left))                
                if q.right or p.right:    
                    sub_nodes.append((p.right, q.right))
            return True    

        if not root:
            return True

        nodes = [root]
        while nodes:
            node = nodes.pop()
            if not node:
                continue
            if checkSubtree(node, subRoot):
                return True
            nodes.append(node.right)
            nodes.append(node.left)                
        return False


