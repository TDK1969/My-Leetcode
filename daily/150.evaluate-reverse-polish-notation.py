class Solution(object):
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
                stack.append(front / back)
            else:
                token = int(token)
                stack.append(token)
        return stack.pop()
            
