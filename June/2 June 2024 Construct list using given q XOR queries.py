from typing import List

class Solution:
    def constructList(self, q: int, queries: List[List[int]]) -> List[int]:
    #code here
        s = [0]  # Initial list with a single element 0
        cumulative_xor = 0  # Track the cumulative XOR
        
        for query in queries:
            if query[0] == 0:
                # Insert x into the list, XORed with the cumulative XOR value
                s.append(query[1] ^ cumulative_xor)
            elif query[0] == 1:
                # Update the cumulative XOR value
                cumulative_xor ^= query[1]
        
        # Apply the cumulative XOR value to each element in the list
        for i in range(len(s)):
            s[i] ^= cumulative_xor
        
        # Sort the list before returning
        s.sort()
        return s
