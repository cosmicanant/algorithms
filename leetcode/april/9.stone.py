class Solution:
    def findTwoMax(self, arr):
        max1 = 0 if arr[0] > arr[1] else 1
        max2 = 1 if max1 == 0 else 0
        
        for i in range(2, len(arr)):
            if arr[i] > arr[max1]:
                max2 = max1
                max1 = i
            elif (arr[max1] >= arr[i] > arr[max2]):
                max2 = i
        return [max1, max2]
        
    def lastStoneWeight(self, stones: [int]) -> int:
        arrLen = len(stones)
        if arrLen == 0:
            return 0
        elif arrLen == 1:
            return stones[1]
        else:
            arr = stones
            while len(arr) > 1:
                maxIndices = self.findTwoMax(arr)
                newEl = arr[maxIndices[0]] - arr[maxIndices[1]]
                arr.pop(maxIndices[0])
                if maxIndices[1] > maxIndices[0]:
                  arr.pop(maxIndices[1]-1)
                else:
                  arr.pop(maxIndices[1])
                if(newEl > 0):
                    arr.append(newEl)
            return 0 if len(arr) == 0 else arr[0]

if __name__ == "__main__":
    sol = Solution()
    print(sol.lastStoneWeight([4,3,4,3,2]))