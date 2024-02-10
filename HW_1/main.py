class Student:
    def __init__(self, name: str, surname: str, student_id: int, course: int, faculty: str, speciality: str):
        self.full_name = [name, surname]
        self.id: int = student_id
        self.s_course: int = course
        self.s_faculty: str = faculty
        self.speciality: str = speciality
        self.is_mestnyi: bool = False
        self.subjects = []
        self.semester: int = 1

    def all_info(self) -> None:
        for attr_name in dir(self):
            if not attr_name.startswith('__'):
                attr_value = getattr(self, attr_name)
                print(f"{attr_name}: {attr_value}")

    def get_full_name(self) -> None:
        print(self.full_name[0] + ' ' + self.full_name[1])

    def add_subject(self, subject: str) -> None:
        self.subjects.append(subject)
        print(self.subjects)

    def semester_change(self) -> None:
        self.semester = self.semester + 1
        print(self.semester)

class Faculty: 
    def __init__(self, name: str, dean: str, cabinet_number: int):
        self.faculty_name: str = name
        self.dean: str = dean
        self.students = []

    def add_student(self, student: Student) -> None:
        self.students.append(student)

    def show_students(self) -> None:
        for student in self.students:
            print(student['full_name'])