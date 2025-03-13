class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for ch in s:
            if ch in bracket_map:
                if stack and stack[-1] == bracket_map.get(ch):
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        
        return len(stack) == 0
