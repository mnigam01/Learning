class Node:
    def __init__(self):
        self.children = defaultdict(list)
        self.word = False

class WordDictionary:

    def __init__(self):
        self.head = Node()
        

    def addWord(self, word: str) -> None:
        prv = self.head
        for c in word:
            if c not in prv.children:
                prv.children[c] = Node()
            prv = prv.children[c]
        prv.word = True

        

    def search(self, word: str) -> bool:

        def helper(i = 0, prv = self.head):
            if i==len(word):
                return prv.word
            if word[i]!='.' and word[i] not in prv.children:
                return False
            elif word[i]!='.':
                return helper(i+1, prv.children[word[i]])
            for c in prv.children:
                if helper(i+1, prv.children[c]):
                    return True
            return False

        return helper()

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)


def search(self, word: str) -> bool:

    def dfs(i=0,node=self.head):

        if i==len(word):
            return node.word
        if word[i]=='.':
            for v in node.children:
                if dfs(i+1,node.children[v]):
                    return True
        elif word[i] in node.children:
            return dfs(i+1, node.children[word[i]])
    
        return False
    return dfs()