class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        create a stack
        iterate tokens
        if ith value is an operator
            
            a = stack.pop()
            b = stack.pop()
            result = a operator b
            stack.append(result)
        else
            insert into stack
        """

        stack = []
        for token in tokens:
            if token == "+":
                a = stack.pop()
                b = stack.pop()
                result = int(b) + int(a)
                stack.append(result)
            elif token == "-":
                a = stack.pop()
                b = stack.pop()
                result = int(b) - int(a)
                stack.append(result)
            elif token == "*":
                a = stack.pop()
                b = stack.pop()
                result = int(b) * int(a)
                stack.append(result)
            elif token == "/":
                a = stack.pop()
                b = stack.pop()
                result = int(b) / int(a)
                stack.append(result)
            else:
                stack.append(token)
            
        return int(stack.pop())
