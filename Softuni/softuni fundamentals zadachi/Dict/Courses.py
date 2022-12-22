`course={}
while True:
    command = input()
    if command == "end":
        break
    else:
        tokens =command.split(" : ")
        course_name = tokens[0]
        student_name = tokens[1]
        if course_name not in course.keys():
            course[course_name] =[]
        course[course_name].append(student_name)
        # elif course_name in course.keys():
        #     course[course_name].append(student_name)

for course_name in course.keys():
    registered_students = len(course[course_name])
    print(f"{course_name}: {registered_students}")
    for i in course[course_name]:
        print(f'-- {i}')

