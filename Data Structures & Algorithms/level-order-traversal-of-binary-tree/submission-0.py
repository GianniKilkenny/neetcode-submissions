# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.res = []
        if not root:
            return self.res
        else:
            self.res.append([root.val])
        def bfs(root):
            queue = []
            queue.append(root)
            while queue:
                n = len(queue)
                for i in range(n):
                    node = queue.pop(0)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                node_vals_per_level = []
                for v in range(len(queue)):
                    val = queue[v].val
                    node_vals_per_level.append(val)
                if node_vals_per_level:
                    self.res.append(node_vals_per_level)

        bfs(root)
        return self.res