class Solution:
    def nextPalindrome(self, num):
        # code here 
        
        # This code implemented by Barsha Saha
        n = len(num)

        # If all digits are 9
        if all(x == 9 for x in num):
            return [1] + [0] * (n - 1) + [1]

        # Copy left to right
        pal = num[:]
        for i in range(n // 2):
            pal[n - i - 1] = pal[i]

        # If palindrome > original, return
        if pal > num:
            return pal
        carry = 1
        mid = n // 2

        # If odd length → handle middle element
        if n % 2 == 1:
            pal[mid] += carry
            carry = pal[mid] // 10
            pal[mid] %= 10
            left = mid - 1
            right = mid + 1
        else:
            left = mid - 1
            right = mid

        # Propagate carry
        while left >= 0 and carry:
            pal[left] += carry
            carry = pal[left] // 10
            pal[left] %= 10
            pal[right] = pal[left]
            left -= 1
            right += 1

        while left >= 0:
            pal[right] = pal[left]
            left -= 1
            right += 1

        return pal
        
        
