class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = len(nums)
        if l < 2:
            return nums.index(target) if l == 1 and nums[0] == target else -1
        pl = 0
        pr = l - 1

        while pl <= pr:
            pm = pl + (pr - pl) // 2
            if nums[pm] == target:
                return pm
            elif nums[pm] >= nums[pl]:
                if target < nums[pm] and target >= nums[pl]:
                    pr = pm - 1
                else:
                    pl = pm + 1
            elif nums[pm] <= nums[pl]:
                if target > nums[pm] and target <= nums[pr]:
                    pl = pm + 1
                else:
                    pr = pm - 1
        return -1

