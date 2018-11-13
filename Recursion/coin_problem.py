import collections

rec_count = 0
dyn_rec_count = 0
def rec_coin(target,coins,rec_count):
  rec_count += 1
  print("rec_count :{0}".format(rec_count))
  min_coins = target
  if target in coins:
    return 1

  else:
    for i in [c for c in coins if c < target]:
      num_coins = 1 + rec_coin(target - i, coins,rec_count)

      if num_coins < min_coins:
        min_coins = num_coins
  return min_coins


def rec_coin_dynamic(target, coins, know_values,dyn_rec_count):
  min_coins = target
  dyn_rec_count += 1
  print("dyn_rec_count :{0}".format(dyn_rec_count))
  if target in coins:
    return 1
  elif know_values[target] > 0:
    return know_values[target]  
  else:
    for i in [c for c in coins if c <= target]:
      num_coins = 1 + rec_coin_dynamic(target - i, coins, know_values, dyn_rec_count)

      if num_coins < min_coins:
        min_coins = num_coins
        know_values[target] = num_coins
  return min_coins     


# print(rec_coin(64, [1,5,6,8,10,15], 0))
print(rec_coin_dynamic(64, [1,5,6,8,10,15],collections.defaultdict(int), 0))