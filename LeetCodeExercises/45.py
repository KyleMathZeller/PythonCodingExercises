"""
45. Jump Game II
Solved
Medium
Topics
Companies

You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

    0 <= j <= nums[i] and
    i + j < n

Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:

Input: nums = [2,3,0,1,4]
Output: 2

 

Constraints:

    1 <= nums.length <= 104
    0 <= nums[i] <= 1000
    It's guaranteed that you can reach nums[n - 1].

"""
class Solution:
    def jump(self, nums: List[int]) -> int:
        #if input is small don't bother with everything else
        if(len(nums) <= 1):
            return 0
        currentPosition = 0
        currentJumpMax = nums[0]
        nextJumpPos = 0
        jumpCount = 0
        #I used a while loop because I don't want to iterate through values my for loop inside the while loop invalidates as bad jumps
        while currentPosition != len(nums):
            #if we can jump to the end DO THAT, jump once return the value
            if(currentJumpMax >= len(nums) - currentPosition - 1):
                jumpCount += 1
                return jumpCount
            #did not want to bother
            count = 0
            #print(f"We are at position [{currentPosition}], we can jump up to {currentJumpMax}")
            nextBiggestJump = 0
            #I ran into the problem of next jump value != to the value of jumping somewhere and needed this additonal variable or to retool my code
            nextBiggestJumpValue = 0
            for index in range(currentPosition + 1, currentPosition + currentJumpMax + 1):
                print(f"checking [{index}]")
                #count is added because a jump of 2 versus a jump of 2 one place father down the array is actually worth +1 more distance
                if (nextBiggestJumpValue < nums[index] + count):
                    nextBiggestJump = nums[index]
                    nextBiggestJumpValue = nums[index] + count
                    print(f"we changed our biggestJump to {nextBiggestJump}")
                    nextJumpPos = index
                count += 1
            currentJumpMax = nextBiggestJump
            currentPosition = nextJumpPos
            #print(f"Jumped to [{currentPosition}] and can now jump [{currentJumpMax}]")
            jumpCount += 1
        