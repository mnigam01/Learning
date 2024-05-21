class Node:
    def __init__(self):
        self.children = dict()
        self.word = False

class Trie:

    def __init__(self):
        self.head = Node()


    def insert(self, word: str) -> None:
        prv = self.head
        for ch in word:
            if ch not in prv.children:
                prv.children[ch] = Node()
            prv = prv.children[ch]
        prv.word = True


        

    def search(self, word: str) -> bool:
        prv = self.head
        for ch in word:
            if ch not in prv.children:
                return False
            prv = prv.children[ch]
        return prv.word
        
        

    def startsWith(self, prefix: str) -> bool:
        prv = self.head
        for ch in prefix:
            if ch not in prv.children:
                return False
            prv = prv.children[ch]
        return True

        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)