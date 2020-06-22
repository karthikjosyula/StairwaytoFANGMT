def QS_DnC(s):
    if len(s) < 2:
        return s
    else:
        pivot = s[0]
        lesserarray = [i for i in s[1:] if i <= pivot]
        greaterarray = [i for i in s[1:] if i > pivot]
        return QS_DnC(lesserarray) + [pivot] + QS_DnC(greaterarray)

print(QS_DnC([1,0,0,43,65,12,18,5,2,100,50,45,21,78,43,11,31,19,29,0,533]))
