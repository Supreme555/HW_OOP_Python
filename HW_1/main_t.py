from main import Student
from main import Faculty

obj_1 = Student('Tom', 'Adoms', 0, 2, 'IT', 'PM')
# obj_1.all_info() 
# obj_1.get_full_name()
# obj_1.add_subject('Math')
# obj_1.semester_change()


obj_2 = Faculty('IT', 'Magomed', 301)
obj_students = [
    {
    'id': 0,
    'full_name': 'Alex Adom_1'
    },
    {
    'id': 1,
    'full_name': 'Alex Adom_2'
    },
    {
    'id': 2,
    'full_name': 'Alex Adom_3'
    },
    {
    'id': 3,
    'full_name': 'Alex Adom_4'
    },
    {
    'id': 4,
    'full_name': 'Alex Adom_5'
    }
]
for i in obj_students:
    obj_2.add_student(i)
obj_2.show_students()
