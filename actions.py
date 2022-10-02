# from main import count

def add_data(data):
    # count = 0
    # read = open('employees_initial.txt', 'r', encoding='utf-8')
    # for line in read:
    #     count += 1
    # read.close()
    # print(count)
            
    with open('employees.txt', 'a', encoding='utf-8') as empl:
        identifier = count + 1
        write = empl.write(f'{identifier}, {data}\n')
        count = identifier                                  #  не знаю, как сделать, чтобы счет продолжался от последнего ввода
        identifier = count + 1
        print(identifier)


def view_data():
    # with open('employees.txt', 'r', encoding='utf-8') as empl:    #почему так не работает?
    #     read = empl.read()
    # return read
   
    count = 0
    read = open('employees.txt', 'r', encoding='utf-8')
    for line in read:
        count += 1
        print(line)
    read.close()
    print(count)



def edit_data(undifier, current, new_data):
    file_base = open('employees.txt','r', encoding='utf-8') 
    data_base = file_base.readlines()
    file_base.close()
    for line in data_base:
        if line.startswith(undifier):
            data = line.split(', ')
            data[current] = new_data
            new_line = ', '.join(data)
    else:
        print(" Такого сотрудника нет. ")
