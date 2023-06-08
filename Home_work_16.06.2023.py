# 1. При старте приложения запускаются три процесса.
# Первый процесс заполняет список случайными числами.
# Два других процесса ожидают заполнения. Когда список
# заполнен оба процесса запускаются. Первый процесс находит
# сумму элементов списка, второй процесс среднеарифметическое значение в списке.
# Полученный список, сумма и среднеарифметическое выводятся на экран.
import dataclasses
# import multiprocessing
# import random
#
#
# def get_spisok(spisok, locker):
#     locker.acquire()
#     spisok = [random.randint(100, 1000) for i in range(2000)]
#     print(spisok)
#     print(f'Процесс {multiprocessing.current_process().name} выполнен')
#     locker.release()
#     return spisok
#
#
# def get_summa(spisok):
#     print(sum(spisok))
#     print(f'Процесс {multiprocessing.current_process().name} выполнен')
#
#
# def get_mean(spisok):
#     print(sum(spisok) / len(spisok))
#     print(f'Процесс {multiprocessing.current_process().name} выполнен')
#
#
# if __name__ == '__main__':
#     numbers = [random.randint(100, 1000) for i in range(2000)]
#     locker = multiprocessing.RLock()
#     pr1 = multiprocessing.Process(target=get_spisok, name='Spisok', args=(numbers, locker))
#     pr2 = multiprocessing.Process(target=get_summa, name='Summa', args=(numbers,))
#     pr3 = multiprocessing.Process(target=get_mean, name='Mean', args=(numbers,))
#     pr1.start()
#     pr2.start()
#     pr3.start()


# 2. Пользователь с клавиатуры вводит путь к файлу.
# После чего запускаются три процесса. Первый процесс заполняет файл случайными числами.
# Два других процесса ожидают заполнения. Когда файл заполнен оба процесса
# стартуют. Первый процесс находит все простые числа, второй процесс факториал каждого
# числа в файле. Результаты поиска каждый процесс должен записать в новый файл. На
# экран необходимо отобразить статистику выполненных операций.

# import multiprocessing
# import random
# import datetime
# from math import factorial
#
#
# def get_spisok(spisok, filename, locker):
#     locker.acquire()
#     print(spisok)
#     text = f'{str(spisok)}\n'
#     with open(filename, 'a', encoding='utf-8') as f:
#         f.write(text)
#     text_log = f'Процесс {multiprocessing.current_process().name} выполнен {datetime.datetime.now()}\n'
#     # print(text_log)
#     with open('2.txt', 'a', encoding='utf-8') as f:
#         f.write(text_log)
#     locker.release()
#
#
# def get_simple(spisok):
#     res = [x for x in spisok if all(x % t for t in range(2, (x // 2 + 1)))]
#     text_log = f'Процесс {multiprocessing.current_process().name} выполнен {datetime.datetime.now()} с результатом {res}\n'
#     # print(text_log)
#     with open('2.txt', 'a', encoding='utf-8') as f:
#         f.write(text_log)
#
#
# def get_factorial(spisok):
#     res = list(map(factorial, spisok))
#     text_log = f'Процесс {multiprocessing.current_process().name} выполнен {datetime.datetime.now()} с результатом {res}\n'
#     # print(text_log)
#     with open('2.txt', 'a', encoding='utf-8') as f:
#         f.write(text_log)
#
#
# if __name__ == '__main__':
#     file_name = input('Введите путь к файлу: ')
#     numbers = [random.randint(10, 50) for i in range(20)]
#     locker = multiprocessing.RLock()
#     pr1 = multiprocessing.Process(target=get_spisok, name='Spisok', args=(numbers, file_name, locker))
#     pr2 = multiprocessing.Process(target=get_simple, name='Simple', args=(numbers, ))
#     pr3 = multiprocessing.Process(target=get_factorial, name='Factorial', args=(numbers,))
#     pr1.start()
#     pr1.join()
#     pr2.start()
#     pr3.start()
#
#
# with open('2.txt', 'r', encoding='utf-8') as file:
#     print(file.read())
