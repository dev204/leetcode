'''
Description
Given a 2-D grid of characters board and a list of strings words, return all words that are present in the grid.

For a word to be present it must be possible to form the word with a path in the board with horizontally or vertically neighboring cells.
The same cell may not be used more than once in a word.
'''


class TrieNode:

    def __init__(self):
        self.children = {}
        self.endOfWord = False

    def addWord(self, word):
        cur = self

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

''' ADDITIONAL Info
We insert all the words into the Trie with their indices marked. Then, we iterate through each cell in the grid. At each cell, we start at the root of the Trie and explore all possible paths. As we traverse, we match characters in the cell with those in the Trie nodes. If we encounter the end of a word, we take the index at that node and add the corresponding word to the result list. Afterward, we unmark that index and continue exploring further paths.


'''
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # inefficient sol will be to search by single word at a time, by running dfs on all the board m*n, and then repeating for all words one by one
        # efficient sol is to run dfs starting from each position single time
        # for every dfs instead of checking for a single word, we can check simultaneously all the words in our list using trie data structure
        # prefix is going to be the current letter on the board

        # step 1 go thru all words and add to prefix tree (trie ds)
        # call dfs for every row and col and pass ""(empty string), and build a word inside "" and every time we add to "" we check in trie if it's end of word
        # this helps as in trie object we already store if one of the word ends at that node

        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()  # res is set to avoid duplicates

        def dfs(r, c, node, word):

            if (r == ROWS or c == COLS or r < 0 or c < 0 or board[r][c] not in node.children or (r, c) in visit):
                return

            visit.add((r, c))
            word += board[r][c]
            node = node.children[board[r][c]]
            if node.endOfWord:
                res.add(word)
            dfs(r + 1, c, node, word)  # call dfs 4 times
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            visit.remove((r, c))

        root = TrieNode()
        for w in words:
            root.addWord(w)

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(res)