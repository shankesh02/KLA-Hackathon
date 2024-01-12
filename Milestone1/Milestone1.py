import math

readObject = open(r"C:\Users\tharu\Downloads\Workshop2024\Milestone1\Input\Testcase4.txt","r")
inp=readObject.read()

inp=inp.split("\n")

values=[]
for i in inp:
    values.append(int(i.split(":")[1]))

output=[]
flag=0
radius=int(values[0]/2)
neg=-radius
space=(values[0]/(values[1]-1))

angle=values[2]

endy = 0 - round(radius * math.sin(math.radians(angle)),4)
endx = 0 - round(radius * math.cos(math.radians(angle)),4)

print(endx,endy)

for i in range(values[1]):
    output.append([endx,endy])
    endy = round(endy + space * math.sin(math.radians(angle)),4)
    endx = round(endx + space * math.cos(math.radians(angle)),4)

writeObject=open(r"C:\Users\tharu\Downloads\Workshop2024\Milestone1\Input\Testcase4Out.txt","w")
outstr=""
for i in output:
    outstr+="("+str(i[0])+","+str(i[1])+")\n"

writeObject.write(outstr)
writeObject.close()
