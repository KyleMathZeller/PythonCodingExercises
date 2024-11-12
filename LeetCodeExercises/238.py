"""
238. Product of Array Except Self
Solved
Medium
Topics
Companies
Hint

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

 

Constraints:

    2 <= nums.length <= 105
    -30 <= nums[i] <= 30
    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        productLeft = [1] * len(nums)
        productRight = [1] *len(nums)
        outputResults = [1] *len(nums)
        #Left side fill we can skip arr[0] will always be 'null' I use 1 to prevent math errors
        for index in range (1, len(nums)):
            productLeft[index] = productLeft[index - 1] * nums[index - 1]
        #Right side fill we can skip arr[0] will always be 'null' I use 1 to prevent math errors
        for index in range(len(nums) - 2, -1, -1):
            productRight[index] = productRight[index + 1] * nums[index + 1]
        #Left * Right = final product
        for index in range(0, len(nums)):
            outputResults[index] = productLeft[index] * productRight[index]
        return outputResults