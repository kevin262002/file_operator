f1 = open("first.txt","r")
f2 = open("second.txt","w")

for line in f1:
    f2.write(line)

f2.close()
