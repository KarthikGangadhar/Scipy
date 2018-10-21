def pair_sum(arr, sum):

  if len(arr) < 2:
    print("invalid data")
    return

  seen = set()
  output = set()

  for num in arr:

    target = sum - num

    if target not in seen:
      seen.add(num)
    else:
      output.add((min(num,target), max(num,target)))

  return "\n".join([str(k) for k in output])

print(pair_sum([1,2,3,4,5,6,7,8,9], 5))
print(pair_sum([1,2,3,4,5,6,7,8,9], 7))
print(pair_sum([1,2,3,4,5,6,7,8,9], 12))

