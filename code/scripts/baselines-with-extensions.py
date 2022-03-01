import argparse

parser = argparse.ArgumentParser("path")
parser.add_argument("--path", type=str, default="../../data/")
parser.add_argument("--outputpath", type=str, default="../../output/")
args = parser.parse_args()


class LAI:
    """
    Leave-As-Is Baseline: Simply uses the input as output.

    Methods
    -------
    simple_baseline(self, word_file)
        Uses the training data to compute the output to be the same
    """
    def __init__(self, path):
        """
        Parameters
        ----------
        path : str
            The path of the file that contains the predictions
        """
        self.path = path
        self.simple_baseline(self.path)

    def simple_baseline(self, word_file):
        """
        Reads the training data and generates a map that counts the frequency of each word's normalized form

        Parameters
        ----------
        word_file : str
            The path of the file that contains the training data

        Returns
        -------
        dict
            Of the gold label counts of each word in the training data
        """
        raw = []
        gold = []
        pred = []
        with open(word_file, encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()
            for line in lines:
                if line != "\n":
                    first, second = line.split(sep="\n")[0].split(sep="\t")
                    raw.append(first)
                    gold.append(second)
                    pred.append(first)
                else:
                    raw.append("\n")
                    gold.append("\n")
                    pred.append("\n")
        with open(args.outputpath + "lai_test.txt", "a") as a_file:
            for i in range(len(raw)):
                if raw[i] != "\n":
                    a_file.write(raw[i] + "\t" + pred[i] + "\t" + gold[i] + "\n")
                else:
                    a_file.write("\n")


class Frequency:
    """
    Uses the most frequent replacement based on the training data.

    Methods
    -------
    def frequency_mapping(self, word_file)
        Calculates the Error Reduction Rate and Accuracy of the model

    load_pred(self, word_file)
        Reads the file that contains the prediction
    """

    def __init__(self, train_path, test_base_path, test_extension_path):
        """
        Parameters
        ----------
        train_path : str
            The path of the file that contains the training data
        test_base_path : str
            The path of the file that contains the testing data
        test_extension_path : str
            The path of the file that contains the predictions of the Char RNN
        """
        self.train_path = train_path
        self.test_base_path = test_base_path
        self.test_extension_path = test_extension_path
        mapping = self.frequency_mapping(self.train_path)
        self.freq_baseline(mapping, self.test_base_path)
        self.freq_baseline_extension(mapping, self.test_extension_path)

    def frequency_mapping(self, word_file):
        """
        Reads the training data and generates a map that counts the frequency of each word's normalized form

        Parameters
        ----------
        word_file : str
            The path of the file that contains the predictions

        Returns
        -------
        dict
            Of the gold label counts of each word in the training data
        """
        main_mapping = {}
        with open(word_file, encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()
            for line in lines:
                if line != "\n":
                    first, second = line.split(sep="\n")[0].split(sep="\t")
                    if first in main_mapping:
                        if second in main_mapping[first]:
                            main_mapping[first][second] += 1
                        else:
                            main_mapping[first][second] = 1
                    else:
                        main_mapping[first] = {second: 1}
        return main_mapping

    def freq_baseline(self, freq_dictionary, word_file):
        """
        Uses the gold token frequency mapped from the training data. If the input word is not present in the training data, it returns the input word.

        Parameters
        ----------
        freq_dictionary : dict
            Contains the gold label counts of each word in the training data

        word_file : str
            The path of the file that contains the predictions

        Returns
        -------
        None
        """

        raw = []
        gold = []
        pred = []
        with open(word_file, encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()
            for line in lines:
                if line != "\n":
                    first, second = line.split(sep="\n")[0].split(sep="\t")
                    raw.append(first)
                    gold.append(second)
                    if first in freq_dictionary:
                        pred.append(
                            max(freq_dictionary[first], key=freq_dictionary[first].get)
                        )
                    else:
                        pred.append(first)
                else:
                    raw.append("\n")
                    gold.append("\n")
                    pred.append("\n")

        with open(args.outputpath + "mfr_base_test.txt", "a") as a_file:

            for i in range(len(raw)):
                if raw[i] != "\n":
                    a_file.write(raw[i] + "\t" + pred[i] + "\t" + gold[i] + "\n")
                else:
                    a_file.write("\n")

    def freq_baseline_extension(self, freq_dictionary, word_file):
        """
        Uses the prediction file generated by the Char RNN. If the input word is not present in the training data, it returns the prediction generated by the Char RNN.

        Parameters
        ----------
        freq_dictionary : dict
            Contains the gold label counts of each word in the training data

        word_file : str
            The path of the file that contains the predictions

        Returns
        -------
        None
        """
        raw = []
        gold = []
        pred = []
        with open(word_file, encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()
            for line in lines:
                if line != "\n":
                    first, second, third = line.split(sep="\n")[0].split(sep="\t")

                    raw.append(first)
                    gold.append(third)
                    if first in freq_dictionary:
                        pred.append(
                            max(freq_dictionary[first], key=freq_dictionary[first].get)
                        )
                    else:
                        pred.append(second)
                else:
                    raw.append("\n")
                    gold.append("\n")
                    pred.append("\n")

        if word_file == args.outputpath + "test_pred_correct_order.txt":
            with open(args.outputpath + "mfr_extension1_test.txt", "a") as a_file:
                for i in range(len(raw)):
                    if raw[i] != "\n":
                        a_file.write(raw[i] + "\t" + pred[i] + "\t" + gold[i] + "\n")
                    else:
                        a_file.write("\n")

        elif word_file == args.outputpath + "test_pred_ours.txt":
            with open(args.outputpath + "mfr_extension2_test.txt", "a") as a_file:
                for i in range(len(raw)):
                    if raw[i] != "\n":
                        a_file.write(raw[i] + "\t" + pred[i] + "\t" + gold[i] + "\n")
                    else:
                        a_file.write("\n")


if __name__ == "__main__":
    LAI(args.path + "test.txt")
    Frequency(
        args.path + "train.txt",
        args.path + "test.txt",
        args.outputpath + "test_pred_correct_order.txt",
    )
    Frequency(
        args.path + "train.txt",
        args.path + "test.txt",
        args.outputpath + "test_pred_ours.txt",
    )
