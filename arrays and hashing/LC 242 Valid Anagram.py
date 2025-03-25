'''
Description
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Input: s = "racecar", t = "carrace"

Output: true

'''
from collections import Counter

def isAnagram(s: str, t: str) -> bool:
    s = Counter(s)
    t = Counter(s)
    return s == t

isAnagram("asd","")