def function():
     
    string_one = input("Введите первую строку: ")
    string_two = input("Введите вторую строку: ")
    if string_one == string_two:
        print(1)
    elif string_one != string_two:
        if len(string_one) > len(string_two):
            print(2)
        elif string_two == 'learn':
            print(3)
    
function()