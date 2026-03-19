class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        def solve(i, j):
            
            if j == len(p):
                return i == len(s)

            if i < len(s) and (s[i] == p[j] or p[j] == '.'):
                match = True
            else:
                match = False

            if j + 1 < len(p) and p[j + 1] == '*':

                if solve(i, j + 2):
                    return True

                if match:
                    return solve(i + 1, j)

                return False

            else:
                if match:
                    return solve(i + 1, j + 1)
                else:
                    return False

        return solve(0, 0)