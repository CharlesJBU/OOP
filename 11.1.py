class Hospital:
    def __init__(self):
        self.loc = ""
        self.size = ""
        self.traumlevel = ""
        self.equip = ""
        self.staff = ""

    def create_hospital(selfs):
        self.loc = input("enter hospital adress")
        self.size = input("enter hospital size")
        self.traumlevel = input("enter hospital trauma level")
        self.equip = input("enter specialized equipment")
        self.staff = input("enter staff")

class Doctor:
    def __init__(self):
        self.userid = ""
        self.name = ""
        self.specialty = ""
        self.experience = ""
        self.password = ""

    def create_doctor(self):
        self.userid = input("enter user ID")
        self.name = input("enter user name")
        self.specialty = input("enter Doctors specialty")
        self.experience = input("enter Doctor experience")
        self.password = input("enter account password")

class Nurse:
    def __init__(self):
        self.userid = ""
        self.name = ""
        self.cerifications = ""
        self.experience = ""
        self.password = ""

    def create_nurse(self):
        self.userid = input("enter user ID")
        self.name = input("enter user name")
        self.certifications = input("enter nurses certifications")
        self.experience = input("enter nurses experience")
        self.password = input("enter nurses password")

class Patient:
    def __init__(self):
        self.userid = ""
        self.name = ""
        self.age = ""
        self.gender = ""
        self.cheifcom = ""
        self.surg = ""
        self.meds = ""
        self.password = ""

    def create_doctor(self):
        self.userid = input("enter user ID")
        self.name = input("enter user name")
        self.age = input("enter patient age")
        self.gender = input("enter patient gender")
        self.cheifcom = input("enter patient cheif complaint")
        self.surg = input("enter patient history of surgeries")
        self.meds = input("enter patient medication list")
        self.password = input("enter account password")

class Administration:
    def __init__(self):


while 1:
    print("Press 1 to log in:")
    print("Press 2 to create an account:")
    print("Press 3 to exit:")
    option = input("Enter command:")
    if option =="1":
        uid = input("input user ID")
        pwd = input("enter password:")

#future directory needed
    #doctor
    print("Press 1 to input patient diagnosis")
    print("Press 2 to presribe medication to patient")
    print("Press 3 to schedule surguries")
    print("Press 4 to update patient medical history")
    print("Press 5 to write patient comments")
    print("Press 5 to logout")

    #nurse
    print("Press 1 to document treatments")
    print("Press 2 to write patient comments")
    print("Press 3 to logout")

    #patient
    print("Press 1 to view medical history")
    print("Press 2 to "


    if option =="2":
        uid = input("enter user ID:")
        nname = input("Enter full name:")
        pwd: input("Enter password:"))
        cclass = input("enter hospital role:")
        print("account created successfully! Proceed to log in.")

    Database.update({uid:{"name":nname, "password":pwd}})
        print(Database)