team = str(input('Введите фразу: '))
if team == 'mystic':
    print('Hi, blue team')
    user_level = int(input('Введите уровень: '))
    if user_level >= 5:
        print('Welcome to the gym')
    else:
        print('Get more exp')
    
elif team == 'instinct':
    print('Hi, yellow team')
elif team == 'valor':
    print('Hi, red team')
