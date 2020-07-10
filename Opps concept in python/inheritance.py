class A:
    def feature1(self):
        print('from feature 1')

class B:
    def feature2(self):
        print('from feature 2')

class C(A,B):
    def feature3(self):
        print('from feature 3')



a=A()
b=B()
c=C()
a.feature1()
b.feature2()
c.feature1()
c.feature2()
c.feature3()