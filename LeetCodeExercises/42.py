"""
Description
Accepted
Accepted
Editorial
Editorial
Solutions
Solutions
Submissions
Submissions
Code
Testcase
Testcase
Test Result
42. Trapping Rain Water
Hard
Topics
Companies

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9

 

Constraints:

    n == height.length
    1 <= n <= 2 * 104
    0 <= height[i] <= 105


"""
waterStored = 0
maxPeakLoc = 0
for index in range(0, len(height)):
    if height[index] > height[maxPeak]:
        maxPeak = index

highestPeakSeen = 0
for index in range(0, maxPeak):
    if (height[index] > highestPeakSeen):
        highestPeakSeen = height[index]
    if(height[index] < highestPeakSeen):
        waterStored += (highestPeakSeen - height[index])

highestPeakSeen = 0
for index in range(len(height) - 1, maxPeak, -1):
    if (height[index] > highestPeakSeen):
        highestPeakSeen = height[index]
    if(height[index] < highestPeakSeen):
        waterStored += (highestPeakSeen - height[index])

return waterStored