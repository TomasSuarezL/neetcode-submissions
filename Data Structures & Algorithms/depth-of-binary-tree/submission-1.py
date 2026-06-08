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
        nodes = {depth: [root]}
        next_depth = True
        while next_depth:
            while nodes[depth]:
                node = nodes[depth].pop()            
                new_depth = depth + 1
                if node.left:
                    if nodes.get(new_depth):
                        nodes[new_depth].append(node.left)
                    else:
                        nodes[new_depth] = [node.left]    
                if node.right:
                    if nodes.get(new_depth):
                        nodes[new_depth].append(node.right)
                    else:
                        nodes[new_depth] = [node.right]    
                print(node.val)
            if nodes.get(depth+1):
                depth = depth+1
            else:
                next_depth = False
        return depth





