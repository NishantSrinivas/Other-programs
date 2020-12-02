a = int(input())
l = list(map(int,input().strip().split()))
for i in range(a):
    if(l[i]%10==0):
        if(l[i]%100//10>0):
            l[i] = (l[i]-10)+1
        else:
            l[i] = 0
print(sum(l))
