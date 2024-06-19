def func(dir,dis,x,y):
    if dir == "E":
        nx, ny = x + dis*dx[0], y + dis*dy[0]
    elif dir == "S":
        nx, ny = x + dis*dx[1], y + dis*dy[1]
    elif dir == "W":
        nx, ny = x + dis*dx[2], y + dis*dy[2]
    else:
        nx, ny = x + dis*dx[3], y + dis*dy[3]

    return nx,ny;

N =int(input())
x, y = 0, 0
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
for i in range(N):
    user_input = input();
    dir_dis = user_input.split()
    dis =int(dir_dis[1])
    x,y=func(dir_dis[0], dis,x,y)
print(x, y)