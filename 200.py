class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        m = len(grid[0]) + 2
        
        extended_grid = [["0"] * m] + [["0"] + row + ["0"] for row in grid] + [["0"] * m] 
        counter = 0
        
        visited = {}
        
        def grabOneIsland(point, counter):
            if extended_grid[point[0]][point[1]] == "1" and point not in visited:
                visited[point] = counter
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if i == 0 or j == 0:
                            grabOneIsland((point[0] + i, point[1] + j), counter)
                            
        
        for i in range(len(extended_grid)):
            for j in range(len(extended_grid[0])):
                if extended_grid[i][j] == "1" and (i, j) not in visited:
                    counter += 1
                    grabOneIsland((i,j), counter)
                    
        return len(set(visited.values()))
