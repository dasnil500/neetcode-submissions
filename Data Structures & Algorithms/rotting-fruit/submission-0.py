class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        fresh, time = 0, 0
        queue = deque()
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    queue.append([i,j])
                elif grid[i][j] == 1:
                    fresh += 1
                else: continue

        while queue and fresh > 0:
            for i in range (len(queue)):
                m,n = queue.popleft()
                directions = [[-1,0], [1,0], [0,1], [0,-1]]
                for dr, dc in directions:
                    new_r, new_c = m+dr, n+dc
                    if new_r > -1 and new_r < row and new_c > -1 and new_c < col and grid[new_r][new_c] == 1:
                         grid[new_r][new_c] = 2
                         fresh -= 1
                         queue.append([new_r, new_c])
                    else: continue

            time += 1
        return time if fresh == 0 else -1