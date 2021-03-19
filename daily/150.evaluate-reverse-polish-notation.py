class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for token in tokens:
            if token == '+':
                back = stack.pop()
                front = stack.pop()
                stack.append(front + back)
            elif token == '-':
                back = stack.pop()
                front = stack.pop()
                stack.append(front - back)
            elif token == '*':
                back = stack.pop()
                front = stack.pop()
                stack.append(front * back)
            elif token == '/':
                back = stack.pop()
                front = stack.pop()
                stack.append(int(front / back))
            else:
                token = int(token)
                stack.append(token)
        return stack.pop()

#tokens = ['10', '6', '9', '3', '+', '-11', '*', '/', '*', '17', '+', '5', '+']
#print(Solution.evalRPN(Solution, tokens))

