a,b = map(str,input().strip().split())
fi = a.index(b)
li = (len(a) - 1) - a[len(a)-1:0:-1].index(b)
k = a[fi+1:li]
print(a[0:fi+1:]+k[::-1]+a[li::])
