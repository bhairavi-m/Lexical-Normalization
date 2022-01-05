"a subdirectory containing all code that you developed for your project, including the baseline and extensions, and your evaluation scripts. This should include a README that gives a step by step walk thorugh of how to run your code, including an example of the command lines to run to reproduce the results that you report."

## Strong Baseline
The strong baseline was established by training a simple character-level RNN using the following command:
```
$ py main.py -logfolder -save_dir S2SChar -gpu 0 -input char -attention -bias -lowercase -bos -eos -brnn -batch_size 32 -dropout 0.2 -emb_size 256 -end_epoch 50 -layers 3 -learning_rate_decay 0.5 -lr 0.001 -max_grad_norm 10 -rnn_size 512 -rnn_type 'LSTM'  -tie_decoder_embeddings -share_embeddings -share_vocab -start_decay_after 30 -teacher_forcing_ratio 0.6  -max_train_decode_len 200
```
but you can just download the model from here_________ and save it to the `S2SChar/` folder. We then evaluated the model using the following command (which, again, you shouldn't have to do)
```
$ py main.py -eval -logfolder -save_dir S2SChar2 -gpu 0 -load_from S2SChar/model_50_char.pt -input char -data_augm -noise_ratio 0.1 -lowercase -bos -eos -batch_size 32 -share_vocab
```
and took the model's output, which we've included in that folder for you, and ran it through `preds.py`, which you don't have to do. We include a copy of this output in the `output/` directory that you can evaluate using the provided script.

## Extension 1




## Extension 2
Extension 2 involved training a word-level model and then two different character-level spelling models, one using their data augmentation function and the other using our enhanced data augmentation function. You shouldn't need to do any training or evaluation because we've included all output in the `/output` directory, but the commands are

Train word-level model:
```
py main.py -logfolder -save_dir word_model -gpu 0 -input word -attention -bias -lowercase -bos -eos -brnn -batch_size 32 -dropout 0.5 -emb_size 100 -end_epoch 50 -layers 3 -learning_rate_decay 0.05 -lr 0.01 -max_grad_norm 5 -rnn_size 200 -rnn_type 'LSTM' -tie_decoder_embeddings -share_embeddings -share_vocab -start_decay_after 15 -teacher_forcing_ratio 0.6  -max_train_decode_len 50
```
or download `model_50_word.pt` from [here](https://drive.google.com/drive/folders/1ycpwbw02DDP2WRxl24z0udGudD-kXsWo?usp=sharing) and save in `word_model/`.

Next, train a character-level model. To choose which `add_noise()` function to use, you'd comment out one or the other in  `rnn_model/lib/data/DataLoader.py`. The version that is readable is ours. Either train the spelling model using the command
```
py main.py -logfolder -save_dir spelling_model -gpu 0 -input spelling -data_augm -noise_ratio 0.1 -attention -bias -lowercase -bos -eos -brnn -batch_size 500 -dropout 0.5 -emb_size 256 -end_epoch 50 -layers 3 -learning_rate_decay 0.05 -lr 0.001 -max_grad_norm 5 -rnn_size 500 -rnn_type 'LSTM'  -tie_decoder_embeddings -share_embeddings -share_vocab -start_decay_after 30 -teacher_forcing_ratio 0.6  -max_train_decode_len 50
```
or download `model_50_spelling.pt` or `model_50_spelling_custom.pt` from [here](https://drive.google.com/drive/folders/1ycpwbw02DDP2WRxl24z0udGudD-kXsWo?usp=sharing) and save it in `/spelling_model_20_pct`.

Test performance is then evaluated by running
```
py main.py -eval -logfolder -save_dir hybrid_model -gpu 0 -load_from word_model/model_50_word.pt -char_model spelling_model/model_50_spelling.pt -input hybrid -data_augm -noise_ratio 0.1 -lowercase -bos -eos -batch_size 32 -share_vocab
```
which generates the folder `hybrid_model_20_pct` or `hybrid_model_20_pct_custom`. We've included all of this output for you so that you don't have to retrain and run inference.

