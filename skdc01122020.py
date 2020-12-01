m,n,k = map(int,input().strip().split())
s = ""
l = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
for i in range(k):
    x = len(l)
    if((i+1)%2!=0):
        p = l[(m%x)-1]
        s+=p
        l.remove(p)
    else:
        q = l[(n%x)-1]
        s+=q
        l.remove(q)
print(s)
