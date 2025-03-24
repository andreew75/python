# Костромин Андрей Львович

full_list = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
my_list = []

for i in full_list:
    if full_list.count(i) == 1:
        my_list.append(i)

print(my_list)
