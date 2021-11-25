class A:
    def a(self):
        print("A类方法")
    pass

class B:
    def b(self):
        print("B类方法")

    pass

class C(A,B):
    pass

c = C();
c.a()
c.b()