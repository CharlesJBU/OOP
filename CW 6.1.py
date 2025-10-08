class Student:
    def __init__(self):
        self.stu_id = ""
        self.stu_name = ""
        self.major = ""
        self.gpa = 0.0
        self.dob = ""

    def add_student(self):
        self.stu_id = input("Enter student ID:")
        self.stu_name = input("Enter student name:")
        self.stu_major = input("Enter student major:")
        self.stu_gpa = float(input("Enter student gpa:"))
        self.stu_dob = input("Enter student date of birth:")
        self.courses = []

    def edit_student(self):
        self.stu_id = input("Enter updated student ID:")
        self.stu_name = input("Enter updated student name:")
        self.stu_major = input("Enter updated student major:")
        self.stu_gpa = int(input("Enter updated student gpa:"))
        self.stu_dob = input("Enter updated student date of birth:")

    def register_course(self, cc1):
        self.courses.append(cc1)

    def display_student(self):
        print("stu_id:", self.stu_id)
        print("stu name:", self.stu_name)
        for x in self.courses:
            print("Course Registered:", self[x].courseName)
class Course:
    def __init__(self, cid, cname):
        self.courseID = ""
        self.courseName = ""
    def add_course(self):
        self.courseID = input("Input course name:")
        self.courseName = input("Input course name:")

s1 = Student()
s1.add_student()
s1.display_student()

c1 = Course("CS1233", "OOP")



s1.register_course(c1)