name = input("Enter your name:")
cgpa = float(input("Enter your CGPA:"))
attendance = float(input("Enter your attendance percentage:"))


print("Student Name:",name)
print("CGPA:",cgpa)
print("Attendance:", attendance)

# if cgpa >= 7:
#     print("Performance: Good")
# else:
#     print("Performance: Needs Improvement")

# if cgpa >= 7 and attendance >= 75:
#     print("Performance: Good")
# else:
#     print("Performance: Needs Improvement")

if cgpa >= 9.0 and attendance >= 90:
    print("Excellent Student")
elif cgpa >= 8.0 and attendance >= 80:
    print("Very Good Student")
elif cgpa >= 7.0 and attendance >= 75:
    print("Good Student")
else:
    print("Average Student")

for i in range(5):
    print("Student number:", i)

    students = ["Ayush", "Rahul", "Aman", "Varun"]

for student in students:
    print("Student:", student)


student = {
    "name": "Ayush",
    "cgpa": 8.2,
    "attendance": 85,
    "projects": 3,
    "internship": True
}

print("Name:", student["name"])
print("CGPA:", student["cgpa"])
print("Attendance:", student["attendance"])
print("Projects:", student["projects"])
print("Internship:", student["internship"])


students = [
    {
        "name": "Ayush",
        "cgpa": 8.2,
        "attendance": 85
    },
    {
        "name": "Rahul",
        "cgpa": 7.4,
        "attendance": 78
    },
    {
        "name": "Aman",
        "cgpa": 9.1,
        "attendance": 92
    }
]

for student in students:
    print("Name:", student["name"])
    print("CGPA:", student["cgpa"])
    print("Attendance:", student["attendance"])
    print("----------------")



def greet_student(name):
    print("Hello", name)

greet_student("Ayush")
greet_student("Rahul")
greet_student("Aman")


def predict_performance(cgpa, attendance):

    if cgpa >= 9.0 and attendance >= 90:
        return "Excellent"

    elif cgpa >= 8.0 and attendance >= 80:
        return "Very Good"

    elif cgpa >= 7.0 and attendance >= 75:
        return "Good"

    else:
        return "Needs Improvement"

result = predict_performance(8.6, 77)

print("Prediction:", result)


print(predict_performance(9.2, 95))
print(predict_performance(8.5, 85))
print(predict_performance(6.5, 70))



def predict_performance(cgpa, attendance):

    if cgpa >= 9.0 and attendance >= 90:
        return "Excellent"

    elif cgpa >= 8.0 and attendance >= 80:
        return "Very Good"

    elif cgpa >= 7.0 and attendance >= 75:
        return "Good"

    else:
        return "Needs Improvement"


students = [
    {
        "name": "Ayush",
        "cgpa": 8.2,
        "attendance": 85
    },
    {
        "name": "Rahul",
        "cgpa": 7.4,
        "attendance": 78
    },
    {
        "name": "Aman",
        "cgpa": 9.1,
        "attendance": 92
    }
]


for student in students:

    result = predict_performance(
        student["cgpa"],
        student["attendance"]
    )

    print("Name:", student["name"])
    print("CGPA:", student["cgpa"])
    print("Attendance:", student["attendance"])
    print("Prediction:", result)
    print("----------------------")
    