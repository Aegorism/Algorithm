def search(X, Y, P, Count):
    # 전역 변수 선언
    global total
    if Count == number:
        total += P
        return 

    Now = P
    ground[X][Y] = 1

    for i in range(4):
        nx = X + dx[i]
        ny = Y + dy[i]

        if 0 <= nx < 2*number+1 and 0 <= ny < 2*number+1:
            if ground[nx][ny] == 1:
                continue
            else:
                search(nx, ny, Now*percent[i], Count+1)
                ground[nx][ny] = 0



number, E, W, S, N = map(int, input().split())
percent = [E/100, W/100, S/100, N/100]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

ground = [[0]*(number*2+1) for _ in range(number*2+1)]

total = 0
search(number, number, 1, 0)
print(total)
