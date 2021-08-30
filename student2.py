class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

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
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
class Lecturer(Mentor):
    def __init__(self, name, surname, *course):
        super().__init__(name=name, surname=surname)
        self.name = name
        self.courses_attached = []
        self.lector_grades = {}
        self.courses_in_progress = []
        self.person = {}
        self.course = course

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
