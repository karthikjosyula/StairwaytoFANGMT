s = "{}{}{}{}{}[][][][()()()]({[]})"
list = []
j = 0
for i in s:
    if i in ["(", "{", "["]:
        list.append(i)
    else:
        if list and ((list[-1] == "(" and i == ")") or (list[-1] == "[" and i == "]") or (list[-1] == "{" and i == "}")):
            list.pop()
        else:
            j += 1
if list:
    j+=1
print(True if j == 0 else False)
