# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class NodeWrapper:
    def __init__(self, node):
        self.node = node
    
    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        dummy = ListNode()
        curr = dummy
        
        # don't scan all heads every time (this is k)
        # instead, why not just use a minHeap for this?
        minHeap = []

        for lst in lists:
            if lst:
                heapq.heappush(minHeap, NodeWrapper(lst))

        while minHeap:
            node_wrapper = heapq.heappop(minHeap)
            curr.next = node_wrapper.node
            curr = curr.next

            if node_wrapper.node.next:
                heapq.heappush(minHeap, NodeWrapper(node_wrapper.node.next))

        return dummy.next