# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # D 1 2 3 4 5
        #   5 4 3 2 1
        # we need dummy node to handle deletion of the first node
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next
        
        # delete
        test = left.next
        del test
        left.next = left.next.next

        return dummy.next