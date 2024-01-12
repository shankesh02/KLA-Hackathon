import math

readObject = open(r"D:\KLA Hackathon\Milestone2\Input\Testcase3.txt","r")
inp=readObject.read()

inp=inp.split("\n")

values=[]
for i in inp:
    values.append(i.split(":")[1])

values[1]=values[1].split("x")
for i in range(2,len(values)):
    values[i]=values[i][1:len(values[i])-1].split(",")

diameter = int(values[0])
dieSize=[]
for i in values[1]:
    dieSize.append(int(i))
    
dieShiftVector=[]
for i in values[2]:
    dieShiftVector.append(int(i))
    
refDie=[]
for i in values[3]:
    refDie.append(int(i))

refCenter=[]
for i in range(2):
    refCenter.append(refDie[i])

refDieCoordinate=[]
for i in range(2):
    refDieCoordinate.append(refCenter[i]-(dieSize[i]/2))

radius=diameter/2

outstr=""
dic={(0,0):0}
def dfs(x,y,i,j):
    global outstr
    
    left=math.dist([0,0], [x,y])
    right=math.dist([0,0], [x+dieSize[0],y])
    top=math.dist([0,0],[x,y+dieSize[1]])
    bottom=math.dist([0,0], [x+dieSize[0],y+dieSize[1]])
    
    
    if dic.get((i,j),0)==1:
        return
    if left<radius or right<radius or top<radius or bottom<radius:
        print("(",i,",",j,"):(",x,y,")")
        outstr+="("+str(i)+","+str(j)+"):("+str(x)+","+str(y)+")\n"
        dic[(i,j)]=1
        dfs(x+dieSize[0],y,i+1,j)
        dfs(x-dieSize[0],y,i-1,j)
        dfs(x,y+dieSize[1],i,j+1)
        dfs(x,y-dieSize[1],i,j-1)
    else:
        return

dfs(refDieCoordinate[0],refDieCoordinate[1],0,0)
    

writeObject=open(r"D:\KLA Hackathon\Milestone2\Output\Testcase3.txt","w")


writeObject.write(outstr)
writeObject.close()
