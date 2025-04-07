class Person:
    def __init__(self, name, age):
            self.name = name
            self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old")


class Student(Person):
    def __init__ (self, name, age, student_id):
        super().__init__(name,age)
        self.student_id = student_id

    def study(self):
        print(f"{self.name} is studying")


studenti1 = Student("Arber",20,"S12345")

studenti1.greet()
studenti1.study()
