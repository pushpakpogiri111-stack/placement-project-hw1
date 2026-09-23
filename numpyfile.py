import csv
import numpy as np

python_list = [] 
aptitude_list = [] 
communication_list = []
skill_list = []

with open("placement_readiness.csv", "r") as f:
    reader = csv.DictReader(f)
    next(reader)  # Skip the header row
    for row in reader:
        python_list.append(int(row["Python_Score"]))
        aptitude_list.append(int(row["Aptitude_Score"]))
        communication_list.append(int(row["Communication_Score"]))
        skill_list.append([int(row["Python_Score"]), int(row["SQL_Score"]), int(row["Aptitude_Score"]), int(row["Communication_Score"])])

python_array = np.array(python_list)
aptitude_array = np.array(aptitude_list)
communication_array = np.array(communication_list)
skill_array = np.array(skill_list)

python_average = python_array.mean() 
aptitude_high = aptitude_array.max()
aptitude_low = aptitude_array.min()
communication_above70 = (communication_array>70).sum()
best_skill = skill_array.max(axis=1)   # axis means means do it for each student (each row).
worst_skill = skill_array.min(axis=1) 
gap_btw_best_worst = best_skill - worst_skill


print("Average Python score:", python_average, "Highest Aptitude:", aptitude_high, "Lowest Aptitude:", aptitude_low, "Communication above 70:", communication_above70, "Skill gaps:", gap_btw_best_worst)



