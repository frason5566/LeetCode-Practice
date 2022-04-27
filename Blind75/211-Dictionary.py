class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
            
        current.isWord = True

    def search(self, word: str) -> bool:
        def find (current,i=0):
            if i == len(word):
                return current.isWord
            if word[i] == '.':
                return any(find(x,i+1) for x in current.children.values())
            if word[i] in current.children:
                return find(current.children[word[i]], i+1)
            return False

        return find(word)


def main():

    obj = WordDictionary()
    obj.insert("apple")
    print(obj.search("apple"))
    print(obj.search("app"))
    obj.insert("app")
    print(obj.search("app"))

main()