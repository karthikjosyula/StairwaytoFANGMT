def valideIPAddress(IPString):
    IPdigits = IPString.split('.')
    i=0
    if len(IPdigits) != 4:
        return False
    else:
        for digits in IPdigits:
            if digits.isdigit() and 0<= int(digits) <=255:
                i+=0
            else:
                i=1
    return True if i==0 else False

print(valideIPAddress('12.23.35.23'))
