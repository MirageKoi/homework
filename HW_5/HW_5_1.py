list_1 = [1, 10, 9, 4, 5, 7, 2, 0]
i_1 = 2
i_2 = 6


def sort_list(list_m:list, i1:int ,i2:int, rev:bool=False)->list:
    """Return the list with sorted part in ascending or descending order between indexes i1 and i2"""
    list_m[i1:i2] = sorted(list_m[i1:i2], reverse=rev)
    return list_m


print(sort_list(list_1, i_1, i_2, True))