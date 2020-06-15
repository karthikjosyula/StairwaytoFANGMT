from typing import List, Tuple
class Solution:
    def twoSum(self, nums: List[int], target: int) -> Tuple[int, int]:
        for i in range(len(nums)):
            if (target - nums[i]) in nums[i+1:]:
                return i, nums.index(target - nums[i], i + 1)
