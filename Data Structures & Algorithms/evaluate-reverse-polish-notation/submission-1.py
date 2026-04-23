class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        oper = '*-+/'
        for n in tokens:
            if n in oper:
                

                if n == '+':
                    stack.append(stack.pop() + stack.pop())
                elif n == '*':
                    stack.append(stack.pop() * stack.pop())
                elif n == '/':
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(int(a / b))
                elif n == '-':
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(a - b)
            else:
                num = int(n)
                stack.append(num)
        return stack[-1]
