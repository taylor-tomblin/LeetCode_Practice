"""
1. Two Sum
(Easy)

Given an array of integers nums and an integer target, return indicies of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
    Input: nums = [3,2,4], target = 6
    Output: [1,2]

Example 3:
    Input: nums = [3,3], target = 6
    Output: [0,1]

Constraints:
    - 2 <= nums.length <= 10^4
    - -10^9 <= nums[i] <= 10^9
    - -10^9 <= target <= 10^9
    - Only one valid answer exists.

Follow-up: Can you come up with an algorithm that is less than O(n^2) time complexity?
"""

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Create a dictionary to store the indices of the numbers
        num_dict = {}
        
        # Iterate through the list of numbers
        for i, num in enumerate(nums):
            complement = target - num
            # Check if the complement is in the dictionary
            if complement in num_dict:
                # If it is, return the indices of the two numbers
                return [num_dict[complement], i]
            # Otherwise, add the current number and its index to the dictionary
            num_dict[num] = i
        
        # If no solution is found, return an empty list (though the problem guarantees one solution)
        return []
    
# Example usage
solution = Solution()

print(solution.twoSum([2, 7, 11, 15], 9))
print(solution.twoSum([3, 2, 4], 6))
print(solution.twoSum([3, 3], 6))