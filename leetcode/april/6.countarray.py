import sys
import bisect

class Solution:
     def countElements(self, arr: [int]) -> int:
        map = {}
        for el in arr:
            if el not in map:
                map[el] = { 'count': 0, 'occurance': 1}
            else:
                map[el]['occurance'] = map[el]['occurance'] + 1
            if (el - 1) in map and map[el-1]['count'] == 0:
                     map[el-1]['count'] = map[el-1]['occurance']
            if(el + 1) in map:
                map[el]['count'] = map[el]['count'] + 1
        count = 0
        for key in map:
            count = count + map[key]['count']
        return count

if __name__ == "__main__":
    sol = Solution()
    arr = [1,3,2,3,5,0]
    count = sol.countElements(arr);
    print(count)
'''
 def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = collections.defaultdict(list)
        for item in strs:
            key = tuple(sorted(item))
            dic[key].append(item)
        return dic.values()

'''
