class Solution:
    def armstrongNumber (self, n):
        # code here 
         # Extracting digits of the number
        hundreds = n // 100
        tens = (n // 10) % 10
        units = n % 10
        
        # Calculating the sum of the cubes of the digits
        sum_of_cubes = hundreds**3 + tens**3 + units**3
        
        # Checking if the sum of the cubes is equal to the number itself
        if sum_of_cubes == n:
            return "Yes"
        else:
            return "No"
