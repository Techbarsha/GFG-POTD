class Solution:
    def patternCount(self, text, pattern):
        # Write your code here
        n = len(text)
        m = len(pattern)
        pos = pattern.find('$')
        s1 = pattern[:pos]
        s2 = pattern[pos + 1:]
        len_s1 = len(s1)
        len_s2 = len(s2)

        # Determine where s1 starts in text
        is_s1_start = [False] * n
        if len_s1 == 0:
            for i in range(n):
                is_s1_start[i] = True
        else:
            for i in range(n - len_s1 + 1):
                if text[i:i + len_s1] == s1:
                    is_s1_start[i] = True

        # Determine where s2 ends in text
        is_s2_end = [False] * n
        if len_s2 == 0:
            for j in range(n):
                is_s2_end[j] = True
        else:
            for j in range(len_s2 - 1, n):
                if text[j - len_s2 + 1:j + 1] == s2:
                    is_s2_end[j] = True

        # Compute suffix sums for is_s2_end
        suffix_sums = [0] * (n + 1)
        for j in range(n - 1, -1, -1):
            suffix_sums[j] = suffix_sums[j + 1] + (1 if is_s2_end[j] else 0)

        # Count valid patterns
        result = 0
        for i in range(n):
            if is_s1_start[i]:
                minimal_j = i + len_s1 + len_s2
                if minimal_j >= n:
                    continue
                result += suffix_sums[minimal_j]

        return result
