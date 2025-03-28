'''
A prefix tree (also known as a trie) is a tree data structure used to efficiently store and retrieve keys in a set of strings.
Some applications of this data structure include auto-complete and spell checker systems.
'''

# A Trie is structured as a tree-like data structure where each node contains a hash map (or an array for fixed character sets)
# to store references to its child nodes, which represent characters.
# Each node also includes a boolean flag to indicate whether the current node marks the end of a valid word

class TrieNode:

    def __init__(self):
        self.children = {}
        self.endOfWord = False
'''
Time complexity: 
O(n) for each function call.
Space complexity: 
O(t)
Where n is the length of the string and t is the total number of TrieNodes created in the Trie
'''
class Trie:

    def __init__(self):
        self.root = TrieNode()

    '''
    To insert a word, we iterate through the characters of the word with index i, 
    starting at the root of the Trie as the current node. If the current node already contains word[i], 
    we continue to the next character and move to the node that word[i] points to. 
    If word[i] is not present, we create a new node for word[i] and continue the process until we reach the end of the word. 
    We mark the boolean variable as true as it is the end of the inserted word.
    '''

    def insert(self, word: str) -> None:
        cur = self.root

        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.endOfWord = True
    '''
    Searching for a word is similar to inserting, but instead of creating new nodes, 
    we return false if we don't find a character in the path while iterating or if the end-of-word marker is 
    not set to true when we reach the end of the word'''
    def search(self, word: str) -> bool:
        cur = self.root

        for char in word:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for char in prefix:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)