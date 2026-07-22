class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        res = 0
        for op in operations:
            if op == "+":
                two_nums = stack[-1] + stack[-2]
                res += two_nums
                stack.append(two_nums)
            elif op == "D":
                double_num = stack[-1] * 2
                res += double_num
                stack.append(double_num)
            elif op == "C":
                res -= stack.pop()
            else:
                num = int(op)
                res += num
                stack.append(num)

        return res