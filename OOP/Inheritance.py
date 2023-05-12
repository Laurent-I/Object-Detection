class A:

    def __init__(self):
        print("A in init")

    def feature1(self):
        print("Feature one")

    def feature2(self):
        print("Feature two")


class B(A):

    def __init__(self):
        print("in B init")

    def feature1(self):
        print("Feature three")

    def feature4(self):
        print("Feature 4 working")


class C(B, A):
    def __init__(self):
        super().__init__()
        print("in C init")


a1 = C()
a1.feature1()
