def pair_sum(arr, sum):

  if len(arr) < 2:
    return "array is not valid"

  seen = set()  
  output = set()

  for num in arr:
    target = sum - num

    if target not in seen:
      seen.add(num)

    else:
      output.add(((min(target,num),max(target, num))))


  return "\n".join([str(k) for k in output])

print("output 1:")
print(pair_sum([0,1,2,3,4,5,6,7,8,9], 5))
print("output 2:")
print(pair_sum([0,1,2,3,4,5,6,7,8,9], 7))
print("output 3:")
print(pair_sum([0,1,2,3,4,5,6,7,8,9], 12))
