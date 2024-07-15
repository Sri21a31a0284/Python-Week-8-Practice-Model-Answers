# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        list=[]
        def it(node):
            if node:
                list.append(node.val)
                it(node.left)
                it(node.right)
        it(root)
        list.sort()
        nt=TreeNode()
        pointer=nt
        for item in list:
            inserts=TreeNode(item)
            pointer.right=inserts
            pointer=pointer.right
        return nt.right
