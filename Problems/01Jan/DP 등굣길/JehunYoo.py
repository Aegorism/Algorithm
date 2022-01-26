# BFS, dynamic programming: O(mn)
def solution(m, n, puddles):
    answer = 0
    grid = [[0 for _ in range(m)] for _ in range(n)] # Space complexity O(mn)
    for px, py in puddles:
        grid[py - 1][px - 1] = -1
    
    queue = [(0, 0)]
    while queue:
        x, y = queue.pop(0)
        if grid[y][x] == 0:
            if x == y == 0:
                grid[y][x] += 1
            if y - 1 >= 0 and grid[y - 1][x] > 0:
                grid[y][x] += grid[y - 1][x]
            if x - 1 >= 0 and grid[y][x - 1] > 0:
                grid[y][x] += grid[y][x - 1]

            if y + 1 < n:
                queue.append((x, y + 1))
            if x + 1 < m:
                queue.append((x + 1, y))
    
    print(grid)
    answer = grid[n - 1][m - 1]
    return answer % 1000000007