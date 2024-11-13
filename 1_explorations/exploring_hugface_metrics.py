from datasets import list_metrics

"""first, we need to know what metrics are available"""
metrics_list = list_metrics()
print(len(metrics_list))
print(metrics_list)
"""De-comment to run it!"""


"""now we are trying to load a metric"""
from datasets import load_metric
matric = load_metric('glue', 'mrpc')
# This will load the matric associated with the MRPC dataset from the Glue benchmark

"""Before you begin using a Metric object, you should get to know it a little better. 
As with a dataset, you can return some basic information about a metric. 
For example, access the inputs_description parameter in datasets.MetricInfo to get 
more information about a metrics expected input format and some usage examples"""
print(matric.info.inputs_description)
"""De-comment to run it!"""

"""Once we have a metric, we can use it to compute the metric score for a given prediction and reference"""
# # Assume that we have a model already
# model_predict = model(model_inputs)
# acc = matric.compute(predictions=model_predict, references=gold_references)
"""De-comment to run it!"""