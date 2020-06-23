class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 1 if len(nums) == 1 else None
        i = 1
        n = 1
        temp = nums[0]
        for j in range(1, len(nums)):
            if nums[j] != temp:
                temp = nums[j]
                nums[i] = nums[j]
                i += 1
        return i

