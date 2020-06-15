def solution(input):
    # Code goes here
    l = len(input)
    sum = []
    a=0
    for i in range(0,l):
        a +=input[i]
        sum.append(a)
    return sum
print(solution([1,4,5,3,2,4,5,6,1]))

#assert solution([1,1,1]) == [1,2,3]
#assert solution([1,-1,3]) == [1,0,3]
