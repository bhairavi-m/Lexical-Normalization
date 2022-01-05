import json

json_file = open(f'test_pred_ours.json')
json_object = json.load(json_file)

# each tweet has tid, index, output, input, target

outfile = open("test_pred_ours.txt","a")

for tweet in json_object:
  for input_word, output_word, target_word in zip(tweet['input'], tweet['output'], tweet['target']):
    outfile.write(f'{input_word}\t{output_word}\t{target_word}\n')

  outfile.write('\n')

outfile.close()