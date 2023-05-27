''' Создайте класс "Компьютер" с атрибутами "марка", "процессор" и "оперативная
память". Напишите метод, который выводит информацию о компьютере в формате
"Марка: марка, Процессор: процессор, Оперативная память: память".'''

class Computer:

    def __init__(self, marka, CPU, RAM):
        self.marka = marka
        self.CPU = CPU
        self.RAM = RAM

    def info(self):
       return f"Марка: {self.marka } , Процессор: {self.CPU} , Оперативная память: {self.RAM} "
comp = Computer('HONOR', 'intel', '16gb')
print(comp.info())


