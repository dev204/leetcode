'''
You are given a string s consisting of only uppercase english characters and an integer k.
You can choose up to k characters of the string and replace them with any other uppercase English character.

After performing at most k replacements,
return the length of the longest substring which contains only one distinct character.

Input: s = "AAABABB", k = 1
Output: 5

'''

# we traverse the input string and calc freq of each char, at the same time we keep count of maxFreq noticed so far
# maxf: the frequency of the most frequent character in the current window

# Use a sliding window and expand it as long as it's valid.
# Window is valid if: (window length) - (max frequency of a char in window) ≤ k
# Because this gives you the number of replacements needed to make the whole window the same character.

# idea here is to make sure (len of sliding window - frequency of max occuring character) is always <= k
# If number of characters to replace > k, window is invalid
# So shrink it from the left (l += 1) until it becomes valid again

# ONLY if asked - When we shrink the window, shouldn’t we also update maxf? Since we're removing characters, isn't maxf potentially outdated?
# even if maxf is technically no longer accurate (due to shrinking), the worst that happens is:
# The window becomes slightly smaller than it could be
# But the next time we expand the window, maxf will be recalculated only if a new larger value appears, which is fine
# This doesn’t affect correctness, and it avoids recalculating maxf on every shrink


def characterReplacement(self, s: str, k: int) -> int:
    count = {}  # hashmap to maintain freq
    res = 0
    # idea is to make sure len of window - frequency of max occuring character is always <= k
    l = 0
    maxfreq = 0
    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)
        maxfreq = max(maxfreq, count[s[r]])

        while (r - l + 1) - maxfreq > k:  # notice here we don't need to decrement maxfreq as we move l fwd
            # reason for this bcus our answer (len of window) - maxfreq <= k will not change even if we reduce maxfreq
            count[s[l]] -= 1
            l += 1

        res = max(res, r - l + 1)

    return res