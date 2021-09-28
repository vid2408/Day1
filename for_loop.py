genre = ['pop', 'rock', 'jazz']
for i in range(len(genre)):
    print("I like", genre[i])


student_name = 'Soyuj'

marks = {'James': 90, 'Jules': 55, 'Arthur': 77}

for student in marks:
    if student == student_name:
        print(marks[student])
        break
else:
    print('No entry with that name found.')