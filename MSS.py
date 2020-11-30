import sys
a = int(input())
l = list(map(int,input().strip().split()))
cm = 0
m = -sys.maxsize
i = 0
for i in l:
    cm += i
    if(cm>m):
        m = cm
    if(cm<0):
        cm = 0
print(m)
