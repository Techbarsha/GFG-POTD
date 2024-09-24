class Solution:

    #Function to find the smallest window in the string s consisting

    #of all the characters of string p.

    def smallestWindow(self, s, p):

        #code edutech barsha 

        if len(p) > len(s):

            return "-1"

        

        forS = [0] * 26

        forP = [0] * 26

        

        c = 0

        for char in p:

            forP[ord(char) - ord('a')] += 1

            if forP[ord(char) - ord('a')] == 1:

                c += 1



        start = -1

        end = -1

        len_min_window = float('inf')

        c2 = 0

        j = 0

        

        for i in range(len(s)):

            forS[ord(s[i]) - ord('a')] += 1

            

            if forS[ord(s[i]) - ord('a')] == forP[ord(s[i]) - ord('a')]:

                c2 += 1

            

            if c2 == c:

                while forS[ord(s[j]) - ord('a')] > forP[ord(s[j]) - ord('a')]:

                    forS[ord(s[j]) - ord('a')] -= 1

                    j += 1

                

                if len_min_window > i - j + 1:

                    start = j

                    end = i

                    len_min_window = i - j + 1

        

        if start == -1:

            return "-1"

        

        return s[start:end + 1]
