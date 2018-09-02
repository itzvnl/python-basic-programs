file = open("C:\\Users\\vasan\\OneDrive\\Desktop\\test.txt","r")
for line in file:
     x = line.split(",")
     print(x[0],'\t',x[2])
