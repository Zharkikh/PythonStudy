# PythonStudy
Обучение новому языку программирования домашние задания 
lis = [55,57,7,48,73,5,79]
#lis.sort(key=lambda x: (int(str(x)[0]), int(str(x)[1])),reverse=True)
import operator
list1 = sorted(lis, key=lambda x: (int(str(x)[0])))
list1.reverse()
print(list1)
