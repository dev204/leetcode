'''
You are given two non-empty linked lists, l1 and l2, where each represents a non-negative integer.

The digits are stored in reverse order, e.g. the number 123 is represented as 3 -> 2 -> 1 -> in the linked list.

Each of the nodes contains a single digit. You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Return the sum of the two numbers as a linked list.
Input: l1 = [1,2,3], l2 = [4,5,6]

Output: [5,7,9]

Explanation: 321 + 654 = 975.

'''

# tc O(n+m) sc O(1)

def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = cur = ListNode()
    carry = 0
    s = 0
    while l1 or l2 or carry:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0

        s = v1 + v2 + carry
        carry = s // 10
        s = s % 10

        n = ListNode(s, None)
        cur.next = n
        cur = cur.next

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return dummy.next