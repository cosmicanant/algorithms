class Solution:
  def isSubsequence(self, s: str, t: str) -> bool:
    i = 0
    j = 0
    l1 = len(s)
    l2 = len(t)
    nextStart = None
    while i < l1 and j < l2:
      if i > 0 and s[0] == t[j]:
        nextStart = j
      if s[i] == t[j]:
        i = i + 1
        j = j + 1
      else:
        j = j + 1
        if j == l2 and nextStart is not None:
          i = 1
          j = nextStart + 1
          nextStart = None
    return i == l1
        

if __name__ == "__main__":
  sol = Solution()
  s =  "rjufvjafbxnbgriwgokdgqdqewn"
  t = "mjmqqjrmzkvhxlyruonekhhofpzzslupzojfuoztvzmmqvmlhgqxehojfowtrinbatjujaxekbcydldglkbxsqbbnrkhfdnpfbuaktupfftiljwpgglkjqunvithzlzpgikixqeuimmtbiskemplcvljqgvlzvnqxgedxqnznddkiujwhdefziydtquoudzxstpjjitmiimbjfgfjikkjycwgnpdxpeppsturjwkgnifinccvqzwlbmgpdaodzptyrjjkbqmgdrftfbwgimsmjpknuqtijrsnwvtytqqvookinzmkkkrkgwafohflvuedssukjgipgmypakhlckvizmqvycvbxhlljzejcaijqnfgobuhuiahtmxfzoplmmjfxtggwwxliplntkfuxjcnzcqsaagahbbneugiocexcfpszzomumfqpaiydssmihdoewahoswhlnpctjmkyufsvjlrflfiktndubnymenlmpyrhjxfdcq"
  s = sol.isSubsequence(s, t)
  print(s)