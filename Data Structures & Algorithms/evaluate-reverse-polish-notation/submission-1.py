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
                a = nums.pop()
                b = nums.pop()
                res = int(ops[t](b, a))
                nums.append(res)
            else:
                nums.append(int(t))
        return nums[-1]