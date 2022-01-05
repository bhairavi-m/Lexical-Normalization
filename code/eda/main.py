from DataHandler import DataHandler

dh_train = DataHandler('train')
dh_test = DataHandler('test')

print(len(dh_train.X), len(dh_test.X))

letters = []

for tweet in dh_train.X:
  for word in tweet:
    prevLetter = word[0]
    n = 1

    for letter in word[1:]:
      if letter == prevLetter:
        n += 1

        if n == 3 and letter.isalnum():
          # print(word, letter)
          letters.append(letter)
      else:
        n = 1
        prevLetter = letter

from collections import Counter

print(len(letters), Counter(letters))

letters = []
for tweet in dh_train.X:
  for word in tweet:
    if len(word) > 2 and len(list(set(list(word[-3:])))) == 1 and list(set(list(word[-3:])))[0].isalnum():
      letters.append(word[-1])
      # print(word, word[-1])
print(len(letters), Counter(letters))

    