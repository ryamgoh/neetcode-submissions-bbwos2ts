# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 12 + 995 = 1007

        # [2,1] + [5,9,9] = [7,0,0,1]
        # [2,1,0,0] + [5,9,9,0] = [7,0,0,1]

        dummy = ListNode()
        curr = dummy

        carry = 0
        while l1 or l2 or carry:
            
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            the_sum = val1 + val2 + carry

            carry = the_sum // 10
            digit = the_sum % 10

            curr.next = ListNode(digit)
            curr = curr.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next