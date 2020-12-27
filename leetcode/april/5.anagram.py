import sys
import bisect

class Solution:
    def insert(self, list, n): 
        bisect.insort(list, n)  
        return list
  
    def getStringHash(self, txt):
        arr = []
        for i in range(0, len(txt)):
             arr = self.insert(arr, ord(txt[i]))
        return '#'.join(str(x) for x in arr)
    
    def groupAnagrams(self, strs):
        map = {}
        for str in strs:
            strHash = self.getStringHash(str)
            if strHash not in map:
                map[strHash] = []
            map[strHash].append(str)
        arr = []
        for strGrp in map:
            arr.append(map[strGrp])
        return arr

if __name__ == "__main__":
    sol = Solution()
    arr = ["cab","tin","pew","duh","may","ill","buy","bar","max","doc"]
    grp = sol.groupAnagrams(arr);
    print(grp)
'''
 def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = collections.defaultdict(list)
        for item in strs:
            key = tuple(sorted(item))
            dic[key].append(item)
        return dic.values()

'''
