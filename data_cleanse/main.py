import pandas as pd
import matplotlib.pyplot as plt
import os

masterbook_dfs = [
    pd.read_csv(f'resources/masterbook_breakdown/{file}')
    for file in os.listdir('../resources/masterbook_breakdown')
]

growing_occ_df = [
    pd.read_csv(f'resources/growing_occupation_breakdown/{file}')
    for file in os.listdir('../resources/growing_occupation_breakdown')
]

# Read the .csv with Employment Information
job_stats_df = masterbook_dfs[1]
print(job_stats_df.columns)
# Update the column names for greater legibility
columns = []
for x in job_stats_df.columns:
    if x == 'Occupation\ntype':
        columns.append("Occupation Type")
    else:
        columns.append(x)
job_stats_df.columns = columns

if not os.path.exists('../resources/graphs/'):
    os.mkdir('../resources/graphs/')
    counter = 0
    for x in range(len(job_stats_df.columns)):
        for y in range(len(job_stats_df.columns)):
            x_axis = job_stats_df[job_stats_df.columns[x]]
            y_axis = job_stats_df[job_stats_df.columns[y]]
            title = f'{job_stats_df.columns[x]} vs. {job_stats_df.columns[y]}'
            plt.figure(counter)
            plt.bar(x_axis, y_axis)
            plt.xlabel(job_stats_df.columns[x])
            plt.ylabel(job_stats_df.columns[y])
            plt.title(title)
            plt.xticks(rotation=90)
            plt.savefig(f'resources/graphs/{title}.png')
            plt.close(counter)
            counter += 1

# 3 4
# plt.bar(job_stats_df[job_stats_df.columns[0]], job_stats_df[job_stats_df.columns[4]])
# plt.bar(job_stats_df[job_stats_df.columns[0]], job_stats_df[job_stats_df.columns[3]])
# plt.xticks(rotation=90)
# plt.savefig('resources/graphs/current_vs_expected_growth.png')
# plt.show()
