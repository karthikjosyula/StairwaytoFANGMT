def multiply(num1, num2):
    l1 = len(num1)
    l2 = len(num2)
    sp = 0

    if l2 == 0:
        return 0
    else:
        tenpower = pow(10,(l2-1))
        a = int(num2[0])
        newnum2 = num2[1:]
        temp1 = str(num1)
        for i in range(0,l1):
            sp += a*int(temp1[i])* pow(10,(l1-1-i))
            product = sp*tenpower
        fp = (product+multiply(num1, newnum2))
    return (fp)

print(multiply("19","20"))
print(str(1))

