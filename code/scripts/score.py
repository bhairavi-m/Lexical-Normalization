from os import error
import argparse

parser = argparse.ArgumentParser("path")
parser.add_argument("--outputpath", type=str, default="../../output/")
args = parser.parse_args()


class Evaluation:
    """
    Evaluates a model designed to form a Lexical Normalization system.

    Methods
    -------
    evaluate(self, raw, gold, pred, ignCaps=True, verbose=False)
        Calculates the Error Reduction Rate and Accuracy of the model

    load_pred(self, word_file)
        Reads the file that contains the prediction
    """
    def __init__(self, path):
        """
        Parameters
        ----------
        path : str
            The path of the file that contains the predictions
        """
        self.path = path
        raw, pred, gold = self.load_pred(path)
        self.evaluate(raw, gold, pred)


    def load_pred(self, word_file):
        """
        Reads the file that contains the prediction

        Parameters
        ----------
        word_file : str
            The path of the file that contains the predictions

        Returns
        -------
        list
            Of raw, gold and predicted words
        """
        raw_list = []
        pred_list = []
        gold_list = []
        with open(word_file, encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()

            for line in lines:
                if line != "\n" and line != None:
                    raw, pred, gold = line.split(sep="\n")[0].split(sep="\t")
                    raw_list.append(raw)
                    pred_list.append(pred)
                    gold_list.append(gold)
        return raw_list, pred_list, gold_list

    def evaluate(self, raw, gold, pred, ignCaps=True, verbose=False):
        """
        Calculates the Error Reduction Rate and Accuracy of the model

        Parameters
        ----------
        raw : list
            List of all the raw words
        gold : list
            List of all the gold words
        preds : list
            List of all the predicted words

        Returns
        -------
        None
        """
        cor = 0
        total = 0

        if len(gold) != len(pred):
            error(
                "Error: gold normalization contains a different number of sentences("
                + str(len(gold))
                + ") compared to system output("
                + str(len(pred))
                + ")"
            )

        TP = 0
        FP = 0
        FN = 0
        for wordRaw, wordGold, wordPred in zip(raw, gold, pred):
            if ignCaps:
                wordRaw = wordRaw.lower()
                wordGold = wordGold.lower()
                wordPred = wordPred.lower()
            if wordRaw == wordGold and wordPred != wordRaw:
                FP += 1
            if wordRaw != wordGold and wordPred != wordGold:
                FN += 1
            if wordRaw != wordGold and wordPred == wordGold:
                TP += 1

            if wordGold == wordPred:
                cor += 1
            elif verbose:
                print(wordRaw, wordGold, wordPred)
            total += 1

        err = (TP - FP) / (TP + FN) #Word level accuracy would be equal to the % of words that are not normalized, and ERR is 0.0.
        accuracy = cor / total
        print("Accuracy:           {:.2f}".format(accuracy * 100))
        print("ERR:                {:.2f}".format(err * 100))

if __name__ == '__main__':
    # Change the path as required
    print("Scores")
    print("____________________________________________________")
    print("Simple Baseline 1 - LAI")
    Evaluation(args.outputpath + "lai_test.txt")
    print("____________________________________________________")
    print("Simple Baseline 2 - MFR Base")
    Evaluation(args.outputpath + "mfr_base_test.txt")
    print("____________________________________________________")
    print("Strong Baseline 1 - Char RNN")
    Evaluation(args.outputpath + "test_pred_correct_order.txt")
    print("____________________________________________________")
    print("Extension 1 - MFR + Char RNN")
    Evaluation(args.outputpath + "mfr_extension1_test.txt")
    print("____________________________________________________")
    print("Extension 2 - MFR + Augmented Data + Char RNN")
    Evaluation(args.outputpath + "mfr_extension2_test.txt")
    print("____________________________________________________")
    print("Published Hybrid Model")
    Evaluation(args.outputpath + "test_pred_theirs.txt")
    print("____________________________________________________")
    print("Hybrid Model + Augmented Data")
    Evaluation(args.outputpath + "test_pred_ours.txt")
    print("____________________________________________________")
