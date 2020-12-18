def digit_sum(n):
    sum = 0
    while(n!=0):
        sum += n%10
        n = n//10
    return sum
a = int(input())
b = list(map(int,input().strip.split()))
c = list(map(int,input().strip.split()))
flag = 0
for i in b:
    if(digit_sum(i) in c):
        flag = 1
        print(i,end=" ")
if(flag==0):
    print("-1")
