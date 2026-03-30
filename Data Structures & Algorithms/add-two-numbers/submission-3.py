# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy

        carry = 0

        while l1 or l2 or carry:
            # Get values from current nodes
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # calculate sum and carry
            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10

            # create this node with the digit we have
            current.next = ListNode(digit)
            current = current.next

            # move to the next nodes if they exist
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next