import csv
import random as rd

NUM_STUDENTS = 100

rd.seed()
rows = []
branches = ["CSE", "ECE", "IT", "MECH"]

for i in range(NUM_STUDENTS):
    student_id = i + 1
    branch = rd.choice(branches)
    python_score = rd.randint(40, 95)
    sql_score = rd.randint(40, 95)
    aptitude_score = rd.randint(40, 95)
    communication_score = rd.randint(40, 95)
    projects_completed = rd.randint(0, 5)
    mock_interviews_attended = rd.randint(0, 5)
    rows.append([student_id,branch,python_score,sql_score,aptitude_score,communication_score,projects_completed,mock_interviews_attended])


with open(
    "placement_readiness.csv",
    "w",
    newline="",
    encoding="utf-8"
) as f:
    writer = csv.writer(f)
    writer.writerow([
        "Student_ID",
        "Branch",
        "Python_Score",
        "SQL_Score",
        "Aptitude_Score",
        "Communication_Score",
        "Projects_Completed",
        "Mock_Interviews_Attended"
    ])
    writer.writerows(rows)
    print("Data generated successfully and saved to placement_readiness.csv")
