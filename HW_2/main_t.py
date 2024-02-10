from main import Drawer
from main import Calculator
from main import Time 
from main import Company 
from main import Employee 

obj_1 = Drawer(3)
# obj_1.set_height(4)
# obj_1.draw_triangle(5)

obj_2 = Calculator()
# obj_2.set_value(2)
# obj_2.add(1)
# obj_2.subtract(1)
# obj_2.multiply(1)
# obj_2.divide(2)
# obj_2.round(1.21)

obj_3 = Time(25 , 67, 120)
# obj_3.get_day_time_universal()

from random import randint

obj_4 = Company("Example Company", "Description", "1234567890")
for i in range(100):
    employee = Employee(i+1, f"Employee{i+1}", "Surname", "Position", 50000, randint(0, 100))
    obj_4.hire_employee(employee)
obj_4.check_performance()
obj_4.print_top_employees()