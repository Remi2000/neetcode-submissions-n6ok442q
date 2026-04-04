# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # 时间	O(m × n)	root 的每个节点（m 个）都可能触发一次 isSameTree 比较（最多比 n 个节点）
        # 空间	O(h)	递归栈深度 = root 的树高 h；平衡时 O(log m)，退化时 O(m)
        # root 为空，不可能包含 subRoot
        if not root:
            return False

        # 以当前节点为起点，和 subRoot 完全相同？
        if self.isSameTree(root, subRoot):
            return True

        # 不同的话，去左子树或右子树里继续找
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # 都为空 → 相同
        if not p and not q:
            return True
        # 一个为空一个不为空 → 不同
        if not p or not q:
            return False
        # 值不同 → 不同
        if p.val != q.val:
            return False
        # 递归比较左右子树
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    