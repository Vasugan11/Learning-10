import time
import threading

class Thread:
    pass
class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.power = power
        self.name = name

    def run(self):
        count = 0
        s = 100
        print(f'{self.name}, на нас напали!')
        while s > 0:
            time.sleep(1)
            s = s - self.power
            count += 1
            print(f'{self.name} сражается {count} дней, осталось {s} воинов.' )
        if s == 0:
            print(f'{self.name} одержал победу спустя {count} дней!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()

print('Все битвы закончились!')
