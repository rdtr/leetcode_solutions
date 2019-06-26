class LRUCache:

    def __init__(self, capacity: int):
        self.head = None
        self.tail = None
        self.map = {}
        self.cur = 0
        self.cap = capacity

    def get(self, key: int) -> int:
        res = self._get(key)
        if res is None:
            return -1
        else:
            return res.val

    def put(self, key: int, value: int) -> None:
        res = self._get(key)
        if res is not None:
            res.val = value
            return

        node = LRUNode(key, value)
        self.map[key] = node

        if self.head is None:
            self.head = node
            self.tail = node
            self.cur = 1
            return

        self.head.prev = node
        node.next = self.head
        self.head = node

        if self.cur < self.cap:
            self.cur += 1
        else:
            tail = self.tail
            prev = tail.prev
            prev.next = None
            self.tail = prev
            del self.map[tail.key]

    def _get(self, key):
        if key not in self.map:
            return None

        node = self.map[key]
        if self.head == node:
            return node
        if self.tail == node:
            prev = self.tail.prev
            self.tail = prev
            prev.next = None
            node.prev = None

            node.next = self.head
            self.head.prev = node
            self.head = node
            return node

        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

        self.head.prev = node
        node.next = self.head
        self.head = node
        return node


class LRUNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)