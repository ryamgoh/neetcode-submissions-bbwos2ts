# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        while curr:
            minNode = -1
            for i in range(len(lists)):
                if not lists[i]:
                    continue  # empty list
                if minNode == -1 or lists[minNode].val > lists[i].val:
                    minNode = i
                
            if minNode == -1:
                break

            curr.next = lists[minNode]
            lists[minNode] = lists[minNode].next
            curr = curr.next

        return dummy.next