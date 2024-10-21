from threading import Thread
import time

class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power


    def run(self):
        enemies = 100
        day_count = 0
        print(f'{self.name}, на нас напали!')
        while enemies != 0:
            enemies = enemies - self.power
            time.sleep(1)
            day_count += 1
            print(f'{self.name} сражается {day_count} день(дня), осталось {enemies} воинов.')
        print(f'{self.name} одержал победу спустя {day_count} дней(дня)!')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

"""for _ in range(2):
    first_knight.start()
    second_knight.start()
for _ in range(2):
    first_knight.join()
    second_knight.join()
    Почему-то когда запускаю потоки через цикл, вылетает ошибка RuntimeError if called more than once,
    а в случае с рабочим кодом ниже все нормально (за исключением отсутствия переноса строки в одном месте),
     хотя судя по консоли они запускаются в одно время
    """
first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()



print('Все битвы закончились!')
