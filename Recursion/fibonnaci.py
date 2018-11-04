def fibonnaci(n):
  #1. using recurssion
  if n == 0 or n == 1:
    return n
  else:
    return fibonnaci(n-1) + fibonnaci(n-2)

  #2. iterative method
  # a,b = 0,1

  # for i in range(n):
  #   a,b = b, a+b
  # return a  


for i in range(20):
  print(fibonnaci(i))

