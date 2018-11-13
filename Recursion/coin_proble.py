import collections

def CoinProblem(target, coins, known_values):
  min_coins = target
  if target in coins:
      return 1
  elif known_values[target] > 0:
    return known_values[target]
  else:
    for i in [c for c in coins if c <= target]:
      num_coins = 1 + CoinProblem(target -i, coins, known_values)
      print(" min num of coins for {0} is : {1}".format(i, num_coins))
      if num_coins < min_coins:
        min_coins = num_coins
        known_values[target] =  min_coins
  return min_coins      


# print(rec_coin(64, [1,5,6,8,10,15], 0))
print(CoinProblem(64, [1,5,6,8,10,15],collections.defaultdict(int)))  