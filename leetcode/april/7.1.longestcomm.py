
cache = {}
def solve (str1, str2, i, j):
    key = str(i) + str(j)
    if key in cache:
        return cache[key]
    elif i >= len(str1) or j >= len(str2):
        subseqLen = 0
    elif str1[i] == str2[j]:
        subseqLen  = 1 + solve(str1, str2, i+1, j + 1)
    else:
        subseqLen = max(
            solve(str1, str2, i + 1, j),
            solve(str1, str2, i, j + 1)
        );
    cache[key] = subseqLen;
    return subseqLen;
if __name__ == "__main__":
  str1 = '12341'
  str2 = '341213'
  print(solve(str1, str2, 0, 0))
