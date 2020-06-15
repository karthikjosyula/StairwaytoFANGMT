def nextPermutation(nums):
    l = len(nums)
    ind=-1
    if l < 2:
        return nums
    elif len(nums) ==2:
        nums[0],nums[1] = nums[1],nums[0]
        return nums
    else:
        if nums[l-1] > nums[l-2]:
            nums[l-1],nums[l-2] = nums[l-2],nums[l-1]
            return nums
        else:
            base = nums[l-1]
            for i in range(l-2,-1,-1):
                if base > nums[i]:
                    ind = i
                    break
                else:
                    base = nums[i]
            if ind > -1:
                for j in range(l-1, ind, -1):
                    if nums[ind] < nums[j]:
                        nums[ind], nums[j] = nums[j], nums[ind]
                        break
    k = ind+1
    #temp = nums[k]
    p=0
    for i in range(k,l):
        if(k<l-1-p):
            temp = nums[k]
            nums[k] = nums[l-1-p]
            nums[l-1-p] = temp
            p+=1
            k+=1
    return nums

print(nextPermutation([3,2,1]))
--5,3,3,3,6,7,8,9,9




