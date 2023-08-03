count=int(input("Введите колличество кустов: "))
wilb=[]
maxWilb = 0
while count > 0:
    print(len(wilb))
    wilb.append(int(input("Введите колличество ягод на кусте: ")))
    count-=1
for i in range(len(wilb)):
    if i+1 < len(wilb):
        if wilb[i-1] + wilb[i] +  wilb[i+1] > maxWilb:
            maxWilb = wilb[i-1] + wilb[i] +  wilb[i+1]
    else:
        if wilb[i-1] + wilb[i] +  wilb[0] > maxWilb:
            maxWilb = wilb[i-1] + wilb[i] +  wilb[0]

print(maxWilb)