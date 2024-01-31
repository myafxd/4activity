


def round_dance(iterable):
    # Находим минимальный элемент и его индекс
    min_element = min(iterable)
    min_index = iterable.index(min_element)

    # Проверяем, соответствует ли порядок элементов правильному хороводу
    n = len(iterable)
    for i in range(n):
        if iterable[(min_index + i) % n] != min_element + i:
            return False
    return True


def main():
    with open('input.txt', 'r') as file:  # Открытие файла для чтения
        input_data = file.readline().strip().split()  # Чтение данных из файла
    participants = list(map(int, input_data))
    result = round_dance(participants)  # Проверка хоровода

    with open('output.txt', 'w') as file:  # Открытие файла для записи
        file.write(str(result))  # Запись результата (True или False) в файл


if __name__ == "__main__":
    main()
