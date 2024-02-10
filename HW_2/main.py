class Drawer:
    def __init__(self, height: float):
        self.height: float = height

    def set_height(self, height) -> float:
        self.height = height
        print(self.height)

    def draw_triangle(self, height) -> float:
        for i in range(1, height + 1):
            print(" " * (height - i) + "*" * (2 * i - 1))

class Calculator:
    def __init__(self):
        self.value = 1

    def set_value(self, num) -> float:
        self.value = num
        self.print_result()

    def add(self, num) -> float:
        self.value = self.value + num
        self.print_result()

    def subtract(self, num) -> float:
        self.value = self.value - num
        self.print_result()

    def multiply(self, num) -> float:
        self.value = self.value * num
        self.print_result()

    def divide(self, num) -> float:
        self.value = self.value / num
        self.print_result()

    def round(self, precision) -> float:
        self.value = round(precision)
        self.print_result()

    def print_result(self) -> None:
        print(self.value)

from datetime import datetime, timedelta

class Time:
    def __init__(self, hh: float, mm: float, ss: float):
        self.hours: float = hh
        self.mins: float = mm
        self.seconds: float = ss

    def get_total_seconds(self):
        total = (self.hours * 3600) + (self.mins * 60) + self.seconds
        print(total)

    def get_total_mins(self):
        total = (self.hours * 60) + self.mins + (self.seconds / 60)
        print(round(total))

    def get_total_hours(self):
        total = self.hours + (self.mins / 60) + (self.seconds / 3600)
        print(round(total))

    def get_day_time(self):
        total_seconds = self.hours * 3600 + self.mins * 60 + self.seconds
        time_delta = timedelta(seconds=total_seconds)
        hours = time_delta.days * 24 + time_delta.seconds // 3600
        minutes = (time_delta.seconds % 3600) // 60
        seconds = time_delta.seconds % 60
        am_pm = "AM" if hours < 12 else "PM"
        if hours == 0:
            hours = 12
        elif hours > 12:
            hours -= 12
        formatted_time = "{:02}:{:02}:{:02} {}".format(hours, minutes, seconds, am_pm)
        print(formatted_time)

    def get_day_time_universal(self):
        total_seconds = self.hours * 3600 + self.mins * 60 + self.seconds
        time_delta = timedelta(seconds=total_seconds)
        hours = time_delta.days * 24 + time_delta.seconds // 3600
        minutes = (time_delta.seconds % 3600) // 60
        seconds = time_delta.seconds % 60
        if hours > 24:
            hours = hours - 24
        formatted_time = "{:02}:{:02}:{:02}".format(hours, minutes, seconds)
        print(formatted_time)

# class Company:
#     def __init__(self):
#         self.name: str
#         self.description: str
#         self.bin: str
#         self.employees: list = []
    
#     def hire_employee(self, employee):


#     def fire_employee(self, employee_id):

#     def check_performance(self):
    
#     def print_top_employees(self):

# class Employee:
#     def __init__(self):
#         self.id: float
#         self.name: str
#         self.surname: str
#         self.position: str 
#         self.salary: str 
#         self.kpi: str 
        


class Employee:
    def __init__(self, employee_id, name, surname, position, salary, kpi):
        self.id = employee_id
        self.name = name
        self.surname = surname
        self.position = position
        self.salary = salary
        self.kpi = kpi

class Company:
    def __init__(self, name, description, bin):
        self.name = name
        self.description = description
        self.bin = bin
        self.employees = []

    def hire_employee(self, employee):
        self.employees.append(employee)

    def fire_employee(self, employee_id):
        for i, emp in enumerate(self.employees):
            if emp.id == employee_id:
                del self.employees[i]
                break

    def check_performance(self):
        for emp in self.employees:
            if emp.kpi < 50:
                self.fire_employee(emp.id)
            elif emp.kpi > 90:
                emp.salary *= 1.2

    def print_top_employees(self):
        sorted_employees = sorted(self.employees, key=lambda x: x.kpi, reverse=True)
        top_employees = []
        current_kpi = None
        for emp in sorted_employees:
            if len(top_employees) >= 3 and emp.kpi != current_kpi:
                break
            top_employees.append(emp)
            current_kpi = emp.kpi
        for emp in top_employees:
            print(f"ID: {emp.id}, Name: {emp.name} {emp.surname}, Position: {emp.position}, Salary: {emp.salary}, KPI: {emp.kpi}")

