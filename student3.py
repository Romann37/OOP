class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
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
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        pass

class Lecturer(Mentor):
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
        return self.person < other.person, 'gggg'



    def ickvel(self):
        if lecturer.person['Elizar'] < lecturer.person['Some']:
            print('лучший преподователь Some')
        else:
            print('лучший преподователь Elizar')
    
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
        
    
 
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
 
cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
 
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
 
print(best_student.grades)
