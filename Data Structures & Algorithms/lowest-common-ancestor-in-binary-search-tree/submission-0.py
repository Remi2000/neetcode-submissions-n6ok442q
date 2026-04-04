# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # 时间	O(h)	只沿一条路径往下走，h 为树高；平衡时 O(log n)，退化时 O(n)
        # 空间	O(h)	递归栈深度 = 路径长度；改用迭代写法可以做到 O(1)
        if not root:
            return None

        # 都在左子树
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)

        # 都在右子树
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

        # 分叉了（一左一右，或其中一个就是 root）→ 当前就是答案
        return root