mylist = {'Andrey' : {"sity" : "Moscow" , "temperature" : 1 , "wind" : "west"}, 
            'Max' : {"sity" : "Chehov" , "temperature" : 2 , "wind" : "nord"} ,
            'Sergey' : {"sity" : "Serpuhov" , "temperature" : 3 , "wind" : "west"}}
name = input('Как Вас зовут? ')
b = mylist.get(name)
a = '{0},{1},{2}'.format(b["sity"],b["temperature"],b["wind"])
print(a)
a = str(mylist.get(name).values())
print(a)