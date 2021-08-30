
from random import randint

class Student:
    def __init__(self, name, surname, gender, *course):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.person = {}
        self.course = course




    def __str__(self):
        return f'Имя - {self.name}, Фамилия - {self.surname}, {self.finished_courses}, "\n"' \
               f'Pytson - {self.grades["Python"]}, "\n" Git - {self.grades["Git"]}"\n"' \
               f' средний бал {self.person[self.name]}'



    def rate_hw(self, lekt, course, grade):
        if isinstance(lekt, Lecturer) and course in lecturer.courses_attached \
                and course in lekt.courses_in_progress:
            if course in lekt.lector_grades:
                lekt.lector_grades[course] += [grade]

            else:
                lekt.lector_grades[course] = [grade]

        else:
            return 'Ошибка'
        return f"{lekt.lector_grades[course]}"



    def peson_grade(self, grade,):
        if self.course in self.grades:
            self.person[self.name] += grade
        else:
                self.pers = self.grades['Python'] + self.grades['Git']
                self.person[self.name] = float(sum(self.grades['Python'] + self.grades['Git']) / len(self.pers))


    def student_act(self):

            dese = randint(1, 6)
            if dese == 1:
                students.rate_hw(lecturer, 'Python', 10) and \
                students.rate_hw(lecturer, 'Git', 8)
                lecturer.peson_grade(lecturer, 'Bill')
                lecturer.peson_grade(lecturer, 'Some')


            elif dese == 4:
                students.rate_hw(lecturer, 'Python', 9) and \
                students.rate_hw(lecturer, 'Git', 10)
                lecturer.peson_grade(lecturer, 'Bill')
                lecturer.peson_grade(lecturer, 'Some')



            elif dese == 5:
                students.rate_hw(lecturer, 'Python', 8) and \
                students.rate_hw(lecturer, 'Git', 9)
                lecturer.peson_grade(lecturer, 'Bill')
                lecturer.peson_grade(lecturer, 'Some')


            else:
                students.rate_hw(lecturer, 'Python', 10) and \
                students.rate_hw(lecturer, 'Git', 10)
                lecturer.peson_grade(lecturer, 'Bill')
                lecturer.peson_grade(lecturer, 'Some')





class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


    def __str__(self):
        pass




class Lecturer(Mentor):
    def __init__(self, name, surname, *course):
        super().__init__(name=name, surname=surname)
        self.name = name
        self.courses_attached = []
        self.lector_grades = {}
        self.courses_in_progress = []
        self.person = {}
        self.course = course
        self.person1 = {}
        self.person2 = {}





    def __str__(self):
        return f'Имя - {self.name}, Фамилия - {self.surname}, "\n"' \
               f'Pytson - {self.lector_grades["Python"]}, "\n" Git - {self.lector_grades["Git"]}"\n"' \
               f'общий средний бал за лекции {self.person[self.name]}"\n"' \
               f'средний бал за лекции Python - {self.person1}"\n"' \
               f'средний бал за лекции Git - {self.person2}'

    def reed_lection(self, cours,):
        print(f'прочтение текста - {cours}')

    def peson_grade(self, grade, name, *course):
        if self.course in self.lector_grades:
            print()
            self.person[self.name] += grade
        else:
                self.pers = self.lector_grades['Python'] + self.lector_grades['Git']
                self.person[name] = round(sum(self.lector_grades['Python'] + self.lector_grades['Git']) / len(self.pers), 2)
                self.person1[self.name] = ("{:.2f}".format(round(sum(self.lector_grades['Python'],
                                                                 2)) / len(self.lector_grades['Python'])))
                self.person2[self.name] = ("{:.2f}".format(round(sum(self.lector_grades['Git'],
                                                                 2)) / len(self.lector_grades['Git'])))

    def __lt__(self, other):
        if self.person < other.person:
            print('Not a Character!')
            return
        return self.person < other.person, 'oh'



    def ickvel(self):
        if lecturer.person['Elizar'] < lecturer.person['Some']:
            print('лучший преподователь Some')
        else:
            print('лучший преподователь Bill')


    def act(self):
        dises = randint(1, 2)
        if dises == 1:
            self.reed_lection('Paython') and self.reed_lection('Git')
        else:
            self.reed_lection('Paython') and self.reed_lection('Git')

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name=name, surname=surname)
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached \
                and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        return f"{student.grades[course]}"

    def rvw_act(self):

        dese = randint(1, 6)
        if dese == 1:
            reviewer.rate_hw(students, 'Python', 10) and \
            reviewer.rate_hw(students, 'Git', 8)
            students.peson_grade(students)
        elif dese == 4:
            reviewer.rate_hw(students, 'Python', 9) and \
            reviewer.rate_hw(students, 'Git', 10)
            students.peson_grade(students)

        elif dese == 5:
            reviewer.rate_hw(students, 'Python', 8) and \
            reviewer.rate_hw(students, 'Git', 9)
            students.peson_grade(students)

        else:
            reviewer.rate_hw(students, 'Python', 10) and \
            reviewer.rate_hw(students, 'Git', 10)
            students.peson_grade(students)


student = [Student(name="Семен", surname="Орлов", gender='Mail'),
            Student(name="Александр", surname="Антонов", gender='Mail',),
            Student(name="Леонид", surname="Парфенов", gender='Mail',)
            ]

for students in student:
    students.courses_in_progress += ['Python']
    students.courses_in_progress += ['Git']
    students.finished_courses = ['введение в програмирование']


lectur = [Lecturer(name='Some', surname='odoc'),
            Lecturer(name='Bill', surname='Fishman')]

for lecturer in lectur:
    lecturer.courses_attached += ['Python']
    lecturer.courses_attached += ['Git']
    lecturer.courses_in_progress += ['Python']
    lecturer.courses_in_progress += ['Git']



reviewer = Reviewer('Some', 'Buddy')
reviewer.courses_attached += ['Python']
reviewer.courses_attached += ['Git']



for week in range(1, 4, 5):
    print(f'========================== {week} ===========================')
    for students in student:
        reviewer.rvw_act()




    print(f'========================== итоги {week} недели ===========================')
    print(f'========================== студенты ===========================')

    for students in student:
        print(f'{students}')



 
    print(f'========================== преподы ===========================')
    for lecturer in lectur:
        students.student_act()
        print(lecturer)
        lecturer.person['Some'].__lt__(lecturer.person['Bill'])

        print(lecturer.person['Bill'])
        print(lecturer.person['Some'])
        print(f'{(lecturer.person["Bill"]) == (lecturer.person["Some"])}')
        print(lecturer.person1)




 


