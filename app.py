def generateProgression(start, d, n):
  prog_list = [start]
  for x in range(2, int(n) + 1):
    next = start + d * (x - 1)
    prog_list.append(next)
  
  return prog_list
  
def countSum(list):
  sum = 0
  for x in list:
    sum = sum + x
  
  return sum


n = input("Enter number of elements in progression: ")

progression = generateProgression(3, 6, n)
print("Result progression:")
print(progression)

print("Result sum of progression:")
print(countSum(progression))