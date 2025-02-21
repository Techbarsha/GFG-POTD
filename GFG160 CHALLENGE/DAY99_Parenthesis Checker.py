class Solution:
    def isBalanced(self, s):
        # code here
        st1=[]
        mp={
            "}":"{",
            "]":"[",
            ")":"("
        }
        
        for i in s:
            if i in "{[(":
                st1.append(i)
            elif st1 and st1[-1]==mp[i]:
                st1.pop()
            else:
                return False
                
                
        return len(st1)==0 
