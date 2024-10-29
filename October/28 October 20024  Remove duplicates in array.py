class Solution:

    def removeDuplicates(self, arr):
            # code here 
            l=[]
            di={}
            for i in arr:
                if i not in di:
                    di[i]=1 
                    l.append(i)
            return l
    
