class Student:
    def __init__(self, name, student_id, email, age, department, marks=None):
        self.name = name
        self.student_id = student_id
        self.__email = email
        self.__marks = marks if marks is not None else []
        self.age = age
        self.department = department

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_marks(self):
        return self.__marks

    def add_mark(self, mark):
        self.__marks.append(mark)

    def calculate_result(self, *additional_bonus_marks):
        if not self.__marks:
            return 0.0
        
        total = sum(self.__marks) + sum(additional_bonus_marks)
        average = total / len(self.__marks)
        return round(average, 2)

    def display_info(self):
        print(f"ID: {self.student_id} | Name: {self.name} | Dept: {self.department} | Age: {self.age} | Email: {self.__email}")

    def get_student_type(self):
        return "General Student"


class UndergraduateStudent(Student):
    def __init__(self, name, student_id, email, age, department, semester, marks=None):
        super().__init__(name, student_id, email, age, department, marks)
        self.semester = semester

    def get_student_type(self):
        return f"Undergraduate Student (Semester: {self.semester})"

    def display_info(self):
        super().display_info()
        print(f"Student Level: {self.get_student_type()}")


class GraduateStudent(Student):
    def __init__(self, name, student_id, email, age, department, research_topic, marks=None):
        super().__init__(name, student_id, email, age, department, marks)
        self.research_topic = research_topic

    def get_student_type(self):
        return f"Graduate Student (Research: {self.research_topic})"

    def display_info(self):
        super().display_info()
        print(f"Student Level: {self.get_student_type()}")


if __name__ == "__main__":
    print("\n--- 1 ---")
    student1 = Student("Rahim Ahmed", "S101", "rahim@example.com", 20, "Computer Science", [85, 90, 88])
    student1.display_info()
    print("Private Email Access (via getter):", student1.get_email())
    print("Calculated Result:", student1.calculate_result())
    print("Calculated Result with Bonus:", student1.calculate_result(2, 3))
    print("-" * 50)

    print("\n--- 2 ---")
    ug_student = UndergraduateStudent("Karim Chowdhury", "UG202", "karim@example.com", 21, "Electrical Eng", "4th Semester", [78, 82, 80])
    ug_student.display_info()
    print("Calculated Result:", ug_student.calculate_result())
    print("-" * 50)

    grad_student = GraduateStudent("Nusrat Jahan", "SS303", "nusrat@example.com", 24, "Data Science", "Machine Learning in Healthcare", [92, 95, 91])
    grad_student.display_info()
    print("Calculated Result:", grad_student.calculate_result())
    print("-" * 50)

    print("\n--- 3 ---")
    students_list = [student1, ug_student, grad_student]

    for s in students_list:
        print(f"{s.name} - Type: {s.get_student_type()}")