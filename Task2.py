from collections import Counter
print("Ввод")
k = int(input())
print("Введите поле 4x4")
c = Counter(int(x) for _ in range(4) for x in input() if x != ".")
result = sum(x <= 2 * k for x in c.values())
print("Вывод")
print(result)
