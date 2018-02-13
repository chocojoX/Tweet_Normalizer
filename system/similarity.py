import numpy as np


class Corrector(object):
    def __init__(self, word2index=None, index2word=None):
        self.word2index = word2index
        self.index2word = index2word
        self.default_dist = 10  # Default distance between two words (if their distance was not completely computed, this distance will be attributed by default)

    def compute_distance(self, word1, word2, max_dist=None):
        n = len(word1)
        p = len(word2)
        distance_matrix = np.zeros((n+1, p+1))
        for i in range(n+1):
            distance_matrix[i, 0] = i
        for j in range(p+1):
            distance_matrix[0,j] = j

        for i in range(0, n):
            for j in range(0, p):
                if word1[i]==word2[j]:
                    cost = 0
                else:
                    cost = 1
                distance_matrix[i+1, j+1] = np.min([distance_matrix[i, j+1]+1, distance_matrix[i+1, j]+1, distance_matrix[i, j]+cost])
            if max_dist is not None and np.min(distance_matrix[i+1,:])>max_dist:
                # The distance between the two words is too high, we therefore shorten the computation and return the default distance value.
                return self.default_dist
        return distance_matrix[-1,-1]


    def get_most_similar_word(self, word, word_list=None):
        if word_list is None:
            word_list = self.index2word

        min_error = len(word)+2
        best_word = ""
        for word2 in word_list:
            dist = self.compute_distance(word, word2)
            if dist<min_error:
                min_error = dist
                best_word = word2
        return best_word


    def get_similarity(self, word, max_dist=3, word_list=None):
        # max_dist is the upper bound for acceptable distances.
        # Fixing a small max_hist will fasten the compute distance algorithm but will lose accurcy for distances strictly above 2
        if word_list is None:
            word_list = self.index2word
        similarities=[]
        for word2 in word_list:
            if len(word2)-len(word)>1 or len(word2)-len(word)<-2 or word2[0]!=word[0]:
                # If length of words are too different or their first letters are different
                similarities.append(10)
            else:
                similarities.append(self.compute_distance(word, word2, max_dist=2))
        return similarities


    def create_similar_words(self, word):
        candidates = [word]
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
        # Creating words at distance 1
        for i in range(len(word)):
            for letter in alphabet:
                word2 = word[:i] + alphabet[i] + word[i:]
                candidates.append(word2)
            word2 = word[:i]+word[(i+1):]
            candidates.append(word2)

        # Creating words at distance (almost always) 2
        for word2 in candidates:
            for i in range(len(word2)):
                for letter in alphabet:
                    word3 = word2[:i] + alphabet[i] + word2[i:]
                    candidates.append(word3)
                word3 = word2[:i]+word2[(i+1):]
                candidates.append(word3)
        return candidates



if __name__=="__main__":
    word1 = "some"
    word2 = "som"
    cor = Corrector()
    print "Theoretical distance between %s and %s : %i" %(word1, word2, 1)
    print "Computed distance : %i"%cor.compute_distance(word1, word2)
