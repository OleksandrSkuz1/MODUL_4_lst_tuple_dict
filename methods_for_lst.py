# APPEND

my_var = list(range(10))
print(len(my_var))

my_var.append(range(1000))
print(len(my_var))
print(my_var[-1])
print(my_var[-1])


# INDEX (шукає ел-т за індексом)
my_str_list = ["ab", "b", "c", "b"]

print(my_str_list.index("b", 2))


# INSERT (приймає індекс і вставляє ел-т за цим індексом)
my_str_list.insert(100, "f")

print(my_str_list)


# REMOVE (видаляє ел-т за значеннм. Перше його входження в списку!)
my_str_list.remove("b")

print(my_str_list)


# POP (видаляє останній ел-т)

print(my_str_list.pop())

print(my_str_list)