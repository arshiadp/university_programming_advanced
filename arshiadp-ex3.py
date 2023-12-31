class Student:
    def __init__(self, first_name, last_name, age, student_code, score):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.student_code = student_code
        self.score = score
        self.students = {}

    def add(self,student):
        self.students[student.student_code] = student


    def info_display(self):
        print(f"your first_name {self.first_name}, your last_name is {self.last_name}, your age is {self.age} ")


    def __str__(self):
        return f"first_name: {self.first_name}, last name:{self.last_name}, age:{self.age},student code:{self.student_code}, score:{self.score} "


class Employee():
    def __init__(self, firs_name, last_name, age, employee_code, salary):
        super().__init__(firs_name, last_name, age)
        self.employee_code = employee_code
        self.salary = salary
        self.employee = {}
    
    def info_display(self):
        print(f"your first_name {self.first_name}, your last_name is {self.last_name}, your age is {self.age} ")
        print(super().info_display)

    def __str__(self):
        return f"{super().__str__()}, salary{self.salary}"    

class university(Student,Employee):

    def add_students(self, obj):
        if obj.first_name not in self.students:
            self.students[obj.first_name] = obj
            print('added!')
        else: 
            print('exist')  

    def remove_students(self, remove):  
        if remove in self.students:
            self.students.pop(remove)
            print('removed!')
        else: 
            print('not found!')

    def search_student(self, student_code):
        if student_code in self.students:
            return self.students[student_code]
        else:
            return None

    def edit_student(self, first_name=None, last_name=None, age=None):
        self.new_first_name = first_name or self.new_first_name
        self.new_last_name = last_name or self.new_last_name
        self.new_age = age or self.new_age
        print('edited! mew')
    
    def show_all_students(self):
        for student_code, student in self.students.items():
            print(f'student code:{self.student_code}')
            print(f'name:{self.first_name}')
            print(f'last name{self.last_name}')
            print(f'age: {self.age}')
            print(f'score{self.score}')  
 #employees method!!            

    def add_employee(self, obj1):
        if obj1.first_name not in self.employee:
            self.employee[obj1.first_name] = obj1
            print('added!')
        else: 
            print('exist') 

    def remove_employee(self, remove):
        if remove in self.employee:
            self.employee.pop(remove)
            print('removed!')
        else:
            print('not found')

    def search_employee(self, employee_code):
        if employee_code in self.employee:
            return self.employee[employee_code]
        else:
            return None
        
    def add(self,employee):
        self.employee[employee.employee_code] = employee    

    def show_all_employee(self):
        for employee_code, employee in self.employee.items():
            print(f'student code:{employee_code}')
            print(f'name:{employee.first_name}')
            print(f'last name{employee.last_name}')
            print(f'age: {employee.age}')
            print(f'score{employee.score}')     
        

if __name__ == '__main__':
    pass

        