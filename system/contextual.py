import numpy as np
from context2vec.common import model_reader
import os
import re


class Contextualizer(object):
    def __init__(self):
        self.read_model()

    def read_model(self):
        model_param_file = "context2vec.mscc.model.package/context2vec.mscc.model.params"
        reader = model_reader.ModelReader(model_param_file)
        self.w = reader.w
        self.word2index = reader.word2index
        self.index2word = reader.index2word
        self.model = reader.model


    def parse_input(self, line):
        sent = line.strip().split()
        return sent


    def predict(self, sent, target_pos=None):
        if target_pos == None:
            raise ParseException("Can't find the target position.")

        if len(sent) > 1:
            context_v = self.model.context2vec(sent, target_pos)
            context_v = context_v / np.sqrt((context_v * context_v).sum())
        else:
            context_v = None

        target_v=None
        if target_v is not None and context_v is not None:
            similarity = mult_sim(w, target_v, context_v)
        else:
            if target_v is not None:
                v = target_v
            elif context_v is not None:
                v = context_v
            else:
                raise ParseException("Can't find a target nor context.")
            similarity = (self.w.dot(v)+1.0)/2 # Cosine similarity can be negative, mapping similarity to [0,1]

        # count = 0; n_result=10
        # for i in (-similarity).argsort():
        #     if np.isnan(similarity[i]):
        #         continue
        #     print('{0}: {1}'.format(self.index2word[i], similarity[i]))
        #     count += 1
        #     if count == n_result:
        #         break
        return -similarity
    # except EOFError:
    #     break
    # except ParseException as e:
    #     print "ParseException: {}".format(e)
    # except Exception:
    #     exc_type, exc_value, exc_traceback = sys.exc_info()
    #     print "*** print_tb:"
    #     traceback.print_tb(exc_traceback, limit=1, file=sys.stdout)
    #     print "*** print_exception:"
    #     traceback.print_exception(exc_type, exc_value, exc_traceback, limit=2, file=sys.stdout)


if __name__=="__main__":

    context2vecdir =  os.environ['CONTEXT2VECDIR']
    contextualizer = Contextualizer()
    line = "This is a nice book"
    sent = contextualizer.parse_input(line)
    print sent
    contextualizer.predict(sent, target_pos=3)

    import pdb; pdb.set_trace()
    # model_param_file = "context2vec.mscc.model.package/context2vec.mscc.model.params"
    # model_reader = model_reader.ModelReader(model_param_file)
    # w = model_reader.w
    # word2index = model_reader.word2index
    # index2word = model_reader.index2word
    # model = model_reader.model
