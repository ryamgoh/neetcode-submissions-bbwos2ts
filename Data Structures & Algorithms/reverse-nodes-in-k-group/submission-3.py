# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Create a "dummy" node before the head to make things easier
        dummy = ListNode(0, head)
        groupPrev = dummy  # Points to node BEFORE current group
        
        while True:
            # 1. Find the kth node from current position
            kth = self.getKth(groupPrev, k)
            if not kth:
                break  # Not enough nodes left, we're done
            
            # 2. Save what comes after this group
            groupNext = kth.next
            
            # 3. Reverse this group
            prev, curr = groupNext, groupPrev.next
            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            # 4. Connect the reversed group back
            temp = groupPrev.next
            groupPrev.next = kth
            groupPrev = temp
        
        return dummy.next

    def getKth(self, curr, k):
        # Move forward k steps from current node
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr  # Returns the kth node or None if not enough nodes