class ListNode:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.head = ListNode() # most recent
        self.tail = ListNode() # least recent
        self.head.next = self.tail
        self.tail.prev = self.head
        self.key_to_listnode = collections.defaultdict(list)
        self.cap = capacity

    def remove(self, node):
        prev = node.prev
        nex = node.next
        prev.next = nex
        nex.prev = prev
        node.prev = None
        node.next = None
    
    def add_to_head(self, node):
        nex = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = nex
        nex.prev = node

    def get(self, key: int) -> int:
        # use key to find the value
        if key not in self.key_to_listnode:
            return -1
        node = self.key_to_listnode[key]
        self.remove(node) # remove the node from the linkedlist
        self.add_to_head(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        # add and delete with O(1) time complexity
        # linkedlist
        if key in self.key_to_listnode:
            node = self.key_to_listnode[key]
            node.val = value
            self.remove(node)
            self.add_to_head(node)
            return
        if len(self.key_to_listnode) == self.cap:
            node = self.tail.prev
            self.remove(node)
            del self.key_to_listnode[node.key]
        node = ListNode(key=key, val=value)
        self.key_to_listnode[key] = node
        self.add_to_head(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
