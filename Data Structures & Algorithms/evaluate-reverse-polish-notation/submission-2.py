class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        OPERATORS = ["+", "-", "*", "/"]
        for token in tokens:
            if token not in OPERATORS:
                stack.append(int(token))
            else:
                operand_2 = stack.pop()
                operand_1 = stack.pop()
                if token == "+":
                    operand_new = operand_1 + operand_2
                elif token == "-":
                    operand_new = operand_1 - operand_2
                elif token == "*":
                    operand_new = operand_1 * operand_2
                else:
                    operand_new = math.trunc(operand_1 / operand_2)
                stack.append(operand_new)
            
        return stack[0]