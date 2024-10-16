class Univeristy:
    def __init__(self, name):
        self.name = name
        self.teachers = []
        self.students = []
        self.sections = []

        def add_teacher(self, teacher):
            self.teachers.append(teacher)

        def add_student(self, student):
            self.students.append(student)

        def add_section(self, section):
            self.sections.append(section)


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Human):
    def __init__(self, name, age, grade):
      super().__init__(name, age)
      self.grade = grade

class Teacher(Human):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject


class Section:
    def __init__(self,student_name, student_teacher, section_name, start_timing, end_timing):
        self.student_name = student_name
        self.student_teacher = student_teacher
        self.section_name = section_name
        self.start_timing = start_timing
        self.end_timing = end_timing

        print(f"student Name : {student_name}")
        print(f"Teacher Name : {student_teacher}")
        print(f"section name : {section_name}")
        print(f" section start timing : {start_timing}, section off timing : {end_timing}")

# creating object
my_university = Univeristy("XYZ University")
student1 = Student("John Doe", 20, "Grade 10")
student2  = Student("Jane Smith", 22, "Grade 11")
student3 = Student("Bob Johnson", 21, "Grade 9")
student4 = Student("Alice Brown", 23, "Grade 12")
student5 = Student("Mike Wilson", 20, "Grade 10")

teacher1 = Teacher("Dr. Smith", 45, "Mathematics")
teacher2 = Teacher("Prof. Johnson", 50, "Physics")
teacher3 = Teacher("Mrs. Brown", 38, "Chemistry")

section1 = Section("Mathematics", "Dr. Smith", "A", "9:00 AM", "12:00 PM")
section2 = Section("Physics", "Prof. Johnson", "B", "10:00 AM", "1:00 PM")
section3 = Section("Chemistry", "Mrs. Brown", "C", "2:00 PM", "5:00 PM")


# adding object in my_univeristy
my_university.add_student(student1)
my_university.add_student(student2)
my_university.add_student(student3)
my_university.add_student(student4)
my_university.add_student(student5)

my_university.add_teacher(teacher1)
my_university.add_teacher(teacher2)
my_university.add_teacher(teacher3)


my_university.add_section(section1)
my_university.add_section(section2)
my_university.add_section(section3)




