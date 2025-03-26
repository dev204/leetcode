'''
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
'''

# TC O(n+m) Where m is the number of strings and n is the length of the longest string.
# SC O(m)

def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    anagramMap = collections.defaultdict(list)

    for word in strs:
        chars = [0] * 26
        for char in word:
            pos = ord(char.lower()) - ord('a')
            chars[pos] += 1
        anagramMap[tuple(chars)].append(word)
    return list(anagramMap.values())