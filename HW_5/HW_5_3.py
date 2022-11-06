a = 'Іі що сало? Ласощіі'


def is_pal(str_1:str)->bool:
    """ Return True if string is palindrome else return False """
    check = [x.casefold() for x in str(str_1) if x.isalnum()]
    return check == check[::-1]


print(is_pal(a))
