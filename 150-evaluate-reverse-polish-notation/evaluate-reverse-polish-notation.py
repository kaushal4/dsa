class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '+':
                new_val = (stack.pop() + stack.pop()) 
                stack.append(new_val)
            elif token == '-':
                a = stack.pop()
                b = stack.pop()
                new_val = (b - a)
                stack.append(new_val)
            elif token == '*':
                new_val = (stack.pop() * stack.pop())
                stack.append(new_val)
            elif token == '/':
                a = stack.pop()
                b = stack.pop()
                new_val = int(b / a)
                stack.append(new_val)
            else:
                stack.append(int(token))
        return stack.pop() if stack else 0