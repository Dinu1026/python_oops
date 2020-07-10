class student:
    school="telusko"
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def avg(self):                               ## non static or instance method
        print("avg is:",self.m1+self.m2+self.m3/3)
    @classmethod
    def getschool(cls):
        print(cls.school)

    @staticmethod
    def info():
        print("this is student class")


s1=student(24,59,75)
s2=student(52,86,41)
s1.avg()
s2.avg()
s1.getschool()
s2.getschool()
student.info()