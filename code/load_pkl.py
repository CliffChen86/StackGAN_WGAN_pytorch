import pickle
import numpy as np 
data_dir = ('../data/coco/train')
embedding_type = 'cnn-rnn'
def load_embedding(data_dir, embedding_type):
    if embedding_type == 'cnn-rnn':
        embedding_filename = '/char-CNN-RNN-embeddings.pickle'
    elif embedding_type == 'cnn-gru':
        embedding_filename = '/char-CNN-GRU-embeddings.pickle'
    elif embedding_type == 'skip-thought':
        embedding_filename = '/skip-thought-embeddings.pickle'

    with open(data_dir + embedding_filename, 'rb') as f:
        embeddings = pickle.load(f)
        embeddings = np.array(embeddings)
        # embedding_shape = [embeddings.shape[-1]]
        print('embeddings: ', embeddings.shape)
    return embeddings

    def load_filenames(self, data_dir):
        filepath = os.path.join(data_dir, 'filenames.pickle')
        with open(filepath, 'rb') as f:
            filenames = pickle.load(f)
        print('Load filenames from: %s (%d)' % (filepath, len(filenames)))
        return filenames

if __name__ == '__main__':
    embedding_type = 'cnn-rnn'
    embeddings = load_embedding(data_dir,embedding_type)