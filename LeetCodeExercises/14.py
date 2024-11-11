"""
14. Longest Common Prefix
Solved
Easy
Topics
Companies

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

 

Constraints:

    1 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] consists of only lowercase English letters.


"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key = len)
        maxPrefix = strs[0]
        #print(f"max len = {len(maxPrefix)} of => {maxPrefix}")
        for entry in range(1, len(strs)):
            comparisonString = strs[entry]
            for char in range(0, len(maxPrefix)):
                if (maxPrefix[char] != comparisonString[char]):
                    maxPrefix = maxPrefix[0:char]
                    break
        return maxPrefix