import pandas as pd
import os
pd.set_option('display.max_columns', 2)

ocupations = [
    '11-3021',
    '15-0000',
    '15-1211',
    '15-1221',
    '15-1231',
    '15-1241',
    '15-1245',
    '15-1251',
    '15-2098',
    '51-9161',
    '51-9162'
]
if not os.path.exists('resources/masterbook_breakdown'):
    counter = 0
    for file in os.listdir('resources/masterbook'):
        df = pd.read_csv(f'resources/masterbook/{file}')
        if counter == 0:
            pass
        else:
            occ_df = df.loc[
                (df[df.columns[1]] == ocupations[0]) |
                (df[df.columns[1]] == ocupations[1]) |
                (df[df.columns[1]] == ocupations[2]) |
                (df[df.columns[1]] == ocupations[3]) |
                (df[df.columns[1]] == ocupations[4]) |
                (df[df.columns[1]] == ocupations[5]) |
                (df[df.columns[1]] == ocupations[6]) |
                (df[df.columns[1]] == ocupations[7]) |
                (df[df.columns[1]] == ocupations[8]) |
                (df[df.columns[1]] == ocupations[9]) |
                (df[df.columns[1]] == ocupations[10])
            ]
            if not os.path.exists('resources/masterbook_breakdown/'):
                os.mkdir('resources/masterbook_breakdown/')
            if not len(occ_df) == 0:
                occ_df.to_csv(f'resources/masterbook_breakdown/{file}', index=False)
        counter += 1
if not os.path.exists('resources/growing_occupation_breakdown'):
    counter = 0
    for file in os.listdir('resources/growing_occupation'):
        df = pd.read_csv(f'resources/growing_occupation/{file}')
        if counter == 0:
            pass
        else:
            occ_df = df.loc[
                (df[df.columns[1]] == ocupations[0]) |
                (df[df.columns[1]] == ocupations[1]) |
                (df[df.columns[1]] == ocupations[2]) |
                (df[df.columns[1]] == ocupations[3]) |
                (df[df.columns[1]] == ocupations[4]) |
                (df[df.columns[1]] == ocupations[5]) |
                (df[df.columns[1]] == ocupations[6]) |
                (df[df.columns[1]] == ocupations[7]) |
                (df[df.columns[1]] == ocupations[8]) |
                (df[df.columns[1]] == ocupations[9]) |
                (df[df.columns[1]] == ocupations[10])
            ]
            if not os.path.exists('resources/growing_occupation_breakdown/'):
                os.mkdir('resources/growing_occupation_breakdown/')
            if not len(occ_df) == 0:
                occ_df.to_csv(f'resources/growing_occupation_breakdown/{file}', index=False)
        counter += 1
