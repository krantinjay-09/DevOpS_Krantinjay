students = {}

while True:
    name = input("Enter student name (stop to finish): ")

    if name.lower() == "stop":
        break

    grade = int(input("Enter grade: "))
    students[name] = grade
    
update_name = input("Enter student name to update: ")
if update_name in students:
    new_grade = int(input("Enter new grade: "))
    students[update_name] = new_grade
    print("Grade updated")
else:
    print("Student not found")

print("\nAll student grades:")

for name, grade in students.items():
    print(name, ":", grade)