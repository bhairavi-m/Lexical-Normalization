from parameters import parser, change_args
import logging
import os
import lib
import json

##################################
# TOGGLE WHETHER OR NOT TO USE GPU
GPU = False
##################################

logger = logging.getLogger("main")

def main(): #-logfolder -gpu 0
  opt = parser.parse_args(f'-eval {"-gpu 0 " if GPU else ""}-save_dir S2SChar -load_from S2SChar/model_50_char.pt -input char -data_augm -noise_ratio 0.1 -lowercase -bos -eos -batch_size 32 -share_vocab'.split(' '))
  opt = change_args(opt)

  logging.basicConfig(filename=os.path.join(opt.save_dir, 'output.log') if opt.logfolder else None, level=logging.INFO)

  train_data, valid_data, test_data, vocab, mappings = lib.data.create_datasets(opt)
  model, optim = lib.model.create_model((vocab['src'], vocab['tgt']), opt)

  test_evaluator = lib.train.Evaluator(model, opt)
  logger.info(model.opt)
  logger.info('Loading test data from "%s"' % opt.testdata)
  logger.info('Loading training data from "%s"' % opt.traindata)
  logger.info(' * Vocabulary size. source = %d; target = %d' % (len(vocab['src']), len(vocab['tgt'])))
  logger.info(' * Maximum batch size. %d' % opt.batch_size)
  logger.info(model)

  logger.info("=======Eval on test set=============")
  pred_file = os.path.join(opt.save_dir, 'test_pred.json')
  test_evaluator.eval(test_data, pred_file=pred_file)

  json_file = open(f'S2SChar/test_pred.json')
  json_object = json.load(json_file)

  # each tweet has tid, index, output, input, target
  outfile = open("test_pred.txt", "w")

  for tweet in json_object:
    for input_word, output_word, target_word in zip(tweet['input'], tweet['output'], tweet['target']):
      outfile.write(f'{input_word}\t{output_word}\t{target_word}\n')

    outfile.write('\n')
  outfile.close()

if __name__ == "__main__":
  main()