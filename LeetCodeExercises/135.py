"""
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

    Each child must have at least one candy.
    Children with a higher rating get more candies than their neighbors.

Return the minimum number of candies you need to have to distribute the candies to the children.

 

Example 1:

Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.

Example 2:

Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.

 

Constraints:

    n == ratings.length
    1 <= n <= 2 * 104
    0 <= ratings[i] <= 2 * 104

The logic for this was a tad convaluted to me so I was commenting it out as I went and then revised it at the end so I could easily follow it if I need ever review it
"""
class Solution:
    def candy(self, ratings: List[int]) -> int:
        #List to hold value of candy of children respective to the rating list ratings[n] == childCandyCount[n]
        childCandyCount = []
        #Catch cases for strange inputs
        if len(ratings) == 0:
            return 0
        elif len(ratings) == 1:
            return 1
        #Children get at minimum 1 piece so this needs to start somewhere
        childCandyCount.append(1)
        previousChildCandy = 1
        #List sweeps left to rigth one way to enforce rules
        for i in range(1, len(ratings)):
            #if current child has a higher rating than the child to the left get they get previousCandy + 1
            if (ratings[i] > ratings[i-1]):
                previousChildCandy += 1
                childCandyCount.append(previousChildCandy)
            #if current child has equal or lesser rating then previous child they get 1 candy    
            else:
                previousChildCandy = 1
                childCandyCount.append(previousChildCandy)
        #List sweeps from right to left to enforce rules on outliers
        for i in range(len(ratings) - 2, -1, -1):
            #if current child has higher rating than child to the right they should have more candy than them
            if (ratings[i] > ratings[i+1]):
                #check to see if child has less or equal candy to lower rated right neighbor
                if (childCandyCount[i] <= childCandyCount[i+1]):
                    #Rules violated, therefore update values to acceptable minimum
                    childCandyCount[i] = childCandyCount[i+1] + 1
        return (sum(childCandyCount))