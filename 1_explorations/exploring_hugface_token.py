from transformers import AutoTokenizer
from datasets import load_dataset


"""here we are loading a pretrained tokenizer and a dataset"""
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
dataset = load_dataset("rotten_tomatoes", split="train")

"""now we are trying to tokenize the dataset"""
# tokenized = tokenizer(dataset[0]["text"])
# print(dataset[0]["text"])
# print(tokenized)
"""De-comment to run it!"""

"""A faster way to tokenize the whole dataset: the map method"""
def tokenization(example):
    return tokenizer(example["text"])

dataset = dataset.map(tokenization, batched=True)
print(dataset[0])


"""Now set the type of your dataset make it compatible with your ML framework"""
dataset.set_format(type="torch", columns=["input_ids", "token_type_ids", "attention_mask", "label"])
print(dataset.format["type"])