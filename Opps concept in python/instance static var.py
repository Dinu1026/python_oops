class car:
    wheel=4 ####static variables

    def __init__(self):
        self.mil=10  ###### non static variables
        self.com="BMW"

c1=car()
c2=car()
c1.mil=5
car.wheel=5
print(c1.mil,c1.com,c1.wheel)
print(c2.mil,c2.com,c2.wheel)