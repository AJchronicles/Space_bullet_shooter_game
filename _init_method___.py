class Student:
    def __init__(self,aname,aage,asalary):
        self.name=aname
        self.age=aage
        self.salary=asalary
    def print_data(self):
        print("name of player is ",self.name,"and age is ",self.age)
        print('in game currency of player is ',self.salary)
    # pass
prateek=Student("prateek",20,340)
chintu=Student("chintu",19,250)
# chintu.name="chintu"
# chintu.age=20
# prateek.name="prateek"
# prateek.age="chintu"
# print(prateek.name)
prateek.print_data()
chintu.print_data()
