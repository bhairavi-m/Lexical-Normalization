import json

def load_json(file_name):
  json_file = open(file_name)
  return json.load(json_file)

# each tweet has tid, index, output, input, target

pred_ours = load_json('test_pred_ours.json')
pred_theirs = load_json('test_pred_theirs.json')

conversion_unneeded = 0
conversion_needed = 0
us = 0
them = 0

# output input target
# print(json.dumps(pred_ours[0], indent=4))
for ours, theirs in list(zip(pred_ours, pred_theirs)):
  for i in range(len(ours['input'])):
    if (ours['output'][i] == ours['target'][i]) and (theirs['output'][i] != theirs['target'][i]):
      # print(ours['input'][i], ours['target'][i], '...', ours['output'][i], theirs['output'][i])
      us += 1
      # if ours['input'][i] == ours['target'][i]:
      #   conversion_unneeded += 1
      # else:
      #   conversion_needed += 1

    if (ours['output'][i] != ours['target'][i]) and (theirs['output'][i] == theirs['target'][i]):
      print(ours['input'][i], ours['target'][i], '...', ours['output'][i], theirs['output'][i])
      them += 1

      if ours['input'][i] == ours['target'][i]:
        conversion_unneeded += 1
      else:
        conversion_needed += 1
# {"tid":"470171172999426050","index":"7539","output":["i'm","in","suhc","a","weird","peaceful","mood","i","ain't","felt","peaceful","since","naptime","in","kindergarten"],"input":["im","in","suhc","a","weird","peaceful","mood","i","aint","felt","peaceful","since","naptime","in","kindergarten"]}
print(f'conversion needed {conversion_needed}; unneeded {conversion_unneeded}')
print(f'us {us}; them {them}')