with open('file_1.txt', 'r+') as f:
    pars = f.readlines()
    for i in range(len(pars)):
        try:
            pars[i] = f'{pars[i].rstrip()} = {str(eval(pars[i]))}\n'
        except ZeroDivisionError:
            pars[i] = f'{pars[i].rstrip()} = Error: division or modulo by zero\n'
        print(pars[i], end='') # перевірка даних у консолі
    f.seek(0)
    [f.write(el) for el in pars]