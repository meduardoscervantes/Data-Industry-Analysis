import pandas as pd
from os.path import exists
import os
pd.set_option('display.max_columns', None)

path = '../../Resources/manuel/occupation_Masterbook.xlsx'
if exists(path) and not exists('../../Resources/masterbook/'):
    os.mkdir('../../Resources/masterbook')
    xcl = pd.read_excel(path, sheet_name=None)
    for key in xcl.keys():
        xcl[key].to_csv('Resources/masterbook/{}.csv'.format(key), index=False)
        df = pd.read_csv('Resources/masterbook/{}.csv'.format(key))
        new_columns = []
        for x in df.columns:
            new_columns.append(df[x].iloc[0])
        df.columns = new_columns
        clean_df = df.iloc[1:]
        clean_df.to_csv('Resources/masterbook/{}.csv'.format(key), index=False)

path = '../../Resources/manuel/Fastest_Growing_Occupations_2020.xlsx'
if exists(path) and not exists('../../Resources/growing_occupation/'):
    os.mkdir('../../Resources/growing_occupation/')
    xcl = pd.read_excel(path, sheet_name=None)
    for key in xcl.keys():
        xcl[key].to_csv('Resources/growing_occupation/{}.csv'.format(key), index=False)
        df = pd.read_csv('Resources/growing_occupation/{}.csv'.format(key))
        new_columns = []
        for x in df.columns:
            new_columns.append(df[x].iloc[0])
        df.columns = new_columns
        clean_df = df.iloc[1:]
        clean_df.to_csv('Resources/growing_occupation/{}.csv'.format(key), index=False)
