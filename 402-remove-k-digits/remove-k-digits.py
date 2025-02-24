class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for i in range(len(num)):
            while k > 0 and stack and stack[-1] > num[i]:
                stack.pop()
                k -=1
            stack.append(num[i])
        if k > 0 and stack:
            stack = stack[:-k]
        return "".join(stack).lstrip('0') or "0"