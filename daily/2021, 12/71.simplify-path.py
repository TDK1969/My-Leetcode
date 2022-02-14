class Solution:
    def simplifyPath(self, path: str) -> str:
        directory = path.split('/')
        directory = [i for i in directory if i]
        stack = []

        for i in directory:
            if i == "..":
                if stack:
                    stack.pop()
            elif i == ".":
                continue
            else:
                stack.append(i)

        if not stack:
            return "/"

        ans = ""
        for j in stack:
            ans += '/' + j

        return ans

test = Solution()
print(test.simplifyPath(path = "/home/"))