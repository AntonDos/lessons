#  Создать класс Dog. Класс имеет четыре атрибута: height, weight, name, age.
#  Класс имеет три метода: jump, run, bark. Каждый метод выводит сообщение на экран.
#  Создать объект класса Dog, вызвать все методы объекта и вывести на экран все его атрибуты.


class Dog:
    def __init__(self, height, weight, name, age):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age


    def jump(self):
        print(f"{self.name} is jumping")


    def run(self):
        print(f"{self.name} is running")


    def bark(self):
        print(f"{self.name} is barking")


dog = Dog(height=100, weight=100, name="Bob", age=10)
dog.jump()
dog.run()
dog.bark()

