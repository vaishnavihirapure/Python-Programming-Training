# Online Python compiler (interpreter)
# Write and run Python online using this editor.

list1=[1,2,3,4,1,2,5,6,3,6,7]
list2=[]
for i in list1:
  if i not in list2:
    list2.append(i)
print(list2)

num=123
a = num % 10
b = (num // 10 ) % 10
c = num // 100
reverse = a*100+b*10+c
print(reverse)

class Student:
  def show(self):
    print("I am hungry")
obj=Student()
obj.show()
Student().show()


class student:
  def __init__(self):
    print("I am a default constructer")
  def show(self):
    print(" I am in student class")

obj=student()
obj.show()

class MyPython:
  def __init__(self):
    print("First constructer")
  def __init__(self):
    print(" Second Constructor") #in this type of question where there are 2 constructor the system will give priority to the second one 

m=MyPython()

#delet instance variable
class MyPython:
  def __init__(self):
      self.a = 10
      self.b = 20
      self.c = 30
      self.d = 40
  def func(self):
    del self.d

n=MyPython()
print(n.__dict__)
n.func()
print(n.__dict__)
del n.c
print(n.__dict__)


class MyPython:
  def __init__(self):
    print(" constructer is called")
  def __init__(self):
    print(" Destructor is called")
  def func(self):
    print(" Func code execution")

m1=MyPython()
m1.func()


#Static Variable
class MyPython:
  x=10               #Static Variable
  def __init__(self):
      self.y=20       #instance variable

m1=MyPython()
m2=MyPython()
print("m1 -->",m1.x,m1.y) 
print("m2 -->",m2.x,m2.y) 
MyPython.x=222
m1.y=111
print("m1 -->",m1.x,m1.y) 
print("m2 -->",m2.x,m2.y) 


#local variables
class Test:
    def func1(self):
      a=100
      print(a)

    def func2(self):
      b=222
     # a=333
      print(b)
      print(a)

t=Test()
t.func1()
t.func2()


#local variables
class Test:
    def func1(self):
      a=100
      print(a)

    def func2(self):
      b=222
      a=333
      print(b)
      print(a)

t=Test()
t.func1()
t.func2()


#QUESTION: Accept 5 paper marks, roll.no,name; and calculate total & percentage if percentage >=85, student can take admisiion else can;t take admission , using class & object & constructor 
class Student:
    def __init__(self, rollno, name, m1, m2, m3, m4, m5):
        self.rollno = rollno
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.m4 = m4
        self.m5 = m5

    def calculate(self):
        total = self.m1 + self.m2 + self.m3 + self.m4 + self.m5
        percentage = total / 5

        print("Roll No:", self.rollno)
        print("Name:", self.name)
        print("Total:", total)
        print("Percentage:", percentage)

        if percentage >= 85:
            print("Student can take admission")
        else:
            print("Student can't take admission")


s1 = Student(18, "Vaishnavi", 90, 85, 88, 92, 86)
s1.calculate()


#single level inheritance
class A:
  def showA(self):
    print("showA function ")
    
class B(A):
  def showB(self):
      print("showB funcion")

obj=B()
obj.showA()
obj.showB()


#multiple level inheritance
class A:
  def showA(self):
    print("showA function ")
    
class B(A):
  def showB(self):
      print("showB funcion")

class C(B):
  def showC(self):
    print("showC funcion")

obj=C()
obj.showA()
obj.showB()
obj.showC()


#hybrid inheritance 
class A:
    def showA(self):
        print("showA function")


class B(A):
    def showB(self):
        print("showB function")


class C(A):
    def showC(self):
        print("showC function")


class D(B, C):
    def showD(self):
        print("showD function")


obj = D()

obj.showA()
obj.showB()
obj.showC()
obj.showD()


#hierarchal inheritance 
class D:
    def showD(self):
        print("D function")


class A(D):
    def showA(self):
        print("A function")


class B(D):
    def showB(self):
        print("B function")


class C(D):
    def showC(self):
        print("C function")


obj1 = A()
obj2 = B()
obj3 = C()

obj1.showD()
obj1.showA()

obj2.showD()
obj2.showB()

obj3.showD()
obj3.showC()

#overriding method 
class Parent:
    def bike(self):
        print("Splender +")


class Child(Parent):
    def bike(self):
        print("HB")


obj = Child()
obj.bike()


    


    


