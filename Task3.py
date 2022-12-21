# PythonStudy
print("Введите входной параметр5")
n = int(input())
if 0<n<10:
    n *= 2
    for mask in range(1 << n):
        balance, is_good, answer = 0, True, ''
        for bit in range(n):
            if (mask >> bit) & 1:
                balance += 1
                answer += '('
            else:
                balance -= 1
                if balance < 0:
                    is_good = False
                    break
                answer += ')'
        if is_good and balance == 0:
            print(answer)
else:
    print("Входной параметр должен быть в промежутке от [0.....10]")
