def multiply(num1, num2):
    idigits = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    cdigits = {val:key for key,val in idigits.items()}
    def atoi(num1):
        prod = 0
        for i in num1:
            prod = prod*10 + idigits[i]
        return prod


    return atoi(num1) * atoi(num2)
print(multiply("19","20"))


