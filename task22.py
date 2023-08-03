mn1=set(input("Введите первое множество чисел через пробел: ").split())
mn2=set(input("Введите второе множество чисел через пробел: ").split())
peres = mn1 & mn2
peres = list(peres)
print(peres)
