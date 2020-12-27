def solve(S, T):
  len1 = len(S) - 1
  len2 = len(T) - 1
  while len1 >= 0 or len2 >= 0:
      if S[len1] == T[len2]:
          len1 = len1 - 1
          len2 = len2 - 1
      elif S[len1] == '#':
          len1 = len1 - 2
      elif T[len2] == '#':
          len2 = len2 -2
      else:
          break
  print(len1)
  print(len2)
  print(len1 == -1 and len2 == -1)

if __name__ == '__main__':
    solve("ab#c", "ad#c"
)