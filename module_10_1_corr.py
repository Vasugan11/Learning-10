import threading
import time

def write_words(word_count, file_name):
    file = open(file_name, 'w', encoding = 'utf-8')
    for i in range(word_count):
        file.write(f'воробей № {i}' +'\n')
        time.sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')
    file.close()

a = (time.time())

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
b = time.time()
print(f'Работа функций {b - a}')

thread = threading.Thread()
thread.start()
thread.join()

thread1 = threading.Thread(target = write_words, args = (10, 'example5.txt'))
thread2 = threading.Thread(target = write_words, args = (30, 'example6.txt'))
thread3 = threading.Thread(target = write_words, args = (200, 'example7.txt'))
thread4 = threading.Thread(target = write_words, args = (100, 'example8.txt'))

c = time.time()
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread1.join()
thread2.join()
thread3.join()
thread4.join()
d = time.time()
print(f'Работа потоков {d - c}')