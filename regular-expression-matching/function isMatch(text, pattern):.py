function isMatch(text, pattern):
    return isMatchHelper(text, pattern, 0, 0)


#  Input:
#    text - the text to check,
#    pattern - the regular expression to be checked,
#    textIndex - the index the text is checked from
#    patIndex -  the index the pattern is checked from
#  Output:
#   true if the text from the index textIndex matches
#   the regular expression pattern from the pattern Index.
#   E.g. isMatchHelper(“aaabb”,”cab*”,2, 1) since the text
#   from index 2 (“abb”) matches the pattern from index 1 (“ab*”)

function isMatchHelper(text, pattern, textIndex, patIndex):
    # base cases - one of the indexes reached the end of text or pattern
    if (textIndex >= text.length):
        if (patIndex >= pattern.length):
            return true
        else:
            if (patIndex+1 < pattern.length) AND  (pattern[patIndex+1] == '*'):
                return isMatchHelper(text, pattern, textIndex, patIndex + 2)
            else:
                return false

    else if (patIndex >= pattern.length) AND (textIndex < text.length):
        return false

    # string matching for character followed by '*'
    else if (patIndex+1 < pattern.length) AND (pattern[patIndex+1] == '*'):
        if (pattern[patIndex] == '.') OR (text[textIndex] == pattern[patIndex]):
            return (isMatchHelper(text, pattern, textIndex, patIndex + 2) OR
                    isMatchHelper(text, pattern, textIndex + 1, patIndex))
        else:
            return isMatchHelper(text, pattern, textIndex, patIndex + 2)

    # string matching for '.' or ordinary char.
    else if (pattern[patIndex] == '.') OR
            (pattern[patIndex] == text[textIndex]):
        return  isMatchHelper(text, pattern, textIndex + 1, patIndex + 1)
    else:
        return false
kevin


len(document) * len(word) * len(result) * n log n

Tim Sort quicksort/insertionsort


// document.split()


O(d*w*r)

0(n )


----------


import string

def word_count_engine(document):
  result = {}
  
  for word in document.split(" "):
    word_ = "".join([i.lower() for i in word if i.isalnum()])
    
    if word_ in result.keys():
      result[word_] += 1
    else:
      result[word_] = 1

  print([[k,v] for k,v in sorted(result.items(),reverse=True, key = lambda x:(x[1],x[0]))])

document = "Practice makes perfect. you'll only get Perfect by practice. just practice!"
word_count_engine(document)







len(document) * len(word) * len(result) * n log n

Tim Sort quicksort/insertionsort


// document.split()


O(d*w*r)

0(n )