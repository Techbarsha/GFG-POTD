class Solution:
    def ExtractNumber(self,sentence):
        #code here
        max_number = -1  # Initialize max_number to -1
        words = sentence.split()  # Split the sentence into words

        for word in words:
            num_str = ''.join(filter(str.isdigit, word))  # Extract digits from the word
            if num_str and '9' not in num_str:  # Check if the extracted number exists and does not contain 9
                number = int(num_str)  # Convert the extracted number string to integer
                max_number = max(max_number, number)  # Update max_number if the current number is greater

        return max_number  # Return the final result
