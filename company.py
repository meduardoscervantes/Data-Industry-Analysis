import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

#######################################################
# Sorted 7mil+ companies into 2mil+ US companies      #
# Then sorted them into US based technology companies #
# Finally created a .csv file with those companies    #
#######################################################
# us_df = pd.read_csv("resources/us_companies.csv")
# industries = ["information technology and services", "computer software", "telecommunications", "computer networking"]
# df = us_df.loc[
#     (us_df["industry"] == industries[0]) |
#     (us_df["industry"] == industries[1]) |
#     (us_df["industry"] == industries[2]) |
#     (us_df["industry"] == industries[3])
# ]
# df.to_csv("resources/us_tech_companies.csv", index=False)
