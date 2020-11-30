#the program accepts an array of n elements and prints two elements(at distinct positions) that add upto x
n,x = map(int,input().strip().split())
arr = list(map(int,input().strip().split()))
f = 0
s = sorted(arr)
one = 0
two = len(arr)-1
while(one<two):
    t = s[one] + s[two]
    if(t==x):
        op = arr.index(s[one])+1
        if(s[one]==s[two]):
            op = arr.index(s[one])+1
            print("%d %d"%(op,arr[op::].index(s[two]) + len(arr[0:op+1])))
            f = 1
            break
        else:
            print("%d %d"%(arr.index(s[one])+1,arr.index(s[two])+1))
            f = 1
            break
    elif(t>x):
        two -= 1
    else:
        one += 1
if(f == 0):
    print("IMPOSSIBLE")

