def finder(arr1, arr2):
  arr1 = sorted(arr1)
  arr2 = sorted(arr2)

  found = set()
  seen = set()
  for num in arr1:
    if num not in arr2:
      found.add(num)
    else:
      seen.add(num)

  return "\nMissing number(s) from arrays are :\n".join([str(num) for num in found])     

print(finder([1,2,3,45,67,8],[1,23,4,56,4,3,5]))
print(finder([1,2,3,4],[1,2,3,4]))
