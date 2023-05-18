# Import pandas library
import pandas as pd

# Read sample.csv file and convert it into a data frame
df_csv = pd.read_csv("Cars1.csv")

# Read sample.xlsx file and convert it into a data frame
df_car = pd.read_csv("cars2.csv")

# Print the data frames
print(df_csv)
print(df_car)

# Merge df_csv and df_excel on the basis of Company Name and Model Name
df_merged = pd.merge(df_csv, df_car, on=["Company Name", "Model Name"])

# Print the merged data frame
print(df_merged)

# Fill the NA values in df_merged with mean
df_merged = df_merged.fillna(df_merged.mean())

# Print the filled data frame
print(df_merged)
