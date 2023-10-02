import pandas as pd
import os
filepath = os.path.join(r'E:\Research Project\Reading pkl file\\')
df = pd.read_csv(filepath + "newfile_data.csv")
df['year'] = df['celex'].str.slice(start=1, stop=5)
df0 = df['year']
df['summary'] = df['summary'].str.replace("\n", "")
df['summary'] = df['summary'].str.replace("\t", "")
df1 = df['summary']
df['text'] = df['text'].str.replace("\n", "")
df['text'] = df['text'].str.replace("\t", "")
df2 = df['text']
df3 = pd.concat([df0, df1, df2], axis=1)
df3.to_html(filepath+"output1.html", index=False)

