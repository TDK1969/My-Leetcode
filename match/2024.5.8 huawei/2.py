class Node:
    def __init__(self, pre: "Node", nxt: "Node", key: int, value: int) -> None:
        self.pre = pre
        self.nxt = nxt
        self.key = key
        self.value = value

class LRU:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.len = 0
        self.head = Node(None, None, -1, -1)
        self.tail = Node(None, None, -1, -1)
        self.head.nxt = self.tail
        self.tail.pre = self.head
        self.d = {}
    
    def read(self, key: int):
        if key in self.d:
            key_node = self.d[key]
            key_node.pre.nxt = key_node.nxt
            key_node.nxt.pre = key_node.pre
            key_node.pre = self.head
            key_node.nxt = self.head.nxt
            self.head.nxt.pre = key_node
            self.head.nxt = key_node
    
    def write(self, key: int, value: int):
        if key in self.d:
            key_node = self.d[key]
            key_node.pre.nxt = key_node.nxt
            key_node.nxt.pre = key_node.pre
            key_node.pre = self.head
            key_node.nxt = self.head.nxt
            self.head.nxt.pre = key_node
            self.head.nxt = key_node
            key_node.value = value
            return
    
        if self.len == self.capacity:
            # 弹出链表尾
            tmp = self.tail.pre
            tmp.pre.nxt = self.tail
            self.tail.pre = tmp.pre
            self.d.pop(tmp.key)
            self.len -= 1
        
        # 插入新元素
        tmp = Node(self.head, self.head.nxt, key, value)
        self.d[key] = tmp
        self.head.nxt.pre = tmp
        self.head.nxt = tmp
        self.len += 1
    
    def query(self, key: int) -> int:
        if key in self.d:
            return self.d[key].value
        else:
            return -1


lru = LRU(3)
lru.write(3, 5)
lru.write(1, 2)
lru.write(1, 3)
lru.write(2, 4)
lru.write(5, 4)
lru.read(5)
lru.write(6, 1)
print(lru.query(1))
