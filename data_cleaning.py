import pandas as pd
import os
filepath = os.path.join(r'F:\SRH Academics\\')
df = pd.read_csv(filepath + "newfile_data.csv")
df['year'] = df['celex'].str.slice(start=1, stop=5)
df0 = df['year']
df['summary'] = df['summary'].str.replace("\n", "")
df['summary'] = df['summary'].str.replace("\t", "")
df['summary'] = df['summary'].str.replace("the", "")
df['summary'] = df['summary'].str.replace("of", "")
df['summary'] = df['summary'].str.replace("and", "")
df['summary'] = df['summary'].str.replace("to", "")
df['summary'] = df['summary'].str.replace("in", "")
df['summary'] = df['summary'].str.replace("for", "")
df['summary'] = df['summary'].str.replace("shall", "")
df['summary'] = df['summary'].str.replace("be", "")
df['summary'] = df['summary'].str.replace("with", "")
df['summary'] = df['summary'].str.replace("The", "")
df['summary'] = df['summary'].str.replace("that", "")
df['summary'] = df['summary'].str.replace("as", "")
df['summary'] = df['summary'].str.replace("a", "")
df['summary'] = df['summary'].str.replace("on", "")
df['summary'] = df['summary'].str.replace("it", "")
df['summary'] = df['summary'].str.replace("should", "")
df['summary'] = df['summary'].str.replace("from", "")
df['summary'] = df['summary'].str.replace("was", "")
df['summary'] = df['summary'].str.replace("by", "")
df['summary'] = df['summary'].str.replace("this", "")
df['summary'] = df['summary'].str.replace("is", "")
df['summary'] = df['summary'].str.replace("which", "")
df['summary'] = df['summary'].str.replace("or", "")
df['summary'] = df['summary'].str.replace("not", "")
df1 = df['summary']
df['text'] = df['text'].str.replace("\n", "")
df['text'] = df['text'].str.replace("\t", "")
df['text'] = df['text'].str.replace("the", "")
df['text'] = df['text'].str.replace("of", "")
df['text'] = df['text'].str.replace("and", "")
df['text'] = df['text'].str.replace("to", "")
df['text'] = df['text'].str.replace("in", "")
df['text'] = df['text'].str.replace("for", "")
df['text'] = df['text'].str.replace("shall", "")
df['text'] = df['text'].str.replace("be", "")
df['text'] = df['text'].str.replace("with", "")
df['text'] = df['text'].str.replace("The", "")
df['text'] = df['text'].str.replace("that", "")
df['text'] = df['text'].str.replace("as", "")
df['text'] = df['text'].str.replace("a", "")
df['text'] = df['text'].str.replace("on", "")
df['text'] = df['text'].str.replace("it", "")
df['text'] = df['text'].str.replace("should", "")
df['text'] = df['text'].str.replace("from", "")
df['text'] = df['text'].str.replace("was", "")
df['text'] = df['text'].str.replace("by", "")
df['text'] = df['text'].str.replace("this", "")
df['text'] = df['text'].str.replace("is", "")
df['text'] = df['text'].str.replace("which", "")
df['text'] = df['text'].str.replace("or", "")
df['text'] = df['text'].str.replace("not", "")
df2 = df['text']
df3 = pd.concat([df0, df1, df2], axis=1)
df3.to_csv(filepath+"output53.csv", index=False)