import pandas as pd
import os

filepath = os.path.join(r'E:\Research Project\Reading pkl file\\')
df = pd.read_html(filepath + "newfile.csv")

df['year'] = df['celex'].str.slice(start=1, stop=5)
df['summary'] = df['summary'].str.replace("[\[\]\']", "")
df1 = pd.DataFrame(df.summary.str.split(',', expand=True).values)

df['text'] = df['text'].str.replace("\n\t", "")
df2 = pd.DataFrame(df.text.str.split(',', expand=True).values)

df3 = pd.concat([df, df1, df2], axis=1)

df3.to_csv(filepath+"output.csv", index=False)