# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        depth = 1
        nodes = {depth: [root], 2:[]}
        next_depth = True
        while next_depth:
            for node in nodes[depth]:            
                new_depth = depth + 1
                # nodes[new_depth] = nodes[new_depth] if nodes.get(new_depth) else []
                if node.left:
                    nodes[new_depth].append(node.left)
                if node.right:
                    nodes[new_depth].append(node.right)
                    
            if nodes.get(new_depth):
                depth = new_depth
                nodes[depth+1] = []
            else:
                next_depth = False
        return depth





