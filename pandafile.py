import csv 
import pandas as pd
df = pd.read_csv("placement_readiness.csv")

print(df.head(9))
print(df.tail())
print(df.shape)
print(df.columns)
print(df.describe)

python_above_75 = df[df["Python_Score"]>75]
aptitude_sort = df.sort_values("Aptitude_Score",ascending=False)
python_top_10 =df.sort_values("Python_Score",ascending=False).head(10)
strong_python_weak_communication = df[(df["Python_Score"]>75) & (df["Communication_Score"] < 60)]

print("First 5 rows:\n",df.head())
print("Shape:\n", df.shape)
print("Columns:\n", df.columns)
print("Description:\n", df.describe())
print("Python above 75:\n", python_above_75)
print("Aptitude highest first:\n", aptitude_sort)
print("Top 10 Python students:\n", python_top_10)
print("Strong Python but weak Communication:\n", strong_python_weak_communication)

Total_Score = df["Python_Score"]+df["Communication_Score"]+df["SQL_Score"] + df["Aptitude_Score"]                        
df[Average_Score] = df[Total_Score]/4  # to create a seperate column(dataframe) we put df[average_score]  .....other wise it store as seperate variable 
df["Weakest_Skill_Score"] = df[["Python_Score", "SQL_Score", "Aptitude_Score", "Communication_Score"]].min(axis=1)#axis for every column 

