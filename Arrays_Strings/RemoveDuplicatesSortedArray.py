class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        [0,0,1,1,1,2,2,3,3,4]
        """
        l=len(nums)
        j=0
        duphash = {}
        for i in range(0,l-1):
            if(nums[i]!=nums[i+1]):
                duphash[nums[i]] = i
                duphash[nums[i+1]] = i+1
                #nums[i], nums[i+1] = nums[i+1], nums[i]

                j+=1
        nums = [nums[k] for k in duphash.values()]
        print(duphash)
        print(nums)
        return j
