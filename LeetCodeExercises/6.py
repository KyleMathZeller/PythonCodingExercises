"""
6. Zigzag Conversion
Solved
Medium
Topics
Companies

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);

 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:

Input: s = "A", numRows = 1
Output: "A"

 

Constraints:

    1 <= s.length <= 1000
    s consists of English letters (lower-case and upper-case), ',' and '.'.
    1 <= numRows <= 1000

I could easily modify this code to rather write into a single string rather than numRows => lists. But then we loose the visual effect.
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        #Edgecase Handlers numRows == 0, 1
        if (numRows < 2):
            return s
        #Edgecase Handler numRows == 2
        if (numRows == 2):
            outputString = ""
            for char in s[0:len(s):2]:
                outputString += char
            for char in s[1:len(s):2]:
                outputString += char
            return outputString
        #if numRows > 2
        tempList = []
        outputList = []
        #Dynamic list size creation
        for index in range(0, numRows):
            outputList.append(tempList.copy())
        currentRow = 0
        skipAmount = numRows - 2
        verticleCycle = True
        for index in range(0, len(s)):
            if verticleCycle:
                print(f'currentRow = {currentRow} index = {index} => {s[index]} vertRow? = {verticleCycle}')
                outputList[currentRow].append(s[index])
                currentRow += 1
                #Keeps us cycling in the dynamic row of numbers
                if currentRow % (numRows) == 0:
                    currentRow = len(outputList) - 2
                    verticleCycle = False
            else:
                print(f'currentRow = {currentRow} index = {index} => {s[index]} vertRow? = {verticleCycle}')
                for jindex in range(0, numRows):
                    if jindex != currentRow:
                        outputList[jindex].append(" ")
                    else:
                        outputList[currentRow].append(s[index])
                currentRow -= 1
                if currentRow == 0:
                    verticleCycle = True
        #For printing lists for debugging and astheitcs~
        #for lists in outputList:
        #    print(lists)
        outputstring = ""
        for index in range(0, numRows):
            for value in outputList[index]:
                if value.isalpha() or value == ',' or value == '.':
                    outputstring += value
        return outputstring