def solution(input):
    # Code goes here
    a =0
    sum = []

    if len(input)==0:
        return 0
    else:
        a += solution(input)
        input.pop(0)
        sum.append(a)
        return sum
print(solution([1,4,5,3,2,4,5,6,1]))

#assert solution([1,1,1]) == [1,2,3]
#assert solution([1,-1,3]) == [1,0,3]
