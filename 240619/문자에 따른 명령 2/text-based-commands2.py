dir_num =0
x,y =0,0
dx,dy=[0,1,0,-1],[1,0,-1,0]

# rotate Circluar
def RC(dir_num):
    dir_num = (dir_num + 1) % 4
    return dir_num

#rotate CountCircluar
def RCC(dir_num):
    dir_num = (dir_num - 1 + 4) % 4
    return dir_num

C= input()
for i in range(len(C)):
    if(C[i]=="R"):
        dir_num=RC(dir_num)
    elif(C[i]=="L"):
        dir_num=RCC(dir_num)
    elif(C[i]=="F"):
        x,y=x+dx[dir_num],y+dy[dir_num]
print(x, y)