class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        temp = s[0]
        maxLen = 1
        currLen = 1
        for i in range(1, len(s)):
            currentCharIndexInTemp = temp.find(s[i])
            if currentCharIndexInTemp >= 0:
                maxLen = max(currLen, maxLen)
                if currentCharIndexInTemp == len(temp) - 1:
                  temp = s[i]
                else:
                  temp = temp[currentCharIndexInTemp + 1:] + s[i]
                currLen = len(temp)
            else:
                temp = temp + s[i]
                currLen = len(temp)
                maxLen = max(currLen, maxLen)
        return maxLen

if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLongestSubstring("pwwkew"))
