class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        n = len(s)
        i = 0
        sol = ''
        while i < n: 
            print(stack)
            if ord(s[i]) >= 97 and ord(s[i]) < 123:
                stack.append(s[i])
            if s[i] == '[':
                i+= 1
                continue
            if s[i] == ']':
                val = ''
                while stack[-1] != '[':
                    val = stack.pop() + val
                stack.pop()
                num = stack.pop()
                new = ''
                for _ in range(int(num)):
                    new += val
                stack.append(new)
            if ord(s[i]) >= 48 and ord(s[i]) < 58:
                num = ''
                while ord(s[i]) >= 48 and ord(s[i]) < 58 and i < n:
                    num += s[i]
                    i += 1
                number = int(num)
                stack.append(number)
                stack.append('[')
            i += 1
        sol = ''
        while stack:
            sol = stack.pop() + sol 
        return sol