class ListNode:
    def __init__(self, key=0, val=0, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:
    def printList(self, text:str):
        print("print")
        curr = self.list_start.next
        s = "list:" + text + " "
        while curr:
            s += str(curr.key) + ":" + str(curr.val) + " "
            curr = curr.next
        print(s)

    def removeKey(self, key: int):
        # print("   ", "remove", key)
        if key in self.cache:
            removal = self.cache[key]
            removal.prev.next = removal.next
            removal.next.prev = removal.prev
            del self.cache[key]
            self.size -= 1
    
    def addKey(self, key: int, val: int):
        # print("   ", "add", key)
        node = ListNode(key, val)
        self.cache[key] = node
        prev, nxt = self.list_end.prev, self.list_end
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev
        self.size += 1

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.list_start = ListNode(0, 0)
        self.list_end = ListNode(0, 0)
        self.list_start.next = self.list_end
        self.list_end.prev = self.list_start
        self.size = 0

    def get(self, key: int) -> int:
        # print("get", key)
        if key in self.cache:
            tmpval = self.cache[key].val
            self.removeKey(key)
            self.addKey(key, tmpval)
            # print("get-found", key, tmpval)
            return tmpval
        # print("get-not-found", key, str(-1))
        return -1

    def put(self, key: int, value: int) -> None:
        # print("put", key)
        self.printList("put")
        if key in self.cache:
            self.removeKey(key)
        if self.size == self.capacity:
            self.removeKey(self.list_start.next.key) # remove least recently used 
        self.addKey(key, value)

