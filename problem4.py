import json


with open("students.json",encoding="utf-8") as file:
    student=json.load(file)

max_ball=max(student,key=lambda x: x["grade"])
min_ball=min(student,key=lambda x: x["grade"])

total=0
for i in student:
    total+=i["grade"]

print(f"Eng yaxshi talaba:{max_ball["name"]} {max_ball["grade"]}")
print(f"Eng past baho:{min_ball["name"],min_ball["grade"]}")
print(f"Ortacha baho:{total//len(student)}")