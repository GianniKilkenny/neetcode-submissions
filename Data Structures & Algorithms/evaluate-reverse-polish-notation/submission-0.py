import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv,
        }
        nums = []

        for t in tokens:
            if t in ops:
                b = nums.pop()
                a = nums.pop()
                nums.append(int(ops[t](a, b)))  # int() to truncate toward zero
            else:
                nums.append(int(t))

        return nums[-1]