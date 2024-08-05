class Solution:
    # Rename parameter to avoid shadowing built-in str
    def isValid(self, str_):
        #code edutechbarsha
        # Split the string by dots
        parts = str_.split('.')
        
        # There should be exactly four parts
        if len(parts) != 4:
            return False
        
        for part in parts:
            # Each part should be a number and should not be empty
            if not part.isdigit():
                return False
            
            # Convert to integer to check the range
            num = int(part)
            if num < 0 or num > 255:
                return False
            
            # Ensure no leading zeros unless it is exactly "0"
            if part != str(num):
                return False
        
        return True
