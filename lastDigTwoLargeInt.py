
# calculate the last digit of n1^n2 where they can be large, only use mod() logic

seq = {1: [1], 2: [2, 4, 8, 6], 3: [3, 9, 7, 1], 4: [4, 6], 5: [5], 6: [6], 7: [7, 9, 3, 1], 8: [8, 4, 2, 6], 9: [9, 1], 0: [0]}

def last_digit(n1, n2):
    lastd = n1 % 10
    if n2 == 0:
      return 1
    if lastd in [0, 1, 5, 6]:
      return lastd
    else:
      s = seq[lastd]
      rem = (n2 - 1) % len(s)
      return s[rem]
      
print(last_digit(100, 0), 1)
print(last_digit(9, 7), 9)
print(last_digit(10, 10 ** 10), 0)
print(last_digit(2 ** 200, 2 ** 300), 6)
print(last_digit(3715290469715693021198967285016729344580685479654510946723, 68819615221552997273737174557165657483427362207517952651), 7)


