''' Создайте базовый класс "Человек" со свойствами "имя", "возраст" и "пол". От этого
класса унаследуйте классы "Мужчина" и "Женщина" и добавьте в них свойства,
связанные с социальным положением (например, "семейное положение",
"количество детей" и т.д.).'''
class People:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

class Woman(People):
    def family_status(self):
        return f"Женщина: {self.name } {self.age}, замужем"

    def amount_of_children(self):
        return f"Количество детей: 2"
class Man(People):
    def family_status(self):
        return f"Мужчина: {self.name} {self.age}, разведен "

    def amount_of_children(self):
        return f"Количество детей: 1"

w = Woman('Саша','29','Ж')
print(w.family_status())
print(w.amount_of_children())
m = Man('Максим','42','М',)
print(m.family_status())
print(m.amount_of_children())
