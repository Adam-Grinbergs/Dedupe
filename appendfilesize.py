import pandas as pd
import os

size = []

df = pd.read_csv('duplicates_smol.csv')
print(df.describe())
for key, value in df.iteritems():
    for value in value.values:
        try:
            size.append([value, os.path.getsize(value)])
        except:
            size.append([value, "failure"])

df2 = pd.DataFrame(size)

df3 = pd.merge(df, df2, left_index = True, right_index = True)
df3.to_csv('file_sizes.csv')

