one = "Привет"
two = "Мир"
def get_summ(one, two, delimeter=' '):
    return str(one) + str(delimeter) + str(two)
a = get_summ(one, two, delimeter=' ')
print(a)