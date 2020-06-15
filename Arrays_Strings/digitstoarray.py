def solution(input):
    # Code goes here
    strinput = str(input)
    l = len(strinput)
    a=[]
    for i in range(0,l):
       a.append(int(strinput[i]))
    return a
print(solution(1200012))

#assert solution(123) == [1,2,3]
#assert solution(400) == [4,0,0]
