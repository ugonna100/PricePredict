import json
import pickle
import time
import string
import numpy as np
from keras.preprocessing.sequence import pad_sequences


# Storage dictionaries
lookUpTable_id_item = {}
lookUpTable_item_id = {}
word_to_idx = {}
max_len = 0
# Starting Timers
start = time.clock()

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

with open('./items.json') as items:
    items_dict = json.loads(items.read())
    print(len(items_dict['snapshot']))
    with open('./item-prices.json') as prices:
        prices_dict = json.loads(prices.read())
        print(len(prices_dict['snapshot']))
        if len(prices_dict['snapshot']) == len(items_dict['snapshot']):
            print('Files match in size, safe to proceed.')
        else:
            print('Warning! Files size mismatch lookup table is inaccurate!')
            exit()
        for item in items_dict['snapshot']:
            id = item["itemId"]["itemCode"]
            description = item["longDescription"]["values"][0]["value"]
            length = len(cleaner(description).split(' '))
            if length > max_len:
                max_len = length
            parts = cleaner(description).split(' ')
            for part in parts:
                try:
                    word_to_idx[part]
                except Exception:
                    length = len(word_to_idx.keys())
                    # print('Adding to lookup:', part)
                    word_to_idx[part] = length + 1
            for price in prices_dict['snapshot']:
                if id == price['priceId']['itemCode']:
                    try:
                        lookUpTable_id_item[id]
                    except KeyError:
                        # print('Adding:',id)
                        lookUpTable_id_item[id] = {'description':description, 'price':price['price'], 'category':item['merchandiseCategory']['nodeId']}
                        lookUpTable_item_id[description] = {'id':id, 'price':price['price'], 'category':item['merchandiseCategory']['nodeId']}
end = time.clock()
print(end - start, 'seconds.')
# Object saver
save_object(lookUpTable_id_item,'lookUp_ID-to-Item.pkl')
save_object(lookUpTable_item_id,'lookUp_Item-to-ID.pkl')

with open('Dataset.csv','w') as out:
    print('Starting dataset file')
    out.write('id,description,price,category\n')
    for id in lookUpTable_id_item.keys():
        row = ''
        place = 0
        for key in lookUpTable_id_item[id].keys():
            if place > 0:
                row += ','
            place += 1
            row += "'" + str(lookUpTable_id_item[id][key]) + "'"
        row += '\n'
        # print(row)
        out.write(row)
    out.close()

# inp = input('Test Conversion system:')
# row = '['
# for word in cleaner(inp).split(' '):
#     spacer = ''
#     if len(str(row)) > 1:
#         spacer = ', '
#     try:
#         row = str(row) + spacer + str(word_to_idx[str(word)])
#     except KeyError:
#         row = str(row) + spacer + '0'
# length = len(cleaner(inp.split(' ')))
# diff = 0
# if max_len > length:
#     diff = max_len - length
# spacer = ','
# print("Difference", diff)
# while diff > 0:
#     row = str(row) + str(spacer) + '0'
#     diff -= 1
# row = str(row) + ']'
# print(row)
validation = []
training = []
with open('MR_Dataset.csv','w') as out:
    print('Starting MR dataset file')
    #out.write('description,price\n')
    for id in lookUpTable_id_item.keys():
        valids = []
        trains = []
        row = ''
        spacer = ''
        valid = lookUpTable_id_item[id]['price']
        length = len(cleaner(lookUpTable_id_item[id]['description']).split(' '))
        for value in cleaner(lookUpTable_id_item[id]['description']).split(' '):
            #trains.append(value)
            try:
                target = word_to_idx[value]
            except KeyError:
                target = 0
            trains.append(target)
        # print(row)
        out.write(str(row))
        valids.append(valid)
        validation.append(valids)
        print(valids)
        training.append(trains)
        print(trains)
    print(numpy_fillna(np.array(training)))
    training = numpy_fillna(np.array(training))
    print(numpy_fillna(np.array(validation)))
    validation = numpy_fillna(np.array(validation))
    out.close()
print('Max Length:',max_len)
save_object(training,'training.pkl')
save_object(validation,'validation.pkl')
save_object(word_to_idx,'word2idx.pkl')