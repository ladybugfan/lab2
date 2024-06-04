import random

class Interpreter:
    
    def __init__(self):
        self.arrays = {}

    def load(self, array_name, file_name):
        try:
            with open(file_name, 'r') as file:
                data = file.read().split()
                data = [x for x in data if x.isdigit()]

                if array_name in self.arrays:
                    choice = input(f"Массив {array_name} уже существует. Перезаписать? (да/нет): ").lower()

                    if choice == 'нет':
                        print("Операция отменена.")
                        return

                self.arrays[array_name] = data
                print(f"Массив {array_name} загружен из файла {file_name}")
                
        except FileNotFoundError:
            print(f"Ошибка: Файл {file_name} не найден")
        except Exception as e:
            print(f"Ошибка: {e}")
            
            
    def save(self, array_name, file_name):
        try:
            array = self.arrays.get(array_name)
            if array is None:
                print(f"Массив {array_name} не найден")
                return

            with open(file_name, 'w') as file:
                file.write(' '.join(map(str, array)))
                
            print(f"Массив {array_name} сохранен в файл {file_name}")
            
        except FileNotFoundError:
            print(f"Файл {file_name} не найден")
        except Exception as e:
            print(f"Ошибка при сохранении: {e}")
        
        
        
        
    def rand(self, array_name, count, lb, rb):
        try:

            if not isinstance(lb, int) or not isinstance(rb, int):
                raise ValueError("lb и rb должны быть целыми числами")
            if lb > rb:
                raise ValueError("lb должен быть меньше или равен rb")

            self.arrays[array_name] = [random.randint(lb, rb) for _ in range(count)]
            print(f"Массив {array_name} заполнен случайными числами от {lb} до {rb}")
            
        except ValueError as ve:
            print(f"Ошибка: {ve}")
            
        except Exception as e:
            print(f"Ошибка: {e}")
    
    
    
    def concat(self, array_name_1, array_name_2):
        try:
            array_1 = self.arrays.get(array_name_1)
            array_2 = self.arrays.get(array_name_2)
            
            if array_1 is None:
                print(f"Массив {array_name_1} не найден")
                return
            if array_2 is None:
                print(f"Массив {array_name_2} не найден")
                return
            
            array_1 += array_2
            print(f"Массив {array_name_1} сконкатенирован с массивом {array_name_2}")

        except Exception as e:
            print(f"Ошибка при конкатенации массивов: {e}")
        
    def free(self, array_name):
        try:

            array = self.arrays.get(array_name)
            if array is None:
                print(f"Массив {array_name} не найден")
                return
            
            while array:
                array.pop()
                
            print(f"Массив {array_name} очищен")
            
        except Exception as e:
            print(f"Ошибка при очистке массива: {e}")





    def remove(self, array_name, start_index, count):
        try:
            array = self.arrays.get(array_name)
            if array is None:
                print(f"Массив {array_name} не найден")
                return

            if start_index < 0:
                start_index += len(array)
            
            if not isinstance(start_index, int) or start_index >= len(array):
                raise ValueError("Некорректное значение начального индекса")

            if not isinstance(count, int) or count < 0:
                raise ValueError("Количество удаляемых значений должно быть целым неотрицательным числом")
            
            if start_index + count > len(array):
                count = len(array) - start_index
                print("Количество элементов для удаления больше количество доступных элементов в массиве. "
                    f"Будет удалено только {count} элементов")
            
            del array[start_index:start_index + count]
            
            print(f"Из массива {array_name} удалено {count} элементов")
        except ValueError as ve:
            print(f"Ошибка: {ve}")
        except Exception as e:
            print(f"Ошибка: {e}")





    def copy(self, array_name_A, start_index, end_index, array_name_B):
        try:
            array_A = self.arrays.get(array_name_A)
            if array_A is None:
                print(f"Массив {array_name_A} не найден")
                return
            
            if not isinstance(start_index, int) or start_index < 0 or start_index >= len(array_A):
                raise ValueError("Некорректное начальное значение")
            if not isinstance(end_index, int) or end_index < 0 or end_index >= len(array_A):
                raise ValueError("Некорректное конечное значение")
            if start_index > end_index:
                raise ValueError("Начальное значение должно быть меньше или равно конечному значению")
            
            array_B = self.arrays.get(array_name_B, [])
            
            if array_B is None:
                print(f"Массив {array_name_B} не найден")
                return
            
            array_B.extend(array_A[start_index:end_index + 1])
            self.arrays[array_name_B] = array_B
            print(f"Из массива {array_name_A} скопированы элементы с {start_index} по {end_index} в массив {array_name_B}")
            
        except ValueError as ve:
            print(f"Ошибка: {ve}")
        except Exception as e:
            print(f"Ошибка: {e}")
            
            
            
    def sort(self, array_name, order='+'):
        try:
            array = self.arrays.get(array_name)
            if array is None:
                print(f"Массив {array_name} не найден")
                return
            
            def quick_sort(arr):
                if len(arr) <= 1:
                    return arr
                middle = int(arr[len(arr) // 2])
                less = [int(x) for x in arr if (int(x) < middle if order == '+' else int(x) > middle)]
                equal = [int(x) for x in arr if x == middle]
                greater = [int(x) for x in arr if (int(x) > middle if order == '+' else int(x) < middle)]
                return quick_sort(less) + equal + quick_sort(greater)
            
           
            sorted_array = quick_sort(array)
            
            self.arrays[array_name] = sorted_array
            
            print(f"Массив {array_name} отсортирован {'по неубыванию' if order == '+' else 'по невозрастанию'}")
        except Exception as e:
            print(f"Ошибка при сортировке массива: {e}")



    def shuffle(self, array_name):
        try:
            array = self.arrays.get(array_name)
            if array is None:
                print(f"Массив {array_name} не найден")
                return

            random.shuffle(array)
            print(f"Элементы массива {array_name} переставлены в псевдослучайном порядке")
            
        except Exception as e:
            print(f"Ошибка при перестановке элементов массива: {e}")


    def stats(self, array_name):
        try:
            array = self.arrays.get(array_name)
            if array is None:
                print(f"Массив {array_name} не найден")
                return

            size = len(array)

            max_elem = max(array)
            max_index = array.index(max_elem)
            min_elem = min(array)
            min_index = array.index(min_elem)

            most_common_elem = max(set(array), key=array.count)

            average = sum(array) / size

            max_deviation = max(abs(elem - average) for elem in array)

            print(f"Статистика для массива {array_name}:")
            print(f"Размер массива: {size}")
            print(f"Максимальный элемент: {max_elem} (индекс: {max_index})")
            print(f"Минимальный элемент: {min_elem} (индекс: {min_index})")
            print(f"Наиболее часто встречающийся элемент: {most_common_elem}")
            print(f"Среднее значение элементов: {average}")
            print(f"Максимальное отклонение элементов от среднего значения: {max_deviation}")

        except Exception as e:
            print(f"Ошибка при вычислении статистики для массива: {e}")
    

    def print_element(self, array_name, index):
        try:
            if not isinstance(index, int):
                raise ValueError("Индекс должен быть целым числом")
            array = self.arrays.get(array_name)
            if array is None:
                print(f"Массив {array_name} не найден")
                return

            if not 0 <= index < len(array):
                print(f"Индекс {index} выходит за пределы массива {array_name}")
                return

            print(f"Элемент массива {array_name} с индексом {index}: {array[index]}")

        except ValueError as ve:
            print(f"Ошибка: {ve}")
        except Exception as e:
            print(f"Ошибка при выводе элемента массива: {e}")


    def print_range(self, array_name, start_index, end_index):
        try:
            if not isinstance(start_index, int) or not isinstance(end_index, int):
                raise ValueError("Индексы должны быть целыми числами")

            array = self.arrays.get(array_name)
            if array is None:
                print(f"Массив {array_name} не найден")
                return

            if not (0 <= start_index <= end_index < len(array)):
                print("Некорректные индексы")
                return

            print(f"Элементы массива {array_name} с {start_index} по {end_index}: {', '.join(map(str, array[start_index:end_index+1]))}")

        except ValueError as ve:
            print(f"Ошибка: {ve}")
        except Exception as e:
            print(f"Ошибка при выводе элементов массива: {e}")

    def print_all(self, array_name):
        try:
            array = self.arrays.get(array_name)
            if array is None:
                print(f"Массив {array_name} не найден")
                return

            if not array:
                print(f"Массив {array_name} пуст")
                return

            print(f"Все элементы массива {array_name}: {', '.join(map(str, array))}")

        except ValueError as ve:
            print(f"Ошибка: {ve}")
        except Exception as e:
            print(f"Ошибка при выводе элементов массива: {e}")


interpreter = Interpreter()

interpreter.load('A', 'lab2/in.txt')
interpreter.save('A', 'lab2/out.txt')

interpreter.load("B", 'lab2/in.txt')

interpreter.save("B", "lab2/saved_data.txt")

interpreter.rand("C", 10, 1, 100)

interpreter.concat("B", "C")

interpreter.remove("C", 3, 5)

interpreter.copy("C", 2, 4, "B")

# по неубыванию
interpreter.sort("B", '+')

interpreter.shuffle("B")

interpreter.stats("B")

interpreter.print_element("B", 3)

interpreter.print_range("B", 2, 6)

interpreter.print_all("B")
