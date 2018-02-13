import numpy as np
from contextual import Contextualizer
from similarity import Corrector
import string
from nltk.tokenize.casual import TweetTokenizer
import time


class Normalizor(object):
    def __init__(self):
        self.contextualizer = Contextualizer()
        self.corrector = Corrector(word2index=self.contextualizer.word2index, index2word=self.contextualizer.index2word)


    def predict(self, sentence):
        sentence = sentence.lower()
        import pdb; pdb.set_trace()
        sentence = sentence.translate(None, string.punctuation)
        list_of_words = self.contextualizer.parse_input(sentence)
        candidate_corrected = []
        for i, word in enumerate(list_of_words):
            context_predictions = np.exp(-20*np.array(self.contextualizer.predict(list_of_words, target_pos=i)))
            similarity = np.exp(-np.array(self.corrector.get_similarity(word)))
            final_score = similarity*context_predictions

            corrected_word = self.contextualizer.index2word[np.argmax(final_score)]
            # Changing the initial word in the sentence so that its correction can help the contextualizer
            list_of_words[i] = corrected_word
            candidate_corrected.append(corrected_word)
        print " ".join(candidate_corrected)
        return " ".join(candidate_corrected)


if __name__=="__main__":
    t0 = time.time()
    normalizor = Normalizor()
    t1=time.time()
    print "Time to initialize Normalizor : %.1fs" %(t1-t0)
    correction = normalizor.corrector.get_similarity("common")
    t2 = time.time()
    print "Time to correct word : %.1fs"%(t2-t1)
    predicted = normalizor.predict("An acress whearing a hatt is walking on the bridge acress the river.")
    import pdb; pdb.set_trace()
