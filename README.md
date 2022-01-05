# Lexical Normalization

To get access to the results that our scripts generate, we have made a structure that allows you to run only two lines of code:

Once you are inside `code/scripts` folder on the command line, you can execute the following commands:

```
$ python baselines-with-extensions.py
```
```
$ python score.py
```


The first command will generate the prediction text files that will be stored in the output folder. These files will then be accessed by `score.py` which will evaluate the predictions and display results on the command line itself.

Since our code contains an implementation of a code base from the `Adapting Sequence to Sequence models for Text Normalization in Social Media` research paper, we use the pretrained model. To be able to run those models and generate files from the start refer to the `PRETRAINED.md` file.

The project is implemented as a solution for the challenge held by the [7th Workshop on Noisy User-Generated Text (W-NUT) with EMNLP 2021]
(https://noisy-text.github.io/2021/multi-lexnorm.html)
