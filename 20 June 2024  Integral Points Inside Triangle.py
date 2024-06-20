class Solution:
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a
    
    def boundaryCount(self, p, q):
        if p[0] == q[0]:
            return abs(p[1] - q[1]) - 1
        if p[1] == q[1]:
            return abs(p[0] - q[0]) - 1
        return self.gcd(abs(p[0] - q[0]), abs(p[1] - q[1])) - 1
    
    def InternalCount(self, p, q, r):
        #code here
        boundary = self.boundaryCount(p, q) + self.boundaryCount(p, r) + self.boundaryCount(q, r) + 3
        Area = abs(
            p[0] * (q[1] - r[1]) + q[0] * (r[1] - p[1]) + r[0] * (p[1] - q[1])
        )
        return (Area - boundary + 2) // 2
