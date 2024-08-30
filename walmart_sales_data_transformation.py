"""
M5 Walmart Sales Data Analysis

Transforming the "sales_train_validation.csv" dataset: original data table has
over a thousand columns, most of them representing days (d_1, d_2, ..., d_1913).
Loading a table with this many columns into SQL is manually intensive, so this
script transforms the data into a table with 7 columns while retaining the
same information. This does mean having many more rows, but this is what I would
have done with SQL so that the data is in the proper format for Power BI.
"""
import pandas as pd

df = pd.read_csv("C:/Users/yeons/Documents/MSDSO/PROJECTS/M5/m5-data/sales_train_validation.csv")
df_id_cols = df[['item_id', 'dept_id', 'cat_id', 'store_id', 'state_id']]
d_1_index = list(df.columns).index('d_1')
days = df.columns[d_1_index:]

for day in days:
    df_temp = pd.concat([df_id_cols, df[day]], axis=1)
    df_temp = df_temp[df_temp[day] > 0]
    df_temp = df_temp.rename(columns = {day: 'qty'})
    df_temp.insert(0, 'day', [day]*df_temp.shape[0])
    if day == 'd_1':
        dft = df_temp
    else:
        dft = pd.concat([dft, df_temp], axis=0)

dft.to_csv('C:/Users/yeons/Documents/MSDSO/PROJECTS/M5/m5-data/sales_data.csv', index=False)


