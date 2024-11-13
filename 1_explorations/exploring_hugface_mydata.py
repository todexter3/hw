"""loading training data from Data/train.json"""

import json

path_lap = "laptop_data/"
path_res = "res_data/"

# read the json file
with open(path_lap + 'train.json') as f:
    train_data = json.load(f)
    
with open(path_lap + 'test.json') as f:
    test_data = json.load(f)



"""create a dataset using the dict"""
"""the text is the term and sentences, while label is the polarity"""
from datasets import Dataset

def get_dict(dataset):
    dic = {}
    list_sentence = []
    list_label = []
    for data in dataset.values():
        list_sentence.append([data['term'] , data['sentence']])
        lable = 0
        if data['polarity'] == 'positive':
            lable = 1
        list_label.append(lable) 
        
    dic['text'] = list_sentence
    dic['label'] = list_label
    return dic
    
train = get_dict(train_data)
test = get_dict(test_data)    
train_dataset = Dataset.from_dict(train)
test_dataset = Dataset.from_dict(test)

# combine the train and test dataset to a DatasetDict
from datasets import DatasetDict
dataset_dict = DatasetDict({'train': train_dataset, 'test': test_dataset})
print(dataset_dict['test'][0])
print(dataset_dict)