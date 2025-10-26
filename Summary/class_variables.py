"""
CLASS VARIABLES = Shared among all instances of a class,
                  Defined outside the constructor function
                  Allows us to share data among all objects of that class
"""


class Student:

    # Class variable
    class_year = 2024
    class_num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.class_num_students += 1


student1 = Student("Bob", 20)
student2 = Student("Marley", 19)
student3 = Student("Alice", 32)
student4 = Student("Jimmy", 28)

"""
print(student1.name)
print(student1.age)
print(student1.class_year)

print(student2.name)
print(student2.age)
print(student2.class_year)
"""
# We can also access a class variable by class name for more readability i,e
print(Student.class_year)

print(
    f"My graduating class of {Student.class_year} has {Student.class_num_students} no of students:"
)
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)
