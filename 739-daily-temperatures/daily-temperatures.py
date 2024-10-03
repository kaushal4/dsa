class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        sol = []
        for i in range(len(temperatures)-1,-1,-1):
            while stack:
                if stack[-1][0] > temperatures[i]:
                    break
                stack.pop()
            if not stack:
                sol.append(0)
            else:
                sol.append(stack[-1][1] - i)
            stack.append((temperatures[i],i))
        return sol[::-1]