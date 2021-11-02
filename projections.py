import pandas as pd
import os
pd.set_option('display.max_columns', None)

for file in os.listdir('resources/masterbook'):
    df = pd.read_csv(f'resources/masterbook/{file}')
    # print(df.head())
code = "15-0000"
ocupations = [
    "Computer and information research scientists",
    "Computer and information systems managers",
    "Computer and mathematical occupations",
    "Computer network architects",
    "Computer network support specialists",
    "Computer numerically controlled tool operators",
    "Computer numerically controlled tool programmers",
    "Computer programmers",
    "Computer systems analysts",
    "Data scientists and mathematical science occupations, all other",
    "Database administrators and architects"
]

t1_7 = pd.read_csv('resources/masterbook/Table 1.7.csv')
new_columns = []

for x in t1_7.columns:
    print(t1_7[x].iloc[0])
    new_columns.append(t1_7[x].iloc[0])
t1_7.columns = new_columns
print(t1_7.head())

masterbook_df = []