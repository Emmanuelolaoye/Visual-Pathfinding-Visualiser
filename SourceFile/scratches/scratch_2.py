class DFSinMatrix:
    # Check whether there is path from SourceFile(x,y) to dest (x, y)
    # DFS wraper, Time O(m*n), Space O(m*n)
    def hasPathDfs(self, adj, sx, sy, dx, dy):
        m = len(adj)
        n = len(adj[0])
        visited = [[False for i in range(n)] for j in range(m)]
        self.dfs(adj, sx, sy, visited)
        if visited[dx][dy] == False:
            return False
        return True

    # DFS + memoization, Time O(m*n), Space O(m*n)
    def dfs(self, adj, i, j, visited):
        m = len(adj)
        n = len(adj[0])
        if i < 0 or j < 0 or i > m - 1 or j > n - 1 or adj[i][j] == 1 or visited[i][j]:
            return
        visited[i][j] = True
        self.dfs(adj, i - 1, j, visited)  # Move left
        self.dfs(adj, i + 1, j, visited)  # Move Right
        self.dfs(adj, i, j - 1, visited)  # Move top
        self.dfs(adj, i, j + 1, visited)  # Move bottom


matrix = [[0, 0, 1, 0, 1],
          [0, 0, 0, 0, 0],
          [0, 1, 0, 1, 1],
          [0, 0, 0, 0, 0]]
# find path
sx = 1  # source x
sy = 3  # source y
dx = 3  # destination x
dy = 1  # destination y
g = DFSinMatrix()
print("Find path from (" + str(sx) + "," + str(sy) + ") to (" + str(dx) + "," + str(dy) + "): ")
print("DFS: " + str(g.hasPathDfs(matrix, sx, sy, dx, dy)))