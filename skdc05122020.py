a = int(input())
l = list(map(int(),input().strip().split())))
t = l[-1]%10
for i in range(len(l)-1,-1,-1):
    if(l[i]%10 == t):
        print(l[i],end=" ")
