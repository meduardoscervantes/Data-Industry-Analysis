import pandas as pd
from os.path import exists

path = 'resources/occupation_Masterbook.xlsx'
if exists(path) and not exists('resources/masterbook/'):
    xcl = pd.read_excel(path, sheet_name=None)
    for key in xcl.keys():
        xcl[key].to_csv('resources/masterbook/{}.csv'.format(key), index=False)

path = 'resources/Fastest_Growing_Occupations_2020.xlsx'
if exists(path) and not exists('resources/growing_occupation/'):
    xcl = pd.read_excel(path, sheet_name=None)
    for key in xcl.keys():
        xcl[key].to_csv('resources/growing_occupation/{}.csv'.format(key), index=False)

