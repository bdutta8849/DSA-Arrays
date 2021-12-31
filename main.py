strings = ['a', 'b' , 'c' , 'd']

def basicOps():
  strings.append('x') #O(1)
  print(strings)

  strings.pop() #O(1)
  print(strings)

  strings.insert(2 , 'y') #O(n)
  print(strings)