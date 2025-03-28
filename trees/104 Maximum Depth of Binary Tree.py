'''
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
'''


def maxDepth(self, root: Optional[TreeNode]) -> int:
    # solution 1) recursive DFS
    # Time complexity:O(n)
    # Space complexity: O(h)
    if root is None:
        return 0 # Base case: a None node contributes 0 depth
    ldepth = self.maxDepth(root.left)
    rdepth = self.maxDepth(root.right)

    # Instead of passing depth explicitly, the depth is calculated implicitly by
    # adding 1 at each recursive call
    return max(ldepth, rdepth) + 1


    # solution 2) iterative DFS using stack
    # Time complexity:O(n)
    # Space complexity: O(h)
    stack = []
    stack.append([root,1])
    max_depth = 0

    while stack:
        node,d = stack.pop()
        if node:
            stack.append([node.left,d+1])
            stack.append([node.right,d+1])
            # Nodes in the stack may belong to different levels of the tree,
            # and updating depth globally without tying it to a specific node causes incorrect results

            max_depth = max(max_depth,d)
        #fails if i uncomment below
        #depth = max(depth,d)
    return max_depth


    # solution 3 with bfs and queue
    # level by level traversal
    # Time complexity:O(n)
    # Space complexity: O(h)
    q = deque()
    if root: q.append(root)
    max_depth = 0

    while q:
        for i in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        # we update depth only after popping all elements from current level
        max_depth += 1
    return max_depth