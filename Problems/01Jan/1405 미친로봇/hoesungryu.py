def dfs(x, y, cnt, p):
    global ans

    if cnt==N:
        ans += p
        return 

    
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        
        if board[nx][ny]: #방문하였다면 무시하고 진행
            continue
        if not 0<= nx <(2*N+1) or not 0 <= ny< (2*N+1): # 보드 밖에 있다면 무시하고 진행 
            continue
            
        board[x][y] = 1 # 방문표시
        dfs(nx, ny, cnt + 1, p * position[i] * 0.01) #퍼센티지 곱해주기
        board[x][y] = 0 # 다 조사한뒤에는 방문한 지점을 지워줘야합니다.



N,e,w,s,n = map(int, input().split()) # 동서남북 

board = [[0] * (2*N+1) for _ in range(2*N+1)]
board[N][N] = 1

position = [e,w,s,n]

dx= [1,-1,0,0]
dy= [0,0,-1,1]
ans = 0

dfs(N, N, 0, 1)
print(ans)