class Solution:
    def multiply_matrices(self, A, B, mod):
        result = [[0, 0], [0, 0]]
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    result[i][j] += (A[i][k] * B[k][j]) % mod
                    result[i][j] %= mod
        return result

    def power_matrix(self, A, n, mod):
        if n == 1:
            return A
        elif n % 2 == 0:
            half_power = self.power_matrix(A, n // 2, mod)
            return self.multiply_matrices(half_power, half_power, mod)
        else:
            half_power = self.power_matrix(A, n // 2, mod)
            return self.multiply_matrices(A, self.multiply_matrices(half_power, half_power, mod), mod)
                
    def firstElement (self, n):
        # code here 
        mod_value = 1000000007
        matrix_a = [[1, 1], [1, 0]]
        result_matrix = self.power_matrix(matrix_a, n, mod_value)
        return result_matrix[1][0]
