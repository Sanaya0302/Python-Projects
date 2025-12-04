class person(object):
    def __init__(self,name,idnum):
        self.name=name
        self.idnum=idnum
    def display(self):
        print(self.name,self.idnum, end="\n")
class employee(person):
    def __init__(self,name,idnum,salary,role):
        self.role=role
        self.salary=salary
        super().__init__(name,idnum)
a=employee("Sanaya",5678,100000,"computer engineer")
a.display()
print(issubclass(employee,person))