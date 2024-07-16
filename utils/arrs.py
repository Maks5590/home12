def get(array, index, default=None):
    """
    Извлекает из списка значение по указанному индексу, если индекс существует.
	@@ -11,13 +8,13 @@ def get(array, index, default=None):
    :param default: значение по-умолчанию.
    :return: значение по индексу или значение по-умолчанию.
    """

    if 0 <= index < len(array):
        return array[index]
    return default


def my_slice(coll, start=None, end=None):
    """
    Возвращает новый массив, содержащий копию части исходного массива.
    :param coll: исходный список.
	@@ -27,19 +24,20 @@ def my_slice(coll, start=0, end=None):
    Если индекс отрицательный, end указывает смещение от конца списка. По умолчанию равен длине исходного списка.
    :return: массив элементов
    """

    length = len(coll)

    if length == 0:
        return []

    if start is None:
        normalized_start = 0
    else:
        normalized_start = start

    if end is None or end > length:
        normalized_end = length
    else:
        normalized_end = end

    return coll[normalized_start:normalized_end]