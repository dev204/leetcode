'''
Given a binary tree, determine if it is height-balanced.
'''
# A binary tree is considered height-balanced if:
# For every node, the height difference between the left and right subtree is no more than 1.
# this naturally leads to a recursive (DFS) approach:
# 1) You can check whether subtrees are balanced bottom-up
# 2) At each node, you need two things 1) Is the subtree balanced? 2) What's its height?
# Traverse the tree in post-order (left → right → current).
# For each node: Recursively get the height and balance status of left and right subtrees
# |left_height - right_height| ≤ 1

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# tc O(n) sc O(h)
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [True, 0]

            left, right = dfs(root.left), dfs(root.right)
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]