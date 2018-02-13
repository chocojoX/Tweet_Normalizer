import os
import numpy as np
import time
import argparse

from normalizor import Normalizor


def run(input_path, output_path, tokenizer="tweet", punctuation=True):
    print "Loading the normalizer ..."
    t0 = time.time()
    normalizor = Normalizor(tokenizer=tokenizer, punctuation=punctuation)
    t1 = time.time()
    print "Time to load normalizer : %.1fs" %(t1-t0)
    lines = [line.rstrip('\n') for line in open(input_path)]
    with open(output_path, "w") as output_f:
        output_f.write("")
    for sentence in lines:
        corrected = normalizor.predict(sentence)
        with open(output_path, "a") as output_f:
            output_f.write(corrected + "\n")


if __name__=="__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input_dataset", default="toy_dataset.txt", help="Relative path to the input dataset")
    parser.add_argument("-o", "--output_dataset", default="toy_dataset_corrected.txt", help="Relative path to the file where to write the results")
    parser.add_argument("-t", "--tokenizer_type", default="tweet", help="Type of tokenizer to use, either -tweet- or -other- tweet option will use the nltk tokenizer for tweets. other will use a dummy tokenizer implemented in contextual.py")
    parser.add_argument("-p", "--punctuation", default=True, help="Wether or not to keep the punctuation in the output. Either way, the punctuation will be use in context analysis")

    args = parser.parse_args()
    input_path = args.input_dataset
    output_path = args.output_dataset
    tokenizer = args.tokenizer_type
    punctuation = args.punctuation

    run(input_path, output_path, tokenizer=tokenizer, punctuation=punctuation)
    import pdb; pdb.set_trace()
    # input_path = "C:\\Users\\Joseph\\Desktop\\Travail\\4A\\NLP\\TD3\\Tweet_Normalizer\\toy_dataset.txt"
    # output_path = "C:\\Users\\Joseph\\Desktop\\Travail\\4A\\NLP\\TD3\\Tweet_Normalizer\\toy_dataset_corrected.txt"
