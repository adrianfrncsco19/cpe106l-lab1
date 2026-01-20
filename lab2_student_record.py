student = {
  "id": "2025-001"
  "name": "Juan Dela Cruz",
"grades": [88, 90, 85]
}

#Calculate Average
average = sum(student["grade"]) / len(student["grade"])
print ("Average", average)

#Data Manipulation

#Add new grade
student["grades"].append(92)

#Update student info
student["name"] = "Juan Dela Cruz Jr."

#Display formatted output
print(f"Student ID: {student['id']}")
print(f"Student Name: {student['name']}")
print(f"Grades: {student['grades']}")
print(f"Updated Average: {sum(student['grade']) / len(student['grade']):.2f}")
