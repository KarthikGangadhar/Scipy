class stack(object):

  def __init__(self):
    self.items = []

  def isEmpty(self):
    return self.items == []

  def push(self, item):
    self.items.append(item)

  def pop(self):
    if self.items != []:
      return self.items.pop()

  def size(self):
    return len(self.items)


def balancce_check(s):

  if len(s) % 2 != 0:
    return False

  opening = set("({[")  
  matching = set([("{","}"),("(",")"),("[","]")])

  stac = stack()
  for paran in s:

    if paran in opening:
      stac.push(paran)
    else:
      if stac.size == 0:
        return False
      else:
        last_opening = stac.pop()
        if (last_opening, paran) not in matching:
          return False
  return stac.size() == 0

print(balancce_check("[]}{[]"))
print(balancce_check("({["))
print(balancce_check("[]{}"))