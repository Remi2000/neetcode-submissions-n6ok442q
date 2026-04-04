# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def valid(node, left, right):
            # base case：空节点自然是合法的
            if not node:
                return True

            # 当前节点必须在 (left, right) 区间内
            # 注意要严格小于和大于（BST 不允许重复值）
            if not (node.val > left and node.val < right):
                return False

            # 递归检查左右子树
            # 左子树：最大上界变成当前节点的值
            # 右子树：最小下界变成当前节点的值
            return valid(node.left, left, node.val) and valid(node.right, node.val, right)

        return valid(root, float('-inf'), float('inf'))