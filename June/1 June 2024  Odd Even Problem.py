class Solution:
    def oddEven(self, s : str) -> str:
        # code here
        from collections import Counter
        
        # Count the frequency of each character
        frequency = Counter(s)
        
        x = 0
        y = 0
        
        for char, freq in frequency.items():
            position = ord(char) - ord('a') + 1  # Get the 1-based position of the character in the alphabet
            
            if position % 2 == 0:  # Even position in the alphabet
                if freq % 2 == 0:  # Even frequency
                    x += 1
            else:  # Odd position in the alphabet
                if freq % 2 == 1:  # Odd frequency
                    y += 1
        
        # Determine if the sum of x and y is even or odd
        if (x + y) % 2 == 0:
            return "EVEN"
        else:
            return "ODD"
