class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.roll_number)
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.brand = "Dell"
            self.cpu = "i6"
            self.ram = 8

        def show(self):
            print(self.brand, self.cpu, self.ram)


s1 = Student("Laurent", 43)
s2 = Student("Lara", 23)

s2.show()
lap1 = Student.Laptop()
lap2 = s2.lap
