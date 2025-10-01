Class Student:
    def_init_(self):
        self.stu_id = ""
        self.stu_name = ""
        self.major = ""
        self.gpa = ""
        self.dob = ""
    def add_student(self):
        self.stu_id = input("Enter student ID:")
        self.stu_name = input("Enter student name:")
        self.stu_major = input("Enter student major:")
        self.stu_gpa = int(input("Enter student gpa:"))
        self.stu_dob = input("Enter student date of birth:")
    def edit_student(self):
        self.stu_id = input("Enter updated student ID:")
        self.stu_name = input("Enter updated student name:")
        self.stu_major = input("Enter updated student major:")
        self.stu_gpa = int(input("Enter updated student gpa:"))
        self.stu_dob = input("Enter updated student date of birth:")
    def display_student(self):
        print("stu_id:", self.stu_id)
Course:

Faculty:

Books: