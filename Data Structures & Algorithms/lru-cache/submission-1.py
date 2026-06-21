'''

Goal: make put a O(1) time complexity. So we need a way to search/track the LRU in constant time.

We can use a doubly-linked-list to do so. Keep the LRU always at head, and MRU at tail.

When capacity is reached, and key is new, remove LRU (head) and append new Node to tail.
When capacity is full, but key is old, simply update value of existing Node and shift it to tail.

'''

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity

        self.head = Node(0, 0)
        self.tail = Node(0, 0)
    
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        # if key exists, return the value from node, and shift node to tail
        # if key doesn't exist, return -1
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # if key exists
            # update node value, then remove node + insert node
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.remove(node)
            self.insert(node)

        # key doesnt exist
            # if has capacity, create node, then insert node
            # no capacity, create node, remove head, then insert node
        else:
            node = Node(key, value)
            if len(self.cache) >= self.capacity:
                self.remove(self.head.next)
            self.insert(node)
    
    def remove(self, node) -> None:
        # 0 <-> node <-> 0 | 0 <-> 0
        # make node.prev.next point to node.next
        # make node.next.prev point to node.prev
        # remove node.key from cache
        node.prev.next = node.next
        node.next.prev = node.prev
        del self.cache[node.key]
    
    def insert(self, node) -> None:
        # 0 <-> 0 | 0 <-> node <-> 0
        # make node.prev = tail.prev
        # make node.next = tail
        # make tail.prev.next = node
        # make tail.prev = node
        # make an entry into self.cache
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node
        self.cache[node.key] = node




