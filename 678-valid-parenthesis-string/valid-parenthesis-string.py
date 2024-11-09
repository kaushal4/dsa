class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        wild_count = 0
        open_count = 0
        for i in range(n):
            if s[i] == '(':
                open_count += 1
            elif s[i] == '*':
                wild_count += 1
            else:
                if open_count > 0:
                    open_count -= 1
                elif wild_count > 0:
                    wild_count -= 1
                else:
                    return False
        if open_count == 0:
            return True

        open_count = 0
        wild_count = 0

        for i in range(n-1, -1, -1):
            if s[i] == ')':
                open_count += 1
            elif s[i] == '*':
                wild_count += 1
            else:
                if open_count > 0:
                    open_count -= 1
                elif wild_count > 0:
                    wild_count -= 1
                else:
                    return False
        
        return True