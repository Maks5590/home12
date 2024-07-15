def get(array, index, default=None):

    if index < 0:
        return default
    return array[index]
def my_slice(coll, start=0, end=None):

    length = len(coll)
    if length == 0:
        return []
    normalized_end = length if end is None else end
    normalized_start = start
    if normalized_start < 0:
        if normalized_start < -length:
            normalized_start = 0
        else:
            normalized_start += length

    return coll[normalized_start:normalized_end]