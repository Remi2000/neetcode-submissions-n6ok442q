# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 时间	O(n)	每个节点恰好访问一次，n 为节点总数
        # 空间	O(h)	递归调用栈深度 = 树高 h；平衡树 h = log n，退化为链表时 h = n
        
        # 基准情况：空节点深度为 0
        if not root:
            return 0

        # 递归求左右子树的最大深度
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        # 当前节点的深度 = 较大的子树深度 + 1（加上自己）
        return max(left_depth, right_depth) + 1