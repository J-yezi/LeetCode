#coding=utf-8

class DLinkedNode(): 
    def __init__(self):
        self.key = 0
        self.value = 0
        self.prev = None
        self.next = None

class LRUCache(object):
    def __init__(self, capacity):
        self.cache = {}
        self.capacity = capacity
        self.size = 0
        self.head = DLinkedNode()
        self.tail = DLinkedNode()

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        node = self.cache.get(key)
        if not node:
            return -1

        self.__move_to_head__(node)
        return node.value

    def put(self, key, value):
        node = self.cache.get(key)
        if not node:
            newNode = DLinkedNode()
            newNode.key = key
            newNode.value = value

            self.cache[key] = newNode
            self.__add_node__(newNode)

            self.size += 1
            if self.size > self.capacity:
            tail = self.__pop_tail__()
            del self.cache[tail.key]
            self.size -= 1
        else:
            node.value = value
            self.__move_to_head__(node)

    def __add_node__(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    
    def __remove_node__(self, node):
        prev = node.prev
        new = node.next
        prev.next = new
        new.prev = prev
    
    def __move_to_head__(self, node):
        self.__remove_node__(node)
        self.__add_node__(node)

    def __pop_tail__(self):
        res = self.tail.prev
        self.__remove_node__(res)
        return res

if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put(2, 1)
    cache.put(1, 1)
    cache.put(2, 3)
    cache.put(4, 1)
    print(cache.get(1))
    print(cache.get(2))