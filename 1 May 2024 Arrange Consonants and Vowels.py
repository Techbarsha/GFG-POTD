class Solution:
    #Function to reverse a linked list.
    def arrangeCV(self, head):
        # Code here
        if not head or not head.next:
            return head
        
        # Helper function to check if a character is a vowel
        def is_vowel(char):
            return char in 'aeiou'
        
        # Separate vowels and consonants into two separate lists
        vowels_head, consonants_head = None, None
        vowels_tail, consonants_tail = None, None
        
        current = head
        while current:
            next_node = current.next
            current.next = None  # Disconnect current node from the list
            
            if is_vowel(current.data):
                if not vowels_head:
                    vowels_head = current
                    vowels_tail = current
                else:
                    vowels_tail.next = current
                    vowels_tail = current
            else:
                if not consonants_head:
                    consonants_head = current
                    consonants_tail = current
                else:
                    consonants_tail.next = current
                    consonants_tail = current
            
            current = next_node
        
        # Connect vowels and consonants lists
        if vowels_head:
            vowels_tail.next = consonants_head
            return vowels_head
        else:
            return consonants_head
