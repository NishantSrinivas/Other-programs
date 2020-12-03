def GCD(a,b):
    if(a==0):
        return b
    return GCD(b%a,a)
def LCM(a,b):
    return((a*b)//GCD(a,b))
R,C = map(int,input().strip().split())
mat = []
for i in range(R):
    mat.append(list(map(int,input().strip().split())))
X,Y = map(int,input().strip().split())
s = 0
t = R-1
for x in range(R):
    print(LCM(mat[s][X-1],mat[t][Y-1]),end = " ")
    s+=1
    t-=1
    
