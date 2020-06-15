s = ["o","n","e","."," ","+","t","w","o"," ","t","h","r","e","e","?"," ","~","f","o","u","r"," ","!","f","i","v","e","-"]
players = ["o","n","e","."," ","+","t","w","o"," ","t","h","r","e","e","?"," ","~","f","o","u","r"," ","!","f","i","v","e","-"]
print(s[-1:])
#print(players[2:6])
#print("--------------")
#print(players[3:])
#print(players[-3:])
#print("--------------")
#print(players[:3])
#print(players[:-3])
#print("--------------")

s[:] = list(" ".join("".join(s).split()[::-1]))
print(s)
print("=================")
for i in range(len(players)//2):
    players[0+i], players[len(players)-1-i] = players[len(players)-1-i], players[0+i]
temp = 0
for k in range(len(players)):
    if players[k] == ' ':
        for j in range(len(players[temp:k])//2):
            players[temp+j], players[k-1-j] = players[k-1-j],players[temp+j]
        temp = k+1
    elif k == len(players)-1:
        for l in range(len(players[temp:k+1])//2):
            players[temp+l], players[k-l] = players[k-l],players[temp+l]

print(players)
print("=================")

s = "  the   man  is on the   top of the hill   "
print(' '.join(s.strip().split()[::-1]))


