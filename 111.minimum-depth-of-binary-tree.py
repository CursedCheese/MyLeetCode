#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0
        if root.right is None and root.left is None: return 1
        
        left_depth = self.minDepth(root.left)
        right_depth = self.minDepth(root.right)
        
        if root.left is None:
            return 1 + right_depth
        if root.right is None:
            return 1 + left_depth
        
        return min(left_depth, right_depth) + 1
# @lc code=end

