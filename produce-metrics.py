import random
from mlflow import log_metric
from random import choice 

metrics = ["cpu", "memory", "disk"]
percentages = [i for i in range(0, 100)]  # 0 to 100 in steps of 5
for i in range(40):
    log_metric(choice(metrics), choice(percentages))

