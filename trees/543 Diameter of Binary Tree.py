'''
The diameter of a binary tree is defined as the length of the longest path between any two nodes within the tree. The path does not necessarily have to pass through the root.

The length of a path between two nodes in a binary tree is the number of edges between the nodes.

Given the root of a binary tree root, return the diameter of the tree.
Input: root = [1,null,2,3,4,5]
Output: 3

'''

#diameter will be left edge + right edge, and the diameter doesn't necessarily have to go thru root
# we can use DFS (Depth-First Search) to compute the height of the tree from bottom up

# Time: O(n), where n = number of nodes . Every node is visited once
# Space: O(h), where h = height of the tree (due to recursion stack)

def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    self.result = 0

    # nested function returns tree height in dfs way
    def treeHt(root):
        if not root:
            return 0
        left = treeHt(root.left)
        right = treeHt(root.right)
        # diameter will be left edge + right edge
        # so we update the max diameter so far (not max diameter is not necessarily through root)
        self.result = max(self.result, left + right)
        # this will return height
        return 1 + max(left, right)

    treeHt(root)
    return self.result