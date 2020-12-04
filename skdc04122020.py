l = input().strip().split()
ccount = {}
maxc = 0
for i in l:
    c = 0
    for j in i:
        if(j.isalpha() and j not in "aeiouAEIOU"):
            c+=1
    maxc = max(c,maxc)
    ccount[i] = c
p = len(l)-1
while(ccount[l[p]]!=maxc):
    l.pop()
    p-=1
print(*l)
