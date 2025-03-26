'''
Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.

Input: head = [0,1,2,3]
Output: [3,2,1,0]

'''

# add prev pointer , which points to null initially
# traverse and keep updating head, prev
# return prev

# tc O(n) sc O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def reverseLinkedList(head):
    prev = None
    curr = head

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev