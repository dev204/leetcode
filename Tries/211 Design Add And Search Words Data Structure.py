'''
Design a data structure that supports adding new words and searching for existing words.

Implement the WordDictionary class:

void addWord(word) Adds word to the data structure.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.

'''

# We can use a Trie to implement adding and searching for words efficiently.
# when searching for a word containing '.' Instead of directly matching, we consider all possible characters at the position of '.' and recursively check the rest of the word for each possibility
# We traverse the word with index i, starting at the root of the Trie. For normal characters, we search as usual. When encountering a dot ('.'), we try all possible characters by recursively extending the search in each direction. If any path leads to a valid word, we return true; otherwise, we return false.
# Time complexity: O ( n ) O(n) for addWord(), O ( n ) O(n) for search().
# Space complexity: O(t+n) Where n is the length of the string and t is the total number of TrieNodes created in the Trie.

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root
            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True # found a path that matches
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.endOfWord # for else condition
        return dfs(0,self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)