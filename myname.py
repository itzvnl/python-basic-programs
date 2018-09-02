#print the last letter from myname

myname = input("Enter you name:")
#print(myname[-1])
'''
print(myname[0])
print(myname[1])
print(myname[2])
print(myname[3])
print(myname[4])
'''
#Method1
#LIST
newarray = []
oddcount = 0
evencount = 0
for i in range(len(myname)):
    print (myname[i])
    newarray.append(i)
    newarray.append(myname[i])

         
print ("New Array from Myname..",newarray)
result = 0
for i in newarray:
    if type(i) == int:
        result = result + i
print("SUM of interger numbers from Array..",result)
#ODDEVEN
for i in range(len(newarray)):
     if i % 2 == 0:
         evencount = evencount + 1
     else:
          oddcount = oddcount + 1
print ("ODD position values",evencount)
print ("Even Position values",oddcount)
#Tuple
tuplearray = []
#expected output = [(0,'K'),(1,'G')]
for i in range(len(myname)):
    tuplearray.append((i,myname[i]))

print("New tuple from myname",tuplearray)
#dictionary
newdict = {}
for i in range(len(myname)):
     newdict[i] = myname[i]
print("New dict from myname",newdict)
print (newdict[0])
'''
#mentod2
for i in myname:
     print (i)
'''
