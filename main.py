def get_top_student(subject, dataset):
    max_marks = 0
    max_student = ""

    for name, marks in dataset.items():
        if max_marks < marks:
            max_marks = marks
            max_student = name

    return (max_student , max_marks)


line = None

with open("data.txt") as file:
    lines = file.readlines()

if not lines:
    print("Error Reading")
    exit()

marks_lines = lines[1:]

subject_marks = {}

for line in marks_lines:
    entries = line.split(",")

    name = entries[0].strip()
    subject = entries[1].strip()
    marks = int(entries[2].strip())

    if subject not in subject_marks:
        subject_marks[subject] = {}

    subject_marks[subject][name] = marks

# print(subject_marks)

for subject , dataset in subject_marks.items():
    name, marks = get_top_student(subject , dataset)
    msg = f"Top Student for {subject} is {name} with {marks}"

    print(msg)


