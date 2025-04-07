class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if not stack:
                stack.append(int(t))
            else:
                if t == "+":
                    stack.append(stack.pop() + stack.pop())
                elif t == "-":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b - a)
                elif t == "*":
                    stack.append(stack.pop() * stack.pop())
                elif t == "/":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(int(b / a))  # // 는 floor
                else:
                    stack.append(int(t))
        return stack[0]
