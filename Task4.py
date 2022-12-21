# PythonStudy
Обучение новому языку программирования домашние задания 
print("Введите входной параметр")
number = int(input())
if 0<number<=100:
    source_array = input().split(' ')
    for i in range(number - 1):
        for j in range(0, number-i-1):
            var1 = source_array[j] + source_array[j+1]
            var2 = source_array[j + 1] + source_array[j]
            if var1 < var2:
                source_array[j], source_array[j+1] = source_array[j+1], source_array[j]
                    
    print("".join(source_array))
else:
    print("Входной параметр должен быть в промежутке от [0.....100]")
