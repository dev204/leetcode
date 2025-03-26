'''
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Input: head = [1,2,3,4]
Output: [1,4,2,3]

'''

# find half way point of the list using slow and fast pointers starting as 0,1 positions resp
# reverse second half, then merge the two lists together

# tc O(n) sc O(1)

def reorderList(self, head: Optional[ListNode]) -> None:
    """
    Do not return anything, modify head in-place instead.
    """
    # find middle
    slow, fast = head, head.next  # note slow and fast start at 0,1 not 0,0
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    # always slow.next is second half of the list, try with [1,2,3,4,5]
    # if we pick one element from each half of the list - slow.next is needed
    # we can't do slow = slow.next as This is slightly problematic because the middle node (2) is skipped when creating the two halves
    second = slow.next  # Start second half from slow.next
    slow.next = None  # Cut the first half of the list

    # reverse second half
    second = self.reverseList(second)

    # merge two lists
    first = head
    '''
    Second Half is Always Shorter or Equal:
When splitting the list, the second half will always have fewer or an equal number of nodes compared to the first half.
For example:
Input [1, 2, 3, 4]: First half [1, 2], Second half [4, 3].
Input [1, 2, 3, 4, 5]: First half [1, 2, 3], Second half [5, 4].

Why Not while first?
The first pointer traverses the nodes from the first half of the list, but we are primarily concerned 
with ensuring all nodes from the second half are merged. 
Once the second half is exhausted, the merging is complete because:
At that point, the first half may have one extra node remaining (if the list length is odd), 
but it will already be in place due to the way the merge interleaves nodes.
    '''
    while second:  # explanation of why while second above
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first, second = tmp1, tmp2


def reverseList(self, head):
    prev = None
    curr = head
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    # imp note return prev
    return prev