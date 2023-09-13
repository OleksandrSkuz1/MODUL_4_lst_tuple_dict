my_lst = list(range(10))
my_dict = {"name": "Bill", "age": 22}       
my_str = "Hello world"

    # for lst
for i in my_lst[4:8]: #ітерація по списку (можна ітер. по певному зрізу)
    print(i)
    
    # for dict
    
for i in my_dict:    #при кожній ітер. будуть ключі
    print(i)
    
for i in my_dict.values(): # при використ. методу values, при ітер. будуть значення
    print(i)
    
for i in my_dict.items():  # ('name', 'Bill')
                           # ('age', 22)
    print(i)    
    
for k, v in my_dict.items(): # ключі розпакуються в pvsyye к, а знач. в v
    print(k, v)    
    
    # for str
    
for i in my_str:  # при кожній ітерації буде новий символ
    print(i)