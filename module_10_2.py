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
        if 100 % self.power != 0:
            print('Измените мощь!')
        else:
            while enemies > 0:
                enemies = enemies - self.power
                time.sleep(1)
                day_count += 1
                print(f'{self.name} сражается {day_count} день(дня), осталось {enemies} воинов.\n')
        print(f'{self.name} одержал победу спустя {day_count} дней(дня)!')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
thread_list = [first_knight, second_knight]
for thread in thread_list:
    thread.start()
for thread in thread_list:
    thread.join()


print('Все битвы закончились!')
