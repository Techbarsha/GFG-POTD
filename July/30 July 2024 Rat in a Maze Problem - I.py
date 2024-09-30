class Solution:
    def findPath(self, m: List[List[int]]) -> List[str]:
        # code here edutechbarsha
        def isSafe(x, y):
            return 0 <= x < n and 0 <= y < n and m[x][y] == 1 and not visited[x][y]

        def solve(x, y, path):
            if x == n - 1 and y == n - 1:
                paths.append(path)
                return
            
            visited[x][y] = True
            for direction, (dx, dy) in directions.items():
                newX, newY = x + dx, y + dy
                if isSafe(newX, newY):
                    solve(newX, newY, path + direction)
            visited[x][y] = False

        n = len(m)
        if m[0][0] == 0:
            return []
        paths = []
        visited = [[False] * n for _ in range(n)]
        directions = {
            'D': (1, 0),
            'U': (-1, 0),
            'R': (0, 1),
            'L': (0, -1)
        }
        solve(0, 0, "")
        return paths
