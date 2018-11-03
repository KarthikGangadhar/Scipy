import collections

def finder(arr1, arr2):

  if (len(arr1) == 0  or len(arr2) == 0 or (len(arr1) == len(arr2))):
    return "invalid array input"

# solution type 1
  # d = collections.defaultdict(int)

  # for num in arr2:
  #   d[num] += 1

  # for num in arr1:
  #   if d[num] == 0:
  #     return num
  #   else:
  #     d[num] -= 1
  
# solution type 2

  # count = {}

  # for num in arr1:
  #   if num not in count:
  #     count[num] = 1
  #   else:
  #     count[num] += 1

  # for num in arr2:
  #   if num not in arr2:
  #     count[num] = 1
  #   else:
  #     count[num] -= 1

  # for num in count:
  #   if count[num] != 0:
  #     return num

# solution type 3
  result = 0

  for num in arr1 + arr2:
    print("XOR of {0} and {1} : {2}".format(result,num, result ^ num) )
    result ^= num
    print(result)

  return result  

print(finder([],[1,2,3]))          
print(finder([1,2,3], []))          
print(finder([1,2,3], [1,2,3]))
print(finder([1,2,3], [1,3]))
print(finder([1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8]))


