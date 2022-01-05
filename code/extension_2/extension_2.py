import random

def leaveOutCharacter(word):
  i = random.randint(0,len(word)-1)

  return word[:i] + word[i+1:]

def swapCharOrder(word):
  i = random.randint(0,len(word)-1)

  i += 1

  return word[:i-1] + word[i:i+1] + word[i-1:i] + word[i+1:]

def keyboardError(word):
  i = random.randint(0,len(word)-1)

  return word[:i] + random.choice(prox_arr[word[i]]) + word[i+1:]  if word[i] in prox_arr else word #default is keyboard errors

def misplaceApostrophe(word):
    idx = word.find("'")

    if idx != -1: 
      # you're -> youre'
      # return word[:idx] + word[idx+1:] + word[idx]

      # you're -> yo'ure
      # return word[:idx-1] + word[idx:idx+1] + word[idx-1:idx] + word[idx+1:]

      # you're -> youre
      # return word[:idx] + word[idx+1:]

      return word[:idx-1] + word[idx:idx+1] + word[idx-1:idx] + word[idx+1:] if random.randint(0, 1) else word[:idx] + word[idx+1:]

def extendLastCharacter(word):
  l = word[-1]

  # if l == 'u' or l == 'y' or l == 's' or l == 'r' or l == 'a' or l == 'o' or l == 'i':
  return word + random.randint(1, 5) * l

def extendChar(word):
  o = word.find('o')
  e = word.find('e')
  a = word.find('a')
  h = word.find('h')
  i = word.find('i')
  x = word.find('x')

  idx = max([o, e, a, h, i, x])

  if idx != -1:
    return word[:idx] +  random.randint(1, 5) * word[idx] + word[idx:]

def add_noise(word):
  op = random.randint(0, 9)
  # print(f'Chosen op {op}')

  if op == 0:
    return leaveOutCharacter(word)

  if op == 1:
    return swapCharOrder(word)

  if op == 2:
    return keyboardError(word)
  
  if op == 3:
    return misplaceApostrophe(word)

  if op in [4, 5, 6]:
    return extendLastCharacter(word)

  if op in [7, 8, 9]:
    return extendChar(word)

def get_prox_keys():
  array_prox = {}

  array_prox['a'] = ['q', 'w', 'z', 'x', 's']
  array_prox['b'] = ['v', 'f', 'g', 'h', 'n', ' ']
  array_prox['c'] = ['x', 's', 'd', 'f', 'v']
  array_prox['d'] = ['x', 's', 'w', 'e', 'r', 'f', 'v', 'c']
  array_prox['e'] = ['w', 's', 'd', 'f', 'r']
  array_prox['f'] = ['c', 'd', 'e', 'r', 't', 'g', 'b', 'v']
  array_prox['g'] = ['r', 'f', 'v', 't', 'b', 'y', 'h', 'n']
  array_prox['h'] = ['b', 'g', 't', 'y', 'u', 'j', 'm', 'n']
  array_prox['i'] = ['u', 'j', 'k', 'l', 'o']
  array_prox['j'] = ['n', 'h', 'y', 'u', 'i', 'k', 'm']
  array_prox['k'] = ['u', 'j', 'm', 'l', 'o']
  array_prox['l'] = ['p', 'o', 'i', 'k', 'm']
  array_prox['m'] = ['n', 'h', 'j', 'k', 'l']
  array_prox['n'] = ['b', 'g', 'h', 'j', 'm']
  array_prox['o'] = ['i', 'k', 'l', 'p']
  array_prox['p'] = ['o', 'l']
  array_prox['q'] = ['w', 'a']
  array_prox['r'] = ['e', 'd', 'f', 'g', 't']
  array_prox['s'] = ['q', 'w', 'e', 'z', 'x', 'c']
  array_prox['t'] = ['r', 'f', 'g', 'h', 'y']
  array_prox['u'] = ['y', 'h', 'j', 'k', 'i']
  array_prox['v'] = ['', 'c', 'd', 'f', 'g', 'b']
  array_prox['w'] = ['q', 'a', 's', 'd', 'e']
  array_prox['x'] = ['z', 'a', 's', 'd', 'c']
  array_prox['y'] = ['t', 'g', 'h', 'j', 'u']
  array_prox['z'] = ['x', 's', 'a']
  array_prox['1'] = ['q', 'w']
  array_prox['2'] = ['q', 'w', 'e']
  array_prox['3'] = ['w', 'e', 'r']
  array_prox['4'] = ['e', 'r', 't']
  array_prox['5'] = ['r', 't', 'y']
  array_prox['6'] = ['t', 'y', 'u']
  array_prox['7'] = ['y', 'u', 'i']
  array_prox['8'] = ['u', 'i', 'o']
  array_prox['9'] = ['i', 'o', 'p']
  array_prox['0'] = ['o', 'p']

  return array_prox

prox_arr = get_prox_keys()

print("Example mutations of \"you\'re\"")
for _ in range(10):
  print(add_noise("you're"))