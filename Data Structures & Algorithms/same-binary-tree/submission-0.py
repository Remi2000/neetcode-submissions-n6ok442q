# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # 时间	O(min(m,n))	最多比较两棵树中较小那棵的所有节点，遇到不同立即停止
        # 空间	O(min(h1,h2))	递归栈深度 = 较矮那棵树的高度；平衡时 O(log n)，退化时 O(n)
        
        # 情况 1：都空 → 相同
        if not p and not q:
            return True

        # 情况 2 和 3：一空一不空 → 不同
        # 走到这里说明不是"都空"，所以只要有一个空就是不对称
        if not p or not q:
            return False

        # 情况 4：都有值 → 先比值，再比子树
        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)