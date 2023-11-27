# Задача №1
# Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
# сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки

# Императивный стиль (пишем тело функции сами, имея доступ к памяти)
def bubbleSortImperative(list1): 
    for i in range(0, len(list1) - 1): 
        for j in range(len(list1) - 1): 
            if(list1[j] < list1[j + 1]): 
                temp = list1[j] 
                list1[j] = list1[j + 1] 
                list1[j + 1] = temp 
    return list1 
 
# Декларативный стиль (используем встроенные функции "под капотом")
def bubbleSortDeclarative(list2):
    return sorted(list2, reverse = True) 


testList = [9, 5, 3, 8, 6, 7, 2, 0, 1] 
print("The unsorted list is: ", testList) 
print("The sorted list (1st version Imperative) is: ", bubbleSortImperative(testList)) 
print("The sorted list (2nd version Declarative) is: ", bubbleSortDeclarative(testList)) 
