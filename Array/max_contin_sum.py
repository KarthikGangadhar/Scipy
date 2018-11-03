def max_sum(arr):

  if len(arr) <= 0:
    return "Enter a valid array"

  current_sum = max_sum = arr[0]
  startIndex = 0
  endIndex = 0
  for num in arr[1:]:
    # current_sum = max(num, current_sum + num)
    current_sum += num
    if num > current_sum:
      startIndex = arr.index[num]
      current_sum = num
    else:
      endIndex = arr.index(num)

    # max_sum = max(current_sum, max_sum)
    if current_sum < max_sum:
      startIndex = arr.index(num)
    else:
      max_sum = current_sum
  print("arr: {0}".format(arr))
  print("start Index:{0} and EndIndex: {1}".format(startIndex,endIndex))
  return max_sum

print(max_sum([1,2,3,-5,6,7,7]))
print(max_sum([1,2,3,4,-2,1,-5]))
print(max_sum([1,2,-3]))