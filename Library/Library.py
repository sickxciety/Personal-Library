import os

def sec_num(lst, num):
    for i in lst:
        if num.isdigit() and num in i[0]:
            return True
            break
    else:
        print('Введите номер, доступный в списке!')

def add_book():
    autors_name = {}
    actions = ['1. Добавить к автору', '2. Добавить нового автора']
    print('Выберите действие:', *actions, sep='\n')
    
    while True:
        num = input()
        if sec_num(actions, num):
            num = int(num)
            break
        
    if num == 2:
        autor = input('Введите имя автора: ')
        if os.path.exists(f'books/{autor}.txt') == False:
            with open(f'books/{autor}.txt', 'a') as file:
                file.write('*' * 20 + '\n')
                file.write(f'Автор: {autor}\n')
                file.write('*' * 20 + '\n')
                
    elif num == 1:
        autors = [f'{i+1}. {n[0:-4]}' for i, n in enumerate(os.listdir('books'))]
        print(f'Выберите автора:\n')
        for i, name in enumerate(autors):
            autors_name[i+1] = name[3:]
            print(f'{name}\n')
            
        while True:
            num = input('Выберите номер автора: ')
            if sec_num(autors, num):
                num = int(num)
                autor = autors_name[num]
                break
            
    book = input('Введите название произведения: ')
    genre = input('Введите жанр: ')
    rating = input('Введите свою оценку (1-5): ')
    review = input('Введите свой отзыв: ')

    collect = {'book': book, 'genre': genre, 'rating': rating, 'review': review}

    with open(f'books/{autor}.txt', 'a') as file:
        file.write(f'Произведение: {collect['book']}\n')
        file.write(f'Жанр: {collect['genre']}\n')
        file.write(f'Оценка: {collect['rating']}\n')
        file.write(f'Отзыв: {collect['review']}\n')
        file.write('-' * 20 + '\n')

    actions = ['1. Добавить ещё', '2. Посмотреть добавленное', '3. Назад']
    print('Выберите действие: ', *actions, sep='\n')
    
    while True:
        num = input()
        if sec_num(actions, num):
            num = int(num)
            break
        
    while True:
        if num == 1:
            add_book()
            break
        elif num == 2:
            look_books()
            break
        elif num == 3:
            break

def look_books():
    autors = [n for n in os.listdir('books')]
    books = []
    for i in autors:
        with open(f'books/{i}', 'r') as file:
            for line in file:
                books.append(line.strip())
    print(*books, sep='\n')

    actions = ['1. Добавить ещё', '2. Назад']
    print('Выберите действие: ', *actions, sep='\n')
    
    while True:
        num = input()
        if sec_num(actions, num):
            num = int(num)
            break
        
    while True:
        if num == 1:
            add_book()
            break
        elif num == 2:
            break

actions = ['1. Добавить книгу', '2. Посмотреть добавленное', '3. Выход']
action = {1: add_book, 2: look_books}

while True:
    print('Выберите действие: ', *actions, sep='\n')
    num = input()
    if sec_num(actions, num):
        num = int(num)
        if num == 1 or num == 2:
            action[num]()
        elif num == 3:
            break
