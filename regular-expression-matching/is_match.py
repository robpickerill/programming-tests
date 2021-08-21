"""
Problem Statement
Given an input string s and a pattern p, implement regular expression matching with support for . and * where:

. Matches any single character.​​​​
* Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Constraints:
0 <= s.length <= 20
0 <= p.length <= 30
s contains only lowercase English letters.
p contains only lowercase English letters, ., and *.
It is guaranteed for each appearance of the character *, there will be a previous valid character to match.
"""

def is_match(s: str, p: str) -> bool:
  rows, columns = len(s), len(p)

  if rows == 0 and columns == 0:
    return True
  if columns == 0:
    return False

  # initialise cache as all False
  # size +1 is to eval empty strings for s and p
  dp = [[False for _ in range(columns + 1)] for _ in range(rows + 1)]

  # An empty string and an empty pattern is a match
  dp[0][0] = True

  # step through * patterns
  for i in range(2, columns + 1):
    if p[i - 1] == "*":
      dp[0][i] = dp[0][i - 2]

  for i in range(1, rows + 1):
    for j in range(1, columns + 1):

      # the rules:
      # if s == p or p == .
      # then take the value of the previous char in the string, which is up and to the left
      # in the cache
      if s[i - 1] == p[j - 1] or p[j - 1] == '.':
        dp[i][j] = dp[i - 1][j - 1]


      elif j > 1 and p[j - 1] == "*":
        dp[i][j] = dp[i][j - 2]


        if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
          dp[i][j] = dp[i][j] or dp[i - 1][j]

  return dp[rows][columns]


print(is_match("aaaa", "a.a."))
print(is_match("aaaab", "a.a.*"))
print(is_match("a", "a"))
print(is_match("nope", "aaaa"))
