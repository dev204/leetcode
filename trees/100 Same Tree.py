'''
Given the roots of two binary trees p and q, return true if the trees are equivalent, otherwise return false.

Two binary trees are considered equivalent if they share the exact same structure and the nodes have the same values.
Input: p = [1,2,3], q = [1,2,3]
Output: true
'''

# tc O(n)n is the total number of nodes in both trees (assuming both trees have the same structure and number of nodes)
# sc O(n) if the tree is skewed (like a linked list)

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        else:
            return False