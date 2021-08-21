from typing import Union

def reverse_vowels(s: str) -> str:
  tmp_s = list(s)

  vowels = ["a", "e", "i", "o", "u"]
  i, j = 0, len(tmp_s) - 1

  while (i < j):
    if tmp_s[i] not in vowels:
      i += 1
      continue

    if tmp_s[j] not in vowels:
      j -= 1
      continue

    tmp_s[i], tmp_s[j] = tmp_s[j], tmp_s[i]
    i += 1
    j -= 1

  return "".join(tmp_s)

assert reverse_vowels("hello world") == "hollo werld"
