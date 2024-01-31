from typing import Iterable, List

def transform(iterable: Iterable) -> List:
    result = []
    current_level = result
    for item in iterable:
        current_level.append(item)
        current_level.append([])
        previous_level = current_level
        current_level = current_level[-1]
    previous_level.pop() 
    return result
# ввод данных
input_data = input("Введите последовательность чисел через пробел: ")
# преобразование строки в целочисл список
input_list = [int(x) for x in input_data.split()]
result = transform(input_list)
print(result)