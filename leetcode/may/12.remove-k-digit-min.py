class Solution:
  def removeKdigits(self, num: str, k: int) -> str:
    numLen = len(num)
    if numLen == k:
      return '0'
    currMinDigit = None
    minNum = ''
    lengthToFill = numLen - k
    i = 0
    minIndex = None
    while i < numLen:
      if currMinDigit == None:
        currMinDigit = num[i]
        minIndex = i
      elif num[i] < currMinDigit:
        currMinDigit = num[i]
        minIndex = i
      if currMinDigit == '0' or i == numLen - lengthToFill:
        minNum = minNum + currMinDigit
        lengthToFill -= 1
        i = minIndex + 1
        currMinDigit = None
      else:
        i += 1
    return str(int(minNum))


if __name__ == "__main__":
  print(Solution()
    .removeKdigits(
      '1432219', 3
    )
  )

"""
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack=[]
        for n in num:
            while k and stack and stack[-1]>n:
                stack.pop()
                k-=1
            stack.append(n)
        
        stack = stack[:-k] if k else stack
        #print(stack)
        return "".join(stack).lstrip('0') or "0"
"""