def unique_elements(input_list):
    unique_list = []

    for num in input_list:
        # Проверяем, есть ли текущий элемент в списке уникальных элементов
        if num not in unique_list:
            # Если элемент не найден, добавляем его в список уникальных элементов
            unique_list.append(num)

    # Возвращаем список уникальных элементов
    return unique_list
