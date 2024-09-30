class Solution:
    def compareFrac (self, str):
        
        # code here
         # Split the input string to get the two fractions
        frac1, frac2 = str.split(', ')
        
        # Split each fraction to get the numerator and denominator
        a, b = map(int, frac1.split('/'))
        c, d = map(int, frac2.split('/'))
        
        # Calculate the cross multiplication values
        first_product = a * d
        second_product = c * b
        
        # Compare the cross multiplication values
        if first_product > second_product:
            return frac1
        elif first_product < second_product:
            return frac2
        else:
            return "equal"
