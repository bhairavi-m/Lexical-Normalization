import json
import random
import seaborn as sb
from matplotlib import pyplot as plt

class DataHandler(object):
  def __init__(self, data_set):
    self.load_data(data_set)

  def load_data(self, data_set):
    data_set_2_file_name = {'train': 'train_data', 'test': 'test_truth'}
    json_file = open(f'data/lexnorm2015/{data_set_2_file_name[data_set]}.json')
    json_object = json.load(json_file)

    setattr(self, 'raw', json_object)

    self.X = []
    self.y = []

    for tweet in json_object:
      self.X.append([token.lower() for token in tweet['input']])
      self.y.append(tweet['output'])

  def sample(self):
    i = random.randint(0, len(self.raw)-1)
    pairs = list(zip(self.X[i], self.y[i]))

    for input, output in pairs:
      print(input, '\t', output, sep='')

  def generateNormal2Slang(self):
    normal2slang = {}

    for X, y in list(zip(self.X, self.y)):
      for X_token, y_token in list(zip(X, y)):
        try:
          if X_token != y_token:
            try:
              normal2slang[y_token][X_token] += 1
            except:
              normal2slang[y_token] = { X_token: 1 }
        except:
          pass

    print(json.dumps(normal2slang, indent=2))

  def generateSlang2N(self):
    slang2N = {}

    for X, y in list(zip(self.X, self.y)):
      for X_token, y_token in list(zip(X, y)):
        try:
          if X_token != y_token:
            try:
              slang2N[X_token] += 1
            except:
              slang2N[X_token] = 1
        except:
          pass

    slang2N = dict(sorted(slang2N.items(), key=lambda item: item[1]))
    print(json.dumps(slang2N, indent=2))

    xs = [1, 2, 3, 4, 5, 6, 7, 8, 9, '10+']
    ys = [0] * 10

    for slang, n in slang2N.items():
      ys[min(n, 10)-1] += 1

    print(ys)
    plt.xlabel('Occurrence of non-standard words')
    plt.ylabel('Number of non-standard words')
    plt.title('Distribution of occurrences of non-standard words')
    plt.bar(list(range(10)), height=ys, tick_label=xs, color='k')
    plt.show()
    

if __name__ == '__main__':
  dh = DataHandler('train')
  dh.sample()
  dh.generateSlang2N()