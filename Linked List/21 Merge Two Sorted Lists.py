'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted linked list and return the head of the new sorted linked list.

The new list should be made up of nodes from list1 and list2.
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
'''
# take head and prehead, keep pointing head to smaller value
# return prehead.next
# O(n+m) tc, sc = O(1) Where n n is the length of l i s t 1 list1 and m m is the length of l i s t 2 list2

def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    prehead = head = ListNode()

    if not list1:
        return list2
    if not list2:
        return list1
    while list1 and list2:
        if list1.val <= list2.val:
            head.next = list1
            list1 = list1.next
        else:
            head.next = list2
            list2 = list2.next
        head = head.next
    if list1: head.next = list1
    if list2: head.next = list2
    return prehead.next