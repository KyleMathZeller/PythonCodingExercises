"""
68. Text Justification
Solved
Hard
Topics
Companies

Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

Note:

    A word is defined as a character sequence consisting of non-space characters only.
    Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
    The input array words contains at least one word.

 

Example 1:

Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]

Example 2:

Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
Note that the second line is also left-justified because it contains only one word.

Example 3:

Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]

 

Constraints:

    1 <= words.length <= 300
    1 <= words[i].length <= 20
    words[i] consists of only English letters and symbols.
    1 <= maxWidth <= 100
    words[i].length <= maxWidth

I do not like my solution to this problem...but it does work. :(
"""

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        tempString = ""
        wordCount = 0
        outputList = []
        tempRow = []
        rowInfo = []
        for index in range(0, len(words)):
            print(f'tempString len => {len(tempString)} index =>{words[index]} wordC =>{wordCount}')
            if (maxWidth ==  len(words[index]) and wordCount == 0):
                tempRow.append(len(words[index]))
                rowInfo.append(tempRow.copy())
                tempRow.clear()
                outputList.append(str(words[index]))
                print("1 hit")
            elif(len(tempString) < maxWidth - len(words[index]) - wordCount):
                tempRow.append(len(words[index]))
                tempString += words[index] 
                wordCount += 1
                print("2 hit")
            elif(len(tempString) + wordCount + len(words[index]) == maxWidth):
                tempRow.append(len(words[index]))
                tempString += words[index]
                wordCount = 0
                outputList.append(str(tempString))
                rowInfo.append(tempRow.copy())
                tempRow.clear()
                tempString = ""
                print("3 hit")
            else:
                wordCount = 0
                outputList.append(str(tempString))
                rowInfo.append(tempRow.copy())
                tempRow.clear()
                tempString = ""
                print("else hit")
                if (len(words[index]) < maxWidth):
                    tempRow.append(len(words[index]))
                    tempString = words[index] 
                    wordCount += 1
                else:
                    tempRow.append(len(words[index]))
                    tempString = words[index]
        if (tempString != ""):
            outputList.append(tempString)
            rowInfo.append(tempRow)
        for index, string in enumerate(outputList):
            characterSum = sum(rowInfo[index])
            spacesNeeded = maxWidth - characterSum
            breaksInWords = len(rowInfo[index]) - 1
            oneWord = False
            if (breaksInWords != 0):
                averageSpaceSize = spacesNeeded // breaksInWords
                extraSpaces = spacesNeeded % breaksInWords
            else:
                oneWord = True
            if oneWord == True:
                outputList[index] = outputList[index] + (" ") * spacesNeeded
            else:
                stringPosition = 0
            if (index != len(outputList) - 1):
                for j in range(0, len(rowInfo[index]) - 1):
                    #print(f"outputList = {outputList[index]} rowInfo[j] = {rowInfo[index][j]}")
                    #print(f"averageSpaceSize = {averageSpaceSize}, extraSpaces = {extraSpaces}")
                    stringPosition += rowInfo[index][j]
                    outputList[index] = outputList[index][:stringPosition] + (" ") * (averageSpaceSize) + outputList[index][stringPosition:]
                    stringPosition += averageSpaceSize
                    if extraSpaces > 0:
                        outputList[index] = outputList[index][:stringPosition] + (" ") + outputList[index][stringPosition:]
                        stringPosition += 1
                        extraSpaces -= 1
        if(len(rowInfo[-1]) > 1):
            stringPosition = rowInfo[-1][0]
        else:
            stringPosition = len(rowInfo[-1])
        for j in range(0, len(rowInfo[-1]) - 1):
            if len(rowInfo[-1]) > 1:
                outputList[-1] = outputList[-1][:stringPosition] + (" ") + outputList[-1][stringPosition:]
                #print(f"{rowInfo[-1][j]}")
                stringPosition += rowInfo[-1][j + 1] + 1
        while len(outputList[-1]) < maxWidth:
            outputList[-1] += " "
        return outputList
