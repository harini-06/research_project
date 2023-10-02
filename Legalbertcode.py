!pip install bertopic[visualization] --quiet
import numpy as np
import pandas as pd
from copy import deepcopy
from bertopic import BERTopic
from google.colab import drive
df = pd.read_csv("/content/drive/MyDrive/data/output53.csv")
df.head(3)
docs = list(df.loc[:, "text"].values)
docs[:474]
model = BERTopic(language="english")
topics, probs = model.fit_transform(docs)
model.get_topic_freq()
model.get_topic(0)
model.get_topic(1)
model.get_topic(2)
model.visualize_barchart()




