nums1 = [5,10,20,300,0,0,0,0]
m = 4
nums2 = [1,25,100,150]
n = 4

p1 = m - 1
p2 = n - 1
# set pointer for nums1
p3 = m + n - 1

# while there are still elements to compare
while p1 >= 0 and p2 >= 0:
    if nums1[p1] < nums2[p2]:
        nums1[p3] = nums2[p2]
        p2 -= 1
    else:
        nums1[p3] = nums1[p1]
        p1 -= 1
    p3 -= 1

# add missing elements from nums2
nums1[:p2 + 1] = nums2[:p2 + 1]
print(nums1)
print(nums2)