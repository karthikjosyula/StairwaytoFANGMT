class Solution(object):
    def romanToInt(s):
        romanmap = {"I": 1,"V": 5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        def recursiveromanint(s):
            #romanmap = {"I": 1,"V": 5, "X":10, "L":50, "C":100, "D":500, "M":1000}
            currval = 0
            l = len(s)
            if(0 <= len(s) <= 1):
                return 0 if len(s) == 0 else (currval + romanmap[s])
            else:
                rs = s[1:l]
                if(romanmap[s[0]] < romanmap[s[1]]):
                    currval = -1*romanmap[s[0]]
                else:
                    currval = romanmap[s[0]]
                return currval + recursiveromanint(rs)
        return recursiveromanint(s)

    print(romanToInt("LIIIIIIIXII"))
