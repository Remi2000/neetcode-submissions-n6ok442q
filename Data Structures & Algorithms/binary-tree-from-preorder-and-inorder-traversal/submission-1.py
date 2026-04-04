# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val: i for i, val in enumerate(inorder)}
        self.pre_nxt_idx = 0

        def build(in_left, in_right):
            if in_left > in_right:
                return None

            root_val = preorder[self.pre_nxt_idx]
            self.pre_nxt_idx += 1
            root = TreeNode(root_val)

            mid = inorder_map[root_val]

            root.left = build(in_left, mid - 1)
            root.right = build(mid + 1, in_right)

            return root
        
        return build(0, len(inorder) - 1)