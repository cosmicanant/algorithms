class Solution:
    def applyEl(self, ch, stack):
        if ch == '(':
            stack.append('(')
        elif ch == ')':
            if len(stack) > 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')
        return stack

    def getCacheKey(self, stack, i):
        return ''.join(stack) + str(i)

    def ifValid(self, s: str, stack, j):
        key = self.getCacheKey(stack, j)
        if key in self.cache:
            return self.cache[key]
        for i in range(j, len(s)):
            if s[i] != '*':
                stack = self.applyEl(s[i], stack)
                if len(stack) > 0 and stack[-1] == ')':
                    break
            else:
                if i+1 == len(s):
                    if len(stack) == 0:
                        stack = []
                        break
                    elif stack[-1] == '(':
                        stack.pop()
                        break
                    else:
                        stack.append(')')
                        break
                temp = self.ifValid(s, self.applyEl('(', stack[0:]), i+1)
                if len(temp) == 0:
                    stack = []
                    break
                elif len(temp) > 0 and temp[-1] == ')':
                    stack = temp
                    break
                temp = self.ifValid(s, self.applyEl(')', stack[0:]), i+1)
                if len(temp) == 0:
                    stack = temp
                    break
        self.cache[key] = stack[0:]
        return stack

    def checkValidString(self, s: str) -> bool:
        self.cache = {}
        if len(s) == 0:
            return True
        stack = self.ifValid(s, [], 0)
        return len(stack) == 0


if __name__ == "__main__":
    sol = Solution()
    # print(sol.checkValidString('((*)(*()(())())())()()((()())((()))(*'))
    # print(sol.checkValidString('(*)'))
    print(sol.checkValidString('**'))

"""
best solution
class Solution:
    def checkValidString(self, s: str) -> bool:
        
        lo, hi = 0, 0
        for c in s:
            lo += 1 if c == '(' else -1
            hi += 1 if c != ')' else -1
            if hi < 0: break
            lo = max(lo, 0)
        return lo == 0
"""