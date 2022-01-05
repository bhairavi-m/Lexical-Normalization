import argparse
parser = argparse.ArgumentParser("path")
parser.add_argument('--path',type = str, default='../../data/')
parser.add_argument('--outputpath',type = str, default='../../output/')
args = parser.parse_args()
class LAI:
    def __init__(self,path):
        self.path = path
        self.simple_baseline(self.path)
    def simple_baseline(self, word_file):
        raw = []
        gold = []
        pred = []
        with open(word_file, encoding = "utf-8", errors = "ignore") as f:
            lines = f.readlines()
            for line in lines:
                if line != "\n":
                    first, second = line.split(sep = "\n")[0].split(sep = "\t")
                    raw.append(first)
                    gold.append(second)
                    pred.append(first)
                else:
                    raw.append("\n")
                    gold.append("\n")
                    pred.append("\n")
        with open(args.outputpath+"lai_test.txt", "a") as a_file:
            for i in range(len(raw)):
                if raw[i]!="\n":
                    a_file.write(raw[i]+"\t"+ pred[i] + "\t"+ gold[i] + "\n")
                else:
                    a_file.write("\n")

class Frequency:
    def __init__(self,train_path, test_base_path, test_extension_path):
        self.train_path = train_path
        self.test_base_path = test_base_path
        self.test_extension_path = test_extension_path
        mapping = self.frequency_mapping(self.train_path)
        self.freq_baseline(mapping,self.test_base_path)
        self.freq_baseline_extension(mapping, self.test_extension_path)

    def frequency_mapping(self, word_file):
        main_mapping = {}
        with open(word_file, encoding = "utf-8", errors = "ignore") as f:
            lines = f.readlines()
            for line in lines:
                if line != "\n":
                    first, second = line.split(sep = "\n")[0].split(sep = "\t")
                    if first in main_mapping:
                        if second in main_mapping[first]:
                            main_mapping[first][second] += 1
                        else:
                            main_mapping[first][second] = 1
                    else:
                        main_mapping[first] = {second:1}
        return main_mapping

    def freq_baseline(self, freq_dictionary, word_file):
        raw = []
        gold = []
        pred = []
        with open(word_file, encoding = "utf-8", errors = "ignore") as f:
            lines = f.readlines()
            for line in lines:
                if line != "\n":
                    first, second = line.split(sep = "\n")[0].split(sep = "\t")
                    raw.append(first)
                    gold.append(second)
                    if (first in freq_dictionary):
                        pred.append(max(freq_dictionary[first], key=freq_dictionary[first].get))
                    else:
                        pred.append(first)
                else:
                    raw.append("\n")
                    gold.append("\n")
                    pred.append("\n")

        with open(args.outputpath+"mfr_base_test.txt", "a") as a_file:

            for i in range(len(raw)):
                if raw[i]!="\n":
                    a_file.write(raw[i]+"\t"+ pred[i] + "\t"+ gold[i] +"\n")
                else:
                    a_file.write("\n")

    def freq_baseline_extension(self, freq_dictionary, word_file):
        raw = []
        gold = []
        pred = []
        with open(word_file, encoding = "utf-8", errors = "ignore") as f:
            lines = f.readlines()
            for line in lines:
                if line != "\n":
                    first, second, third = line.split(sep = "\n")[0].split(sep = "\t")

                    raw.append(first)
                    gold.append(third)
                    if (first in freq_dictionary):
                        pred.append(max(freq_dictionary[first], key=freq_dictionary[first].get))
                    else:
                        pred.append(second)
                else:
                    raw.append("\n")
                    gold.append("\n")
                    pred.append("\n")

        if word_file == args.outputpath+"test_pred_correct_order.txt":
            with open(args.outputpath+"mfr_extension1_test.txt", "a") as a_file:
                for i in range(len(raw)):
                    if raw[i]!="\n":
                        a_file.write(raw[i]+"\t"+ pred[i] + "\t"+ gold[i]+ "\n")
                    else:
                        a_file.write("\n")

        elif word_file == args.outputpath+"test_pred_ours.txt":
            with open(args.outputpath+"mfr_extension2_test.txt", "a") as a_file:
                for i in range(len(raw)):
                    if raw[i]!="\n":
                        a_file.write(raw[i]+"\t"+ pred[i] + "\t"+ gold[i]+ "\n")
                    else:
                        a_file.write("\n")



LAI(args.path+"test.txt")
Frequency(args.path+"train.txt",args.path+"test.txt",args.outputpath+"test_pred_correct_order.txt")
Frequency(args.path+"train.txt",args.path+"test.txt",args.outputpath+"test_pred_ours.txt")
