#Run length encoder and decoder
a = input().strip()
def runLengthEncoder(a):
    prev = a[0]
    count = 0
    s = ""
    for i in a:
        if(i==prev):
            count+=1
        else:
            s = s + str(count) + prev
            prev = i
            count = 1
    s = s + str(count) + prev
    return s
def runLengthDecoder(a):
    s = ""
    for i in range(len(a)-1):
        if(a[i].isdigit()):
            s += int(a[i])*(a[i+1])
    return(s)
print(runLengthEncoder(a))
print(runLengthDecoder(runLengthEncoder(a)))
