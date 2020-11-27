a = int(input())
l = []
for i in range(a):
    l.append(input())
for j in l:
    if(j[::-1] in l):
        print("%d %s"%(len(j),j[len(j)//2]))
        break
