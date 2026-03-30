class Node:
    """
    Double Linked List Node
    """
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    """
    LRU Cache that uses a HashMap + our double linked List

    get(key): O(1)
    put(key, value): O(1)
    space complexity should be as big as capacity so O(N)
    """

    def __init__(self, capacity: int):
       self.capacity = capacity
       self.cache = {} # key -> node

       # dummy nodes for Head (MRU) and Tail (LRU) to avoid edge cases 
       self.head = Node()
       self.tail = Node()
       self.head.next = self.tail
       self.tail.prev = self.head

    def get(self, key: int) -> int:
        """Return the value if exist, else -1
        """
        if key not in self.cache:
            return -1

        # Get the nod eand move from its poisition in the linked list to the front
        # so essentially a remove and a add operation? (O(1))
        node = self.cache[key]
        self._remove(node)
        self._add(node)
        return node.value
        

    def put(self, key: int, value: int) -> None:
        """Add or update key-value pair"""
        if key in self.cache:
            self._remove(self.cache[key])
        
        # create new node
        node = Node(key, value)
        self.cache[key] = node
        self._add(node)

        # overcapacity logic
        if len(self.cache) > self.capacity:
            # pop out the LRU
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]

    def _add(self, node):
        """Add node right atter the head"""

        # For connecting ht enode to head and head's next (shoving in between two nodes, where left node is the HEAD)
        node.prev = self.head
        node.next = self.head.next

        # update surrounding nodes
        self.head.next.prev = node
        self.head.next = node


    def _remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev




