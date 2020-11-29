a = input().strip()
s = ""
for i in a:
    if(i == "a" or i=="A"):
        s += i*2
    elif(i == "e" or i=="E"):
        s += i*3
    elif(i == "i" or i=="I"):
        s += i*4
    elif(i == "o" or i=="O"):
        s += i*5
    elif(i == "u" or i=="U"):
        s += i*6
    else:
        s += i
print(s)
