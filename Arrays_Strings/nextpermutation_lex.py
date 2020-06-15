def nextPermutation(nums):
    l = len(nums)
    if l < 2:
        return nums
    elif len(nums) ==2:
        nums[0],nums[1] = nums[1],nums[0]
        return nums
    else:
        if nums[l-1] > nums[l-2]:
            nums[l-1],nums[l-2] = nums[l-2],nums[l-1]
        else:
            return getswitchindices(nums)

def getswitchindices(nums):
    l = len(nums)
    ind = 0
    base = nums[l-1]
    for i in range(l-2,-1,-1):
        if base > nums[i]:
            ind = i
            break
        else:
            base = nums[i]
    for j in range(l-1,ind,-1):
        if nums[ind] < nums[j]:
            nums[ind],nums[j] = nums[j], nums[ind]
            break
    #print(ind+1)
    #print(nums)
    #print(sortnum(nums[ind+1:]))
    #print(nums[:ind+1])
    return sortnum(nums) if ind==0 else  nums[:ind+1] + sortnum(nums[ind+1:])


def sortnum(s):
    if(len(s)<2):
        return s
    else:
        pivot = s[0]
        lessarray = [i for i in s[1:] if i <=pivot]
        greatarray = [i for i in s[1:] if i > pivot]
        return sortnum(lessarray) +  [pivot] + sortnum(greatarray)

print(nextPermutation([9,8,7,5,6,4,3,2]))




