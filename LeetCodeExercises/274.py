"""
Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.

According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.

 

Example 1:

Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.

Example 2:

Input: citations = [1,3,1]
Output: 1

 

Constraints:

    n == citations.length
    1 <= n <= 5000
    0 <= citations[i] <= 1000


"""
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        arraySize = len(citations)
        valueDictionary = {}
        #the H value will never be higher than the amount of papers published or average
        if max(citations) > len(citations):
            maxHValue = len(citations)
        else:
            maxHValue = max(citations)
        #Create a dictionary of possible H values
        print(maxHValue)
        for i in range(0, maxHValue + 1):
            valueDictionary.update({i: 0})
        for value in citations:
            startValue = maxHValue
            while (startValue > 0):
                if value >= startValue:
                   valueDictionary.update({startValue: valueDictionary.get(startValue) + 1})
                startValue -= 1
        print(valueDictionary)
        for entry in reversed(valueDictionary):
            if entry <= valueDictionary.get(entry):
                return entry
            print(entry)
        