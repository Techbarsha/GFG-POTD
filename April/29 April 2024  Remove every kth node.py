class Solution:
    def deleteK(self, head, k):
        #code here  
         if k == 1:
            return None

         current = head
         prev = None
         count = 1

        
         while current:
            if count == k:
                if prev:
                    prev.next = current.next
                else:
                    head = current.next
                
                current = current.next
                count = 1 
            else:
                prev = current
                current = current.next
                count += 1  

         return head
