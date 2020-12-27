class Solution:
  def frequencySort(self, s: str) -> str:
    charMap = {}
    for ch in s:
      if ch in charMap:
        charMap[ch] += 1
      else:
        charMap[ch] = 1
    arr = []
    for key in charMap:
      ct = charMap[key]
      ob = {"ch": key, "ct": ct}
      if len(arr) == 0:
        arr.append(ob)
      else:
        i = 0
        l1 = len(arr)
        while i < len(arr):
          if arr[i]["ct"] > ct:
            break
          i = i + 1
        if i == 0:
          arr.insert(0, ob)
        elif i == l1:
          arr.append(ob)
        else:
          arr = arr[0:i]  + [ob] + arr[i:l1]
    st = ''
    while len(arr) > 0:
      ob = arr.pop()
      ch = ob["ch"]
      for i in range(ob["ct"]):
        st = st + ch
    return st
    

if __name__ == "__main__":
  print(Solution()
    .frequencySort(
      'abaccadeeefaafcc'
    )
  )

