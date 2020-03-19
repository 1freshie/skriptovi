class Person:
    def __init__(self, name, age, surname):
        self.age = age
        self.name = name
        self.surname = surname

    def __add__(self, other_obj):
        return self.name + self.surname 

    def __sub__(self, other_obj):
        return self.age - other_obj.age
    
    def __mul__(self, other_obj):
        return self.age * other_obj.age
    
    def __radd__(self, age):
        print(age)
        return self.age + age


p1 = Person("Goshko", 15, "Goshkov")
p2 = Person("Ivan", 14, "Ivanov")
print(p1 + p1)
