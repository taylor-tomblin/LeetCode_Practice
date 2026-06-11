"""
3741. Minimum Distance Between Three Equal Elements II
(Medium)

You are given an integer array nums.

A rouple (i, j, k) of 3 distinct indicies is good if nums[i] = nums[j] = nums[k].

The distance of a good tuple is abs(i - j) + abs(j - k) + abs(k - i), where abs(x) denotes the absolute value of x.

Return an integer denoting the minimum possible distance of a good tuple. If no good tuples exist, return -1.

Example 1:
    Input: nums = [1,2,1,1,3]
    Output: 6
    Explanation: The minimum distance is achieved by the good tuple (0, 2, 3). (0, 2, 3) is a good tuple because nums[0] == nums[2] == nums[3] == 1. Its distance is abs(0 - 2) + abs(2 - 3) + abs(3 - 0) = 6.

Example 2:
    Input: nums = [1,1,2,3,2,1,2]
    Output: 8
    Explanation: The minimum distance is achieved by the good tuple (2, 4, 6). (2, 4, 6) is a good tuple because nums[2] == nums[4] == nums[6] == 2. Its distance is abs(2 - 4) + abs(4 - 6) + abs(6 - 2) = 8.

Example 3:
    Input: nums = [1]
    Output: -1
    Explanation: There are no good tuples. Therefore, the answer is -1.

Constraints:
    - 1 <= n == nums.length <= 10^5
    - 1 <= nums[i] <= n
"""

class Solution(object):
    def minimumDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import defaultdict

        index_map = defaultdict(list)

        for i, num in enumerate(nums):
            index_map[num].append(i)

        min_distance = float('inf')

        for indices in index_map.values():
            if len(indices) >= 3:
                for i in range(len(indices) - 2):
                    distance = abs(indices[i] - indices[i + 1]) + abs(indices[i + 1] - indices[i + 2]) + abs(indices[i + 2] - indices[i])
                    min_distance = min(min_distance, distance)

        return min_distance if min_distance != float('inf') else -1