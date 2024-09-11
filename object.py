class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def introduce(self):
        print(f'Hello, my name is {self.name}, i am {self.age} years old and i am a {self.gender}')

abdulbasit = Person('Abdulbasit', 30, 'male')
abdulbasit.introduce()