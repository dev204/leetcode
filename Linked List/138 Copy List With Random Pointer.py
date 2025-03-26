'''
You are given the head of a linked list of length n. Unlike a singly linked list, each node contains an additional pointer random, which may point to any node in the list, or null.

Create a deep copy of the list.

The deep copy should consist of exactly n new nodes, each including:

The original value val of the copied node
A next pointer to the new node corresponding to the next pointer of the original node
A random pointer to the new node corresponding to the random pointer of the original node
Note: None of the pointers in the new list should point to nodes in the original list.

Return the head of the copied linked list.

In the examples, the linked list is represented as a list of n nodes. Each node is represented as a pair of [val, random_index] where random_index is the index of the node (0-indexed) that the random pointer points to, or null if it does not point to any node.

Input: head = [[3,null],[7,3],[4,0],[5,1]]

Output: [[3,null],[7,3],[4,0],[5,1]]

'''

# we do a single pass and create new nodes (copy of original nodes) and also use a hashmap to map oldNode -> newNode
# then we traverse original again, with the idea safe that we have all nodes available to be linked together
# in this traversal we fetch new node corresponding to the old node using the hashmap and link everything together

# tc O(n) sc O(n) for creating new copy
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cur = head
        m = {None:None} # this is imp to have none to none mapping
        while cur:
            copy = Node(cur.val)
            m[cur] = copy
            cur = cur.next
        cur = head
        while cur:
            copy = m[cur]
            copy.next = m[cur.next]
            copy.random = m[cur.random]
            cur = cur.next
            copy = copy.next
        return m[head] # we return mapping of head