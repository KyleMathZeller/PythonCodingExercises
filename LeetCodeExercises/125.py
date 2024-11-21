"""
125. Valid Palindrome
Solved
Easy
Topics
Companies

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

 

Constraints:

    1 <= s.length <= 2 * 105
    s consists only of printable ASCII characters.


"""

#This code is intentionally not particularly pythonic. It is exercises labelled under 2-pointers which python does not have pointers...
#So in the spirit of the code I tried to take a more pointer link approach.
def isLetterorNum(c: chr) -> bool:
    if c.isalpha():
        return True
    if c.isnumeric():
        return True
    return False

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i = 0
        j = len(s) - 1
        while (i < j):
            if (isLetterorNum(s[i]) and isLetterorNum(s[j])):
                if(s[i] == s[j]):
                    i += 1
                    j -= 1
                else:
                    return False
            if(not isLetterorNum(s[i])):
                i += 1
            if(not isLetterorNum(s[j])):
                j -= 1
        return True