# function to convert between different system (hex, dec, oct, alpha)

def convert(input, source, target):
    if source == target:
      return input
    else:
      n = 0
      ret = ''
      for i in range(1, len(input) + 1): # from back
        idx = source.find(input[-i])
        n += idx * len(source) ** (i - 1)
      if n == 0:
      	return target[0]
      while n > 0:
        n, idx = divmod(n, len(target))
        ret = target[idx] + ret
    return ret
    
bin='01'
oct='01234567'
dec='0123456789'
hex='0123456789abcdef'
allow='abcdefghijklmnopqrstuvwxyz'
allup='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alpha='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphanum='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

print(convert("15", dec, bin), '1111', '"15" dec -> bin');
print(convert("15", dec, oct), '17', '"15" dec -> oct');
print(convert("1010", bin, dec), '10', '"1010" bin -> dec');
print(convert("1010", bin, hex), 'a', '"1010" bin -> hex');

print(convert("0", dec, alpha), 'a', '"0" dec -> alpha');
print(convert("27", dec, allow), 'bb', '"27" dec -> alpha_lower');
print(convert("hello", allow, hex), '320048', '"hello" alpha_lower -> hex')
print(convert("SAME", allup, allup), 'SAME', '"SAME" alpha_upper -> alpha_upper');
print(convert('fedcba', hex, dec))
print(convert('ZZZZZZ', alphanum, dec))
