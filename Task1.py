import random
print("Укажите количество домов на улице!")
try:
    Colhome = int(input())
    if Colhome>0:
        street =random.sample(range(0,10**9),Colhome)
        street.append(0)
        print(*street,sep=' ')
        if 0 in street:
            n =len(street)
            mass = [i for i in range(n)  if street[i]==0]
            i0=mass[0]
            i1 = mass[-1] if len(mass) ==1 else mass[1]
            for i in range(i0):
                street[i]= i0-i
                #print(street[i])
            m = 1
            for i in range(i0+1, mass[-1]):
                if street[i]:
                    street[i] = min(i - i0, i1 - i)
                else:
                    m += 1
                    i0 = i1
                    i1 = mass[m]
            for i in range(i1+1, n):
                street[i] = i - i1
                print(street[i])   
            print(*street,sep=' ')  
        else:
            print("В массиве нет нуля")
    else:
        print("Длина не может быть 0 или отрицательной")
except ValueError:
    print("Неверный формат в вода, в водить надо число")