"""
Задания:
    1. Cоздайте экземпляр класса студенда.
    2. Получите его полное имя используя метод get_full_name.
    3. Положите результат вызова метода get_full_name в переменную и распечатайте ее.
"""


class Student:
    def __init__(self, name: str, surname: str, faculty: str, course: int) -> None:
        self.name = name
        self.surname = surname
        self.faculty = faculty
        self.course = course

    def get_full_name(self) -> str:
        return f"Student's full name: {self.surname}, {self.name}"


if __name__ == '__main__':
    student = Student(name='Ivan', surname='Ivanov', faculty='Python Development', course='Learn Python')
    student_info = student.get_full_name()
    print(student_info)


