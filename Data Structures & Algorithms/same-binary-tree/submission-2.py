# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def checkSameNode(p: Optional[TreeNode], q: Optional[TreeNode]):
            if p.val != q.val:
                return False
            if p.left and not q.left or not p.left and q.left:
                return False
            if p.right and not q.right or not p.right and q.right:
                return False
            if p.left and q.left and p.left.val != q.left.val:
                return False
            if p.right and q.right and p.right.val != q.right.val:
                return False
            return True

        if not p and q or not q and p:
            return False
        if not p and not q:
            return True

        nodes = [(p,q)]
        depth=0
        while nodes:
            x,y = nodes.pop()
            areEqual = checkSameNode(x,y)
            print(x.val, y.val, areEqual)
            if not areEqual:
                return False
            if x.left:
                nodes.append((x.left, y.left))                
            if x.right:
                nodes.append((x.right, y.right))

        return True
            





