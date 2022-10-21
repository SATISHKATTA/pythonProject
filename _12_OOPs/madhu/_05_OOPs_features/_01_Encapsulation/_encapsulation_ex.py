
class Employee:
    # STATE --> data members  *  logical
    def __init__(self, eid, name, sal):
        self.eid = eid
        self.name = name
        self.sal = sal

    # BEHAVIOR --> member methods   * physical
    def get_details(self):
        print("Employee details")

# Employee.get_details()
obj = Employee(1001,'MadhuN',10000)   # data physical methods logical
obj.get_details()
'''
Class   - Variables - Logical    <===>  Methods  - Physical
Object  - Variables - Physical    <===>  Methods  - Logical
 

'''
class Student:
    def __init__(self,id,name,email):
        self.id = id
        self.name = name
        self.email = email
    def student_details(self):
        print("Student details")

object = Student(101,"satish","satish123@gmail.com")
object.student_details()

list1 = [1,2,3,4,5,6,7,8,9]
for i in list1:
    if(i % 2 != 0):
        print(i)

