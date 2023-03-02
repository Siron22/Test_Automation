"""1. Написать функцию, которая генерируют в директории `directory` `number_of_files` файлов.
Содержимое файлов должно быть случайным, состоять из больших/маленьких латинских букв, цифр и символов пунктуации.
Файл должен содержать случайное число символов в диапазоне от `size/2` до `size` символов.
def file_generator(directory, number_of_files, size)
    Осторожно: file_generator('files', 200, 1000_000) ~150 Mb
2. Написать функцию (обычную, однопоточную), которая возвращает число букв `letter_to_find` во всех файлах директории `directory`
def letter_counter_in_one_thread(directory, letter_to_find)
3. Написать функцию, которая возвращает число букв `letter_to_find` во всех файлах директории `directory`
Функция должна разбить файлы в директории на `number_of_threads` групп, и чтение/подсчет буквы для каждой группы вести в отдельном потоке.
Группы стоит разбить максимально равно.
def letter_counter_in_n_threads(directory, letter_to_find, number_of_threads)
4. Написать клиентский код, который создает файлы, подсичтывает количество букв функцией в одном потоке и в нескольких потоках, и выводит время выполнения функций.
NOTE: Директорию считаем "плоской" - вложенных директорий нет."""
import  random, string, os, threading, time


def file_generator(directory:str, number_of_files:int, size:int):
    file_counter = 1
    os.mkdir(f'{directory}')
    symbols = string.ascii_letters + string.digits + string.punctuation
    for _ in range(number_of_files):
        text = ''.join(random.choice(symbols) for _ in range(random.randint(size / 2, size)))
        with open(f'./{directory}/file:{file_counter}', 'w') as f:
            f.write(text)
        file_counter+=1


def letter_counter_in_one_thread(directory:str, letter_to_find:str):
    start = time.time()
    letter_counter = 0
    for filename in os.listdir(directory):
        with open(os.path.join(directory, filename), 'r') as f:
            text = f.read()
        letter_counter += text.count(letter_to_find)
    return  f'In all files there is {letter_counter} of symbol << {letter_to_find} >>. ' \
           f'Function with ONE thread calculated it for {time.time() - start} seconds'




def letter_counter_help(directory:str, letter_to_find:str, files:list):
    letter_counter = 0
    for filename in files:
        with open(os.path.join(directory, filename), 'r') as f:
            text = f.read()
        letter_counter += text.count(letter_to_find)
    return  letter_counter


class CustomThread(threading.Thread):

    def __init__(self, group=None, target=None, name=None, args=(), kwargs={}, Verbose=None):
        threading.Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None

    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args, **self._kwargs)

    def join(self, *args):
        threading.Thread.join(self, *args)
        return self._return





def letter_counter_in_n_threads(directory:str, letter_to_find:str, number_of_threads:int):
    start = time.time()
    file_list = []
    for filename in os.listdir(directory):
        file_list.append(filename)
    counter_of_threads = 0
    result = []
    while counter_of_threads < number_of_threads:
        files = file_list[counter_of_threads::number_of_threads]
        thread =  CustomThread(target=letter_counter_help, args=(directory, letter_to_find, files))
        thread.start()
        quantity = thread.join()
        result.append(quantity)
        counter_of_threads+=1
    return f'In all files there is {sum(result)} of symbol << {letter_to_find} >>. ' \
           f'Function with {number_of_threads} threads calculated it for {time.time() - start} seconds'


# def letter_counter_in_n_threads(directory:str, letter_to_find:str, number_of_threads:int):
#     start = time.time()
#     file_list = []
#     for filename in os.listdir(directory):
#         file_list.append(filename)
#     counter_of_threads = 0
#     thread_list = []
#     result = []
#     while counter_of_threads < number_of_threads:
#         files = file_list[counter_of_threads::number_of_threads]
#         thread =  CustomThread(target=letter_counter_help, args=(directory, letter_to_find, files))
#         thread.start()
#         thread_list.append(thread)
#         counter_of_threads+=1
#     for thread in thread_list:
#         quantity = thread.join()
#         result.append(quantity)
#     return f'In all files there is {sum(result)} of symbol << {letter_to_find} >>. ' \
#            f'Function with {number_of_threads} thread_list calculated it for {time.time() - start} seconds'






# file_generator('dir', 100, 1000000)
one_thread = letter_counter_in_one_thread("dir", '!')
n_treads = letter_counter_in_n_threads('dir', '!', 10)
print(one_thread)
print('*' * 40)
print(n_treads)