from random import randint
import time
import threading

class Thread:
    pass

lock = threading.Lock()
balance = 0
class Bank(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.balance = balance
        self.lock = lock

    def deposit(self):
        global balance
        for i in range(100):
            addition = randint(100, 500)
            if balance >= 500 and self.lock.locked():
                self.lock.release()
            self.balance = self.balance + addition
            print(f'Пополнение: {addition} Баланс: {self.balance}')
            time.sleep(0.001)


    def take(self):
        global balance
        for i in range(100):
            withdrawal = randint(50, 100)
            print(f'Запрос на {withdrawal}')
            if withdrawal <= self.balance:
                self.balance = self.balance - withdrawal
                print(f'Снятие:{withdrawal} Баланс:{self.balance}')
                time.sleep(0.001)
            else:
                print('Запрос отклонен, недостаточно средств')
                time.sleep(0.001)
                self.lock.acquire()

bk = Bank()

deposit = threading.Thread(target=Bank.deposit, args=(bk,))
take =  threading.Thread(target=Bank.take, args=(bk,))

deposit.start()
take.start()
deposit.join()
take.join()

print(f'Итоговый баланс: {bk.balance}')