def permute(str):
  out = []
  if len(str) == 1:
    return [str]

  else:
    for i,let in enumerate(str):
      for perm in permute(str[:i] + str[i+1:]):
        out += [let+ perm]
  
  print("permute length: {0}".format(len(out)))
  print(out)
  return out

permute("ab")