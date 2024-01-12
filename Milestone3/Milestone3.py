import math

readObject = open(r"D:\KLA Hackathon\Milestone3\Input\Testcase1.txt","r")
inp=readObject.read()

inp=inp.split("\n")

values=[]
for i in inp:
    values.append(i.split(":")[1])

values[1]=values[1].split("x")
for i in range(2,len(values)-1):
    values[i]=values[i][1:len(values[i])-1].split(",")
values[len(values)-1]=values[len(values)-1].split("x")

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
    
dieStreet=[]
for i in values[4]:
    dieStreet.append(int(i))

reticleStreet=[]
for i in values[5]:
    reticleStreet.append(int(i))
    
diesPerReticle=[]
for i in values[6]:
    diesPerReticle.append(int(i))

radius=diameter/2

outstr=""
dic={(0,0):0}
flag1=0
flag2=1
def dfs(x,y,i,j,flag1,flag2):
    global outstr
    
    left=math.dist([0,0], [x,y])
    right=math.dist([0,0], [x+dieSize[0],y])
    top=math.dist([0,0],[x,y+dieSize[1]])
    bottom=math.dist([0,0], [x+dieSize[0],y+dieSize[1]])
    
    flag1=flag1+1
    flag2=flag2+1
    
    if dic.get((i,j),0)==1:
        return
    if left<radius or right<radius or top<radius or bottom<radius:
        print("(",i,",",j,"):(",x,y,")")
        outstr+="("+str(i)+","+str(j)+"):("+str(x)+","+str(y)+")\n"
        
        dic[(i,j)]=1
        if flag1%diesPerReticle[0]==0:
            dfs(x+dieSize[0]+dieStreet[0]+reticleStreet[0],y,i+1,j,flag1,flag2)
            dfs(x-dieSize[0]-dieStreet[0],y,i-1,j,flag1,flag2)
        else:
            dfs(x+dieSize[0]+dieStreet[0],y,i+1,j,flag1,flag2)
            dfs(x-dieSize[0]-dieStreet[0]-reticleStreet[0],y,i-1,j,flag1,flag2)
            
        if flag2%diesPerReticle[1]==0:
            dfs(x,y+dieSize[1]+dieStreet[1]+reticleStreet[1],i,j+1,flag1,flag2)
            dfs(x,y-dieSize[1]-dieStreet[1],i,j-1,flag1,flag2)
        else:
            dfs(x,y+dieSize[1]+dieStreet[1],i,j+1,flag1,flag2)
            dfs(x,y-dieSize[1]-dieStreet[1]-reticleStreet[1],i,j-1,flag1,flag2)
        
    else:
        return

dfs(refDieCoordinate[0],refDieCoordinate[1],0,0,flag1,flag2)

writeObject=open(r"D:\KLA Hackathon\Milestone3\Output\Testcase1.txt","w")
writeObject.write(outstr)
writeObject.close()
