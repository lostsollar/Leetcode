class Solution(object):
    # my own solution version1.0
    def isValid(self, s):
        stack = []
        for i in range(len(s)):
            if s[i] in [")", "]", "}"]:
                if len(stack) == 0:
                    return False
                left = ord(s[i]) - 1 if s[i] == ")" else ord(s[i]) - 2
                right = ord(stack[-1])
                if left != right:
                    return False
                stack.pop()
            if s[i] in ["(", "[", "{"]:
                stack.append(s[i])
        return True if len(stack) == 0 else False

    # my own solution version2.0
    def isValid1(self, s):
        stack = []
        for c in s:
            if c in ["(", "[", "{"]:
                stack.append(c)
            elif not stack:
                return False
            else:
                left = ord(c) - 1 if c == ")" else ord(c) - 2
                right = ord(stack[-1])
                if left != right:
                    return False
                stack.pop()
        return not stack

    # https://time.geekbang.org/course/detail/130-41557
    def isValid2(self, s):
        stack = []
        parentheses_map = {")": "(", "]": "[", "}": "{"}
        for c in s:
            if c not in parentheses_map:
                stack.append(c)
            elif not stack or parentheses_map[c] != stack.pop():
                return False
        return not stack


if __name__ == "__main__":
    checker = Solution()
    test1 = "()"
    print checker.isValid(test1)
    print checker.isValid1(test1)
    test2 = "(){}[]"
    print checker.isValid(test2)
    print checker.isValid1(test2)
    test3 = "(]"
    print checker.isValid(test3)
    print checker.isValid1(test3)
    test4 = "{[]}"
    print checker.isValid(test4)
    print checker.isValid1(test4)