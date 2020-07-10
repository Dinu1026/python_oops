class student:

    def __init__(self,name,rollno):
        self.name=name
        self.rollno = rollno
        self.lap1=self.laptop()

    def show(self):
        print(self.name,self.rollno)
        self.lap1.show()

    class laptop:

        def __init__(self):
            self.brand='lenovo'
            self.ram=12
            self.cpu='intel'

        def show(self):
            print(self.brand,self.cpu,self.ram)


a,b=input("enter name and roll no").split()
s1=student(a,b)
s1.show()
lap=student.laptop()
lap.show()