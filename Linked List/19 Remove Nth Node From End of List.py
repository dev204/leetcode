'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

'''

# create two pointers l and r, one starts before head second starts at head
# Step 1: Move r ahead by n steps, This creates a gap of n nodes between l and r.
# Step 2: Move both l and r until r hits the end
# So now, when r reaches the end, l will be just before the node to be removed
# then we can simple remove the node and return

# tc O(n) sc O(1)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        l = dummy
        r = head

        for i in range(n):
            r = r.next

        while r:
            r = r.next
            l = l.next

        l.next = l.next.next
        return dummy.next