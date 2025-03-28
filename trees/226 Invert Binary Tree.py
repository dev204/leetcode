'''
You are given the root of a binary tree root. Invert the binary tree and return its root.
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
        4
      /   \
     2     7
    / \   / \
   1   3 6   9

'''
# tc O(n) as we traverse each node exactly once sc O(n) for the recursion stack
class Solution:
    '''
    4left -> 2 (first recursion line 18) -> 1 = swaps 1left and 1right
    back to 2 second recursion line 19
    2right -> 3 = swaps 3left and 3right
    now swap 2l and 2r
    now 4right
    7left = swap 6l,6r
    7right = swap 9l,9r
    now 7 = swap7l,7r
    now back to 4
    swap 4l,4r
    '''
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        self.invertTree(root.left)
        self.invertTree(root.right)
        root.left,root.right = root.right,root.left

        return root