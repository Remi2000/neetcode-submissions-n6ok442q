# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 时间	O(n)	每个节点恰好访问一次，执行一次交换操作，n 为节点总数
        # 空间	O(h)	递归调用栈深度 = 树高 h；平衡树 h = log n，退化为链表时 h = n
        # 基准情况：空节点直接返回
        if not root:
            return None

        # 交换当前节点的左右子树
        root.left, root.right = root.right, root.left

        # 递归翻转左子树
        self.invertTree(root.left)
        # 递归翻转右子树
        self.invertTree(root.right)

        return root