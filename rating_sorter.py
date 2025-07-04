import json

with open("students.json") as f:
    students = json.load(f)

students_s = sorted(students, key=lambda x: x["score"], reverse=True)

for i, student in enumerate(students_s, start=1):
    student["rank"] = i

with open("rating.json", "w") as f1:
    json.dump(students_s, f1, indent=2)


