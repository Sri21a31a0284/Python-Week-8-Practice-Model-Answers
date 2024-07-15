# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # store the range sum
        range_sum = 0

        # perform inorder traversal
        def inorder(node, low, high):
            nonlocal range_sum

            if not node:
                return 0

            inorder(node.left, low, high)
            val = node.val
            if low <= val <= high:
                range_sum += val
            inorder(node.right, low, high)
        
        inorder(root, low, high)

        return range_sum
