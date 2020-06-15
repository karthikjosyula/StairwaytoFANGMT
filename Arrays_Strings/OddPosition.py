def solution(input):
    #code goes here
    l = len(input)
    a =[]
    for i in range(0,l):
        if i%2==1:
            a.append(input[i])            
    return a

print(solution([1,-1,2,-2]))
#assert solution([0,1,2,3,4,5]) == [1,3,5]
#assert solution([1,-1,2,-2]) == [-1,-2]
