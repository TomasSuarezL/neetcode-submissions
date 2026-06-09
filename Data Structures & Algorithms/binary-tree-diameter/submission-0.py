# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def getDepth(node: TreeNode):
            depth = 0
            nodes = {depth:[node]}
            while nodes[depth]:
                nodes[depth+1]=[]
                for node in nodes[depth]:
                    if node.left:
                        nodes[depth+1].append(node.left)
                    if node.right:
                        nodes[depth+1].append(node.right)
                depth = depth+1
            return depth
        
        nodes = [root]
        depth=0
        while nodes:
            node = nodes.pop()
            left_depth, right_depth = 0,0
            if node.left:
                nodes.append(node.left)
                left_depth = getDepth(node.left)
            if node.right:
                nodes.append(node.right)
                right_depth = getDepth(node.right)
            total_depth = left_depth + right_depth
            print(total_depth)
            if total_depth > depth:
                depth = total_depth
        return depth