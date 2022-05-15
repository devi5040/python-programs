class Student:
    def __init__(self):
        self.__student_id=None
        self.__age=None
        self.__marks=None
        self.__a=None
        self.__b=None
    def set_age(self,age):
        self.__age=age
    def set_student_id(self,student_id):
        self.__student_id=student_id
    def set_marks(self,marks):
        self.__marks=marks
    def get_marks(self):
        return self.__marks
    def get_age(self):
        return self.__age
    def get_student_id(self):
        return self.__student_id
    def validate_marks(self):
        if self.__marks>=0 and self.__marks<=100:
            return True
        else:
            return False
    def validate_age(self):
        if self.__age>20:
            return True
        else:
            return False
    def check_qualification(self):
        if self.validate_marks() and self.validate_age():
            if self.__marks>=65:
                return True
        return False
student=Student()
student.set_age(21)
student.set_student_id(1234)
student.set_marks(65)
student.validate_marks()
student.validate_age()
print(student.check_qualification())