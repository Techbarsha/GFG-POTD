class Solution:
    def stableMarriage(self, men, women):
        # code here
        # This code implemented by Barsha Saha
        n = len(men)
        
        # Track which woman each man will propose next
        next_proposal = [0] * n
        partner_of_man = [-1] * n
        partner_of_woman = [-1] * n

        # Precompute women's ranking of men
        rank = [[0] * n for _ in range(n)]
        for w in range(n):
            for i in range(n):
                rank[w][women[w][i]] = i

        free_men = list(range(n))

        while free_men:
            m = free_men.pop(0)

            # Woman to propose
            w = men[m][next_proposal[m]]
            next_proposal[m] += 1

            if partner_of_woman[w] == -1:
                # Woman is free
                partner_of_woman[w] = m
                partner_of_man[m] = w
            else:
                current = partner_of_woman[w]

                # Check preference
                if rank[w][m] < rank[w][current]:
                    partner_of_woman[w] = m
                    partner_of_man[m] = w
                    partner_of_man[current] = -1
                    free_men.append(current)
                else:
                    free_men.append(m)

        return partner_of_man
        
        
