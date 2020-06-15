def centered_average(nums):
  l=len(nums)
  for i in range(0,l-1):
    minindex = i
    for j in range(i+1, l):
      if(nums[j]<nums[minindex]):
        minindex = j
    if minindex!=i:
      nums[i], nums[minindex] = nums[minindex],nums[i]
  nums = nums[1:l-1]
  l=len(nums)
  return 0 if len(nums)==0 else (centeraverage2(nums)/l)

def centeraverage2(nums):
  if len(nums) == 0:
    return 0
  else:
    sum = nums[0]
    nums.pop(0)
    return sum + centeraverage2(nums)

print(centered_average([11,12,13,14,13,22,110,11,34,15,46]))
