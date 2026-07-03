import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops =   {
                "+": operator.add,
                "-": operator.sub,
                "*": operator.mul,
                "/": lambda a, b: int(a / b),  # truncate toward zero
                }

        for token in tokens:
            if token in ops:
                b = stack.pop()
                a = stack.pop()
                stack.append(ops[token](a, b))
            else:
                stack.append(int(token))

        return stack[0]