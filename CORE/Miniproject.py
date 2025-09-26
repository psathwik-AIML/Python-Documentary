# Mini project using list,tuple,dictionary and set
# mini data base 
print("STUDENT MANAGER: ---------->")
# dictionary to store students data
student1={
    "name":"sathwik",
    "age":22,
    "skills":["java","sql","python"]
    }
student2={
    "name":"remo",
    "age":31,
    "skills":["python","html","java","AIML"]
}
# store students in a list
students=[student1,student2]
# store unique skills of students in a set
unique_skills=set()
for student in students:
    for skill in student["skills"]:
        unique_skills.add(skill)
# store date of birth as tuple
sathwik_dob = (2003, 3, 31)  # year, month, day
# print all
for i, student in enumerate(students, start=1):
    print(f"Student {i}: {student}")

print(f"Unique skills: {unique_skills}")
print(f"Sunny DOB: {sathwik_dob}")
