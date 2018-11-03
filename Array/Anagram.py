def Anagram(s1, s2):
  s1 = s1.lower().replace(" ", "")
  s2 = s2.lower().replace(" ", "")

  if len(s1) != len(s2):
    return False

  # return sorted(s1) == sorted(s2)
  
  count = {}

  for letter in s1:
    if letter in count:
      count[letter] += 1
    else:
      count[letter] = 1

  for letter in s2:
    if letter in count:
      count[letter] -= 1
    else:
      count[letter] = 1

  for item in count:
    if count[item] != 0:
      return False

  return True


print(Anagram("dog","God"))
print(Anagram("clint eastwood ","old west action"))
