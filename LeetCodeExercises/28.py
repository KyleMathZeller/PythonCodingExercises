"""
28. Find the Index of the First Occurrence in a String
Solved
Easy
Topics
Companies

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.

 

Constraints:

    1 <= haystack.length, needle.length <= 104
    haystack and needle consist of only lowercase English characters.


"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        firstOccurrence = -1
        traversalRange = len(haystack) - len(needle)
        print(traversalRange)
        #Exception handler for empty needle
        if (traversalRange == 0):
            if needle == haystack:
                return 0
        #Exception handler for needle len == 1 and optimization
        if (len(needle) == 1):
            for index in range(0, traversalRange + 1):
                if (haystack[index] == needle[0]):
                    firstOccurrence = index
                    return firstOccurrence
        #Logic for needle > 1
        for index in range(0, traversalRange + 1):
            if (haystack[index] == needle[0]):
                firstOccurrence = index
                for charLoc in range(1, len(needle)):
                    if (haystack[index + charLoc] != needle[charLoc]):
                        firstOccurrence = -1
                        break
                    elif (charLoc == len(needle) - 1):
                        return firstOccurrence
        return firstOccurrence
    
    """
    Learned woops could have just used the index method! Here's an optimized redo below
    """
    
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        try:
            return haystack.index(needle)
        except Exception:
            print(f'No occurrence of substring {needle} found.')
        return -1