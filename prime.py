import sys

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

# num1 = int(input('Enter number 1'))
# num2 = int(input('Enter number 2'))

print(f"Prime numbers between {num1} and {num2} are: ")
for x in range(num1, num2 + 1):
  count = 0
  for y in range(2, x//2+1):
    if (x % y == 0):
      count = count + 1
      break
  if (count == 0 and x != 1):
    print(f"{x} ", end = ' ')