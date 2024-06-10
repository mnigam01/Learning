class DLL:
    def __init__(self, key=None, val=None, prv=None, next=None):
        self.key = key
        self.val = val
        self.prv = prv
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.current = 0
        self.d = {}
        self.head = DLL()
        self.tail = DLL()
        self.head.next = self.tail
        self.tail.prv = self.head
        

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1
        node = self.d[key]
        self.remove_from_pos(node)
        self.add_to_head(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            node = self.d[key]
            node.val = value
            self.remove_from_pos(node)
            self.add_to_head(node)
        else:
            while self.current>=self.capacity:
                self.remove_from_tail()
                self.current-=1
            
            node = DLL(key=key,val=value)
            self.d[key] = node
            self.add_to_head(node)
            self.current+=1


    def add_to_head(self,node):
        tmp = self.head.next
        self.head.next = node
        node.prv = self.head
        node.next = tmp
        tmp.prv = node

    def remove_from_pos(self,node):
        node.prv.next = node.next
        node.next.prv = node.prv

    def remove_from_tail(self):
        if self.current==0:
            return
        node = self.tail.prv
        del self.d[node.key]
        self.remove_from_pos(node)

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)