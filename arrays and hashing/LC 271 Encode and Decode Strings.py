'''
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.
implement encode and decode

Input: ["neet","code","love","you"]

Output:["neet","code","love","you"]
'''
# TC O(n)
# If the total number of characters in the list of strings is n, The output string res will take O(n) space
# The extra characters (lengths and #) are small compared to n and still grow linearly → so total space is O(n)

class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        ans = []
        for s in strs:
            ans.append(str(len(s)) + '#' + s)
        return("".join(ans))

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        ans = []
        i=0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            word_len=int(s[i:j])
            ans.append(s[j+1:j+1+word_len])
            i = j + 1 + word_len
        return(ans)


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))