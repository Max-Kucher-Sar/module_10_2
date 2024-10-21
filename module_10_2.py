from threading import Thread
import time

class Knight(Thread):
    def __init__(self, name, power):
        self.name = name
        self.power = power
        super().__init__()

    def run(self):
        enemies = 100
        day_count = 0
        print(f'{self.name}, на нас напали!')
        while enemies != 0:
            enemies = enemies - self.power
            time.sleep(1)
            day_count += 1
            print(f'{self.name} сражается {day_count}, осталось {enemies} воинов.')
        print(f'{self.name} одержал победу спустя {day_count} дней(дня)!')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
first_knight.join()
second_knight.start()
second_knight.join()
print('Все битвы закончились!')
