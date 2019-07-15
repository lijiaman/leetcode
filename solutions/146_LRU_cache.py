# 1. Using OrderedDict
from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.data = collections.OrderedDict()
        self.remain = capacity

    def get(self, key: int) -> int:
        if key not in self.data:
            return -1
        v = self.data.pop(key)
        self.data[key] = v
        return v

    def put(self, key: int, value: int) -> None:
        if key in self.data:
            self.data.pop(key)
        else:
            if self.remain > 0:
                self.remain -= 1
            else:
                self.data.popitem(last=False)
        self.data[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# 2. Using Double-linked List
class DoubleNode:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.data_dict = {}
        self.capacity = capacity
        self.head = DoubleNode()
        self.tail = DoubleNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.data_dict:
            node = self.data_dict[key]
            node.prev.next = node.next
            node.next.prev = node.prev
            self.data_dict.pop(key)

            self.data_dict[key] = DoubleNode(key, node.val)
            self.data_dict[key].next = self.head.next
            self.data_dict[key].prev = self.head
            self.head.next.prev = self.data_dict[key]
            self.head.next = self.data_dict[key]

            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # Delete from double linked list
        if key in self.data_dict:
            node = self.data_dict[key]
            node.prev.next = node.next
            node.next.prev = node.prev
            self.data_dict.pop(key)
        else:
            if self.capacity > 0:
                self.capacity -= 1
            else:
                del_node = self.tail.prev
                self.tail.prev.prev.next = self.tail
                self.tail.prev = self.tail.prev.prev
                self.data_dict.pop(del_node.key)

        self.data_dict[key] = DoubleNode(key, value)
        self.data_dict[key].next = self.head.next
        self.data_dict[key].prev = self.head
        self.head.next.prev = self.data_dict[key]
        self.head.next = self.data_dict[key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)