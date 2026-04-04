# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # 时间	O(H + k)	H 是树的高度（先走到最左），k 是要访问的节点数
        # 空间	O(H)	栈最多存 H 个节点（树的高度）
        stack = []
        curr = root

        while curr or stack:
            # 一路向左，把左链全部压栈
            while curr:
                stack.append(curr)
                curr = curr.left

            # 弹出栈顶 = 当前最小的未访问节点
            curr = stack.pop()
            k -= 1

            # k 减到 0，说明当前节点就是第 k 小
            if k == 0:
                return curr.val

            # 转向右子树，继续中序遍历
            curr = curr.right