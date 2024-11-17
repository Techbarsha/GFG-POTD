class Solution:
    def minDistance(self, alice, bob, apples):
        # Code Here
        from math import inf
        n = len(apples)
        positions = [(0, 0)] * (n + 1)
        
        for i in range(n):
            positions[i + 1] = (apples[i][0], apples[i][1])
        positions[0] = (alice[0], alice[1])
        bob_initial = (bob[0], bob[1])  

        dp = [[inf] * (n + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for i in range(n + 1):
            for j in range(n + 1):
                if dp[i][j] == inf:
                    continue
                k = max(i, j) + 1
                if k > n:
                    continue
                
                # Transition for Alice picking apple k
                alice_pos = positions[i] if i > 0 else positions[0]
                dist = dp[i][j] + abs(alice_pos[0] - positions[k][0]) + abs(alice_pos[1] - positions[k][1])
                if dist < dp[k][j]:
                    dp[k][j] = dist
                
                # Transition for Bob picking apple k
                bob_pos = positions[j] if j > 0 else bob_initial
                dist = dp[i][j] + abs(bob_pos[0] - positions[k][0]) + abs(bob_pos[1] - positions[k][1])
                if dist < dp[i][k]:
                    dp[i][k] = dist

        
        answer = inf
        for i in range(n + 1):
            answer = min(answer, dp[n][i], dp[i][n])

        return answer
