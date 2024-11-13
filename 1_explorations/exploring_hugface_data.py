from datasets import load_dataset_builder

"""for this commands, we are trying to get some details about the dataset"""
# ds_builder = load_dataset_builder("rotten_tomatoes")
# print(ds_builder.info.description)
# print(ds_builder.info.features)
"""De-comment to run it!"""


"""to see the split names of a dataset"""
from datasets import load_dataset, get_dataset_split_names
# split_names = get_dataset_split_names("rotten_tomatoes")
# print(split_names)
"""De-comment to run it!"""""

"""Two ways loading dataset"""
# # now we are loading dataset from the builder
# dataset = load_dataset("rotten_tomatoes", split="train")
# # and if we don't use the split parameter, we will get the whole dataset with the type of dict
# detaset = load_dataset("rotten_tomatoes")
""""De-comment to run it!"""


"""for some dataset, it may contain many configurations, we need to select the one we want
otherwitse it will raise an error"""
from datasets import get_dataset_config_names
# config_names = get_dataset_config_names("PolyAI/minds14")
# print(config_names)
"""De-comment to run it!"""


"""now we are trying to play with the dataset, see what it looks like"""
"""Remember that the indexing order matters, you should use id before text or label"""
"""Slicing is supported"""
dataset = load_dataset("rotten_tomatoes", split="train")
id1 = dataset[0]
print(id1)

"""De-comment to run it!"""