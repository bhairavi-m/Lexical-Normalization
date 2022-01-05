from os import error
import argparse
parser = argparse.ArgumentParser("path")
parser.add_argument('--outputpath',type = str, default='../../output/')
args = parser.parse_args()

class Evaluation:
    def __init__(self, path):
        self.path = path
        raw, pred, gold = self.load_pred(path)
        self.evaluate(raw, gold, pred)

    def evaluate(self, raw, gold, pred, ignCaps= True, verbose=False):
        cor = 0
        changed = 0
        total = 0

        if len(gold) != len(pred):
            error('Error: gold normalization contains a different numer of sentences(' + str(len(gold)) + ') compared to system output(' + str(len(pred)) + ')')

        # for sentRaw, sentGold, sentPred in zip(raw, gold, pred):
        #     if len(sentGold) != len(sentPred):
        #         err('Error: a sentence has a different length in you output, check the order of the sentences')
        TP = 0
        FP = 0
        FN = 0
        for wordRaw, wordGold, wordPred in zip(raw, gold, pred):
            if ignCaps:
                wordRaw = wordRaw.lower()
                wordGold = wordGold.lower()
                wordPred = wordPred.lower()
            if wordRaw == wordGold and wordPred!= wordRaw:
                FP += 1
            if wordRaw != wordGold and wordPred!= wordGold:
                FN += 1
            if wordRaw != wordGold and wordPred== wordGold:
                TP += 1
            if wordRaw != wordGold:
                changed += 1

            if wordGold == wordPred:
                cor += 1
            elif verbose:
                print(wordRaw, wordGold, wordPred)
            total += 1

        err = (TP - FP)/(TP+FN)
        accuracy = cor / total
        print('Accuracy:           {:.2f}'.format(accuracy * 100))
        print('ERR:                {:.2f}'.format(err * 100))


    def load_pred(self, word_file):
        """Loads data """
        raw_list = []
        pred_list = []
        gold_list = []
        with open(word_file, encoding = "utf-8", errors = "ignore") as f:
            lines = f.readlines()

            for line in lines:
                if line != "\n" and line != None:
                    raw, pred, gold = line.split(sep = "\n")[0].split(sep = "\t")
                    raw_list.append(raw)
                    pred_list.append(pred)
                    gold_list.append(gold)
        return raw_list, pred_list, gold_list

#Change the path as required
print("Scores")
print("____________________________________________________")
print("Simple Baseline 1 - LAI")
Evaluation(args.outputpath+"lai_test.txt")
print("____________________________________________________")
print("Simple Baseline 2 - MFR Base")
Evaluation(args.outputpath+"mfr_base_test.txt")
print("____________________________________________________")
print("Strong Baseline 1 - Char RNN")
Evaluation(args.outputpath+"test_pred_correct_order.txt")
print("____________________________________________________")
print("Extension 1 - MFR + Char RNN")
Evaluation(args.outputpath+"mfr_extension1_test.txt")
print("____________________________________________________")
print("Extension 2 - MFR + Augmented Data + Char RNN")
Evaluation(args.outputpath+"mfr_extension2_test.txt")
print("____________________________________________________")
print("Published Hybrid Model")
Evaluation(args.outputpath+"test_pred_theirs.txt")
print("____________________________________________________")
print("Hybrid Model + Augmented Data")
Evaluation(args.outputpath+"test_pred_ours.txt")
print("____________________________________________________")