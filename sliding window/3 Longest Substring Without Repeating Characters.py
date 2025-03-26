'''
Given a string s, find the length of the longest substring without duplicate characters.

A substring is a contiguous sequence of characters within a string.

Input: s = "zxyzxyz"
Output: 3
'''

# we can use a hashset to keep track of chars
# use 2 pointers l,r and keep moving r fwd until chars are unique
# at first instance of duplicate chars, we move l fwd while removing char[l] from set
# sort of like sliding window
# tc O(n) where n is len of string and sc O(m) where m is total num of unique chars in s

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0

        l = 0
        longest = 1
        seen = set()

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            longest = max(longest,r-l+1)
            r += 1
        return longest