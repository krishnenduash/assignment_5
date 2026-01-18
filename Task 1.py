student_marks = {
    "arjun": 85,
    "raja": 78,
    "ram": 92,
    "bhim": 88
}

name_input = input("Enter the student's name: ")

input_lower = name_input.lower()

if input_lower in student_marks:
    print(f"{name_input.capitalize()}'s marks: {student_marks[input_lower]}")
else:
    print("Student not found.")
