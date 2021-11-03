import pandas as pd
from os.path import exists
import os
pd.set_option('display.max_columns', None)

path = '../resources/occupation_Masterbook.xlsx'
if exists(path) and not exists('../resources/masterbook/'):
    os.mkdir('../resources/masterbook')
    xcl = pd.read_excel(path, sheet_name=None)
    for key in xcl.keys():
        xcl[key].to_csv('resources/masterbook/{}.csv'.format(key), index=False)
        df = pd.read_csv('resources/masterbook/{}.csv'.format(key))
        new_columns = []
        for x in df.columns:
            new_columns.append(df[x].iloc[0])
        df.columns = new_columns
        clean_df = df.iloc[1:]
        clean_df.to_csv('resources/masterbook/{}.csv'.format(key), index=False)

path = '../resources/Fastest_Growing_Occupations_2020.xlsx'
if exists(path) and not exists('../resources/growing_occupation/'):
    os.mkdir('../resources/growing_occupation/')
    xcl = pd.read_excel(path, sheet_name=None)
    for key in xcl.keys():
        xcl[key].to_csv('resources/growing_occupation/{}.csv'.format(key), index=False)
        df = pd.read_csv('resources/growing_occupation/{}.csv'.format(key))
        new_columns = []
        for x in df.columns:
            new_columns.append(df[x].iloc[0])
        df.columns = new_columns
        clean_df = df.iloc[1:]
        clean_df.to_csv('resources/growing_occupation/{}.csv'.format(key), index=False)
