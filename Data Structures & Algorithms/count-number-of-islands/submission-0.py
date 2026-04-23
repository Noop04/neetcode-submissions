class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islandCount = 0
        rows, cols = len(grid), len(grid[0])
        def bfs(r, c):
            # TODO
            if r >= rows or r < 0 or c >= cols or c < 0 or grid[r][c] == '0':
                return 
            grid[r][c] = '0'
            bfs(r + 1, c)
            bfs(r - 1, c)
            bfs(r, c + 1)
            bfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    bfs(r,c)
                    islandCount += 1

        return islandCount