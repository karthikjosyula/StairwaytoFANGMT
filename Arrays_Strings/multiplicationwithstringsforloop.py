def multiply(num1, num2):
    l1 = len(num1)
    l2 = len(num2)
    product = 0
    for i in range(0,l2):
        a = int(num2[i])
        tenpower1 = pow(10,(l2-1-i))
        sp = 0
        for j in range(0,l1):
            b = int(num1[j])
            tenpower2 = pow(10,(l1-1-j))
            sp += a*b*tenpower2
        product += sp*tenpower1
    return str(product)


print(multiply("19","20"))


