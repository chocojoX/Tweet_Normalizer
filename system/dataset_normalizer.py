import os
import numpy as np
import time

from normalizor import Normalizor


def run(input_path, output_path):
    print "Loading the normalizer ..."
    t0 = time.time()
    normalizor = Normalizor()
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
    input_path = "C:\\Users\\Joseph\\Desktop\\Travail\\4A\\NLP\\TD3\\toy_dataset.txt"
    output_path = "C:\\Users\\Joseph\\Desktop\\Travail\\4A\\NLP\\TD3\\toy_dataset_corrected.txt"
    run(input_path, output_path)
