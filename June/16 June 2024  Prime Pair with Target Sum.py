from typing import List


class Solution:
    def getPrimes(self, n : int) -> List[int]:
        # code here
        if n < 4:
            return [-1, -1]

        # Step 1: Sieve of Eratosthenes to find all primes up to n
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes
        
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                for j in range(i*i, n + 1, i):
                    is_prime[j] = False

        # Step 2: Find the pair (a, b) such that a + b = n and both are primes
        for a in range(2, n):
            if is_prime[a]:
                b = n - a
                if b >= a and is_prime[b]:
                    return [a, b]
        
        return [-1, -1]
