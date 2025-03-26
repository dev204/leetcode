'''
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.
'''

# we can use doubly linked list with a hashmap, hashmap to store key-val pairs and DLL to keep track of LRUs as doubly
# can achieve O(1) tc, sc O(n)
# we can create leftnode and rightnode between which we can insert all incoming nodes that will make our life easier
# # leftnode, n1,n2,n3,n4 , rightnode where n1 is lru, n4 is most recently used


class Node:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None


# leftnode, n1,n2,n3,n4 , rightnode
# n1 is lru, n4 is most recently used
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}

        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def removeNode(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    # add node to end of the list
    def addNode(self, node):
        p, n = self.right.prev, self.right
        p.next = node
        node.prev = p
        node.next = n
        n.prev = node

    def get(self, key: int) -> int:
        if key in self.map:
            self.removeNode(self.map[key])
            self.addNode(self.map[key])
            return self.map[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.removeNode(self.map[key])  # need to remove as it's going to be inserted as most recently used
        node = Node(key, value)
        self.map[key] = node
        self.addNode(node)

        if len(self.map) > self.capacity:
            del self.map[self.left.next.key]
            self.removeNode(self.left.next)