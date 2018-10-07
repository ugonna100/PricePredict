import sklearn
from sklearn.ensemble import GradientBoostingRegressor
import pickle
import numpy
import pandas as pd
import numpy as np
import string
from sklearn.model_selection import cross_val_score

def numpy_fillna(data):
    # Get lengths of each row of data
    lens = np.array([len(i) for i in data])

    # Mask of valid places in each row
    mask = np.arange(lens.max()) < lens[:,None]

    # Setup output array and put elements from data into masked positions
    out = np.zeros(mask.shape, dtype=data.dtype)
    out[mask] = np.concatenate(data)
    return out

# saved to file
def save_object(obj, filename):
    with open(filename, 'wb') as output:  # Overwrites any existing file.
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)

# string cleaner
def cleaner(sentence):
    tr = str.maketrans("", "", string.punctuation)
    work = str(sentence).translate(tr).lower()
    work = str(work).replace('(','').replace(')','').replace('%','').strip().replace('  ',' ').replace('®','')
    return work

#Loading training objects
infile = open('./training.pkl','rb')

train = pickle.load(infile)
train = pd.DataFrame(train)
infile.close()
infile = open('./validation.pkl','rb')
validation = pickle.load(infile)
validation = pd.DataFrame(validation)
infile.close()
word_to_idx = open('./word2idx.pkl','rb')
word_to_idx = pickle.load(word_to_idx)

print('Loaded Files')

#Preparing regressor.

model = GradientBoostingRegressor(n_estimators=17525, learning_rate=0.75)
# print(train)
# print(np.ravel(numpy.asarray(validation)))
model.fit(train, np.ravel(numpy.asarray(validation)))
scores = cross_val_score(model, train, np.ravel(numpy.asarray(validation)), cv=5)
print(abs(scores.mean()))

def predict(text=None):
    inp = text
    if inp:
        pass
    else:
        inp = input('Test Conversion system:')
    value = []
    for word in cleaner(inp).split(' '):
        try:
            item = word_to_idx[str(word)]
            value.append(item)
        except KeyError:
            value.append(0)
    while len(value) < 22:
        value.append(0)
    
    print(value)
    print(model.predict([value[0:22]]))
predict()