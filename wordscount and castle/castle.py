from itertools import groupby
A = [2, 2, 3, 4, 3, 3, 2, 2, 1, 1, 2, 5, 2]

#Додатково рахує кількість замків в долині і на вершині гори
def build_castles(A):
    hills = 0
    valley = 0
    #Почистив від повторюваних символів підряд, адже на результат завдання не впливає
    A = [el for el, _ in groupby(A)]
    #Перебираємо кожний елемент списку
    for i in range(0,len(A),1):
        #Граничний(крайній) елемент зліва
        if i == 0:
            if A[i+1] > A[i]:
                hills+=1
            else:
                valley+=1
        #Граничний(крайній) елемент справа
        elif i == len(A)-1:
            if A[i-1] > A[i]:
                valley+=1
            else:
                hills+=1
        #Якщо i-й елемент менше від числа зліва і справа то рахується долиною
        elif A[i] < A[i+1] and  A[i] < A[i-1]:
            valley += 1
        # Якщо i-й елемент більше від числа зліва і справа то рахується горою
        elif A[i] > A[i+1] and  A[i] > A[i-1]:
            valley += 1
    return 'Кількість замків в долині = ' + str(hills) + '\nКількість замків на вершині гори = ' + str(valley) + \
           '\nЗагальна кількість замків = ' + str(hills+valley)

print(build_castles(A))

#Результатом виконанн має бути загальна кількість замків, тому можна скоротити код
def build_castles1(A):
    castles = 0
    #Почистив від повторюваних символів підряд, адже на результат завдання не впливає
    A = [el for el, _ in groupby(A)]
    #Перебираємо кожний елемент списку
    for i in range(0,len(A),1):
        #Граничний(крайній) елемент зліва
        if i == 0:
            castles+=1
        #Граничний(крайній) елемент справа
        elif i == len(A)-1:
            castles+=1
        #Якщо i-й елемент менше від числа зліва і справа то рахується долиною
        elif A[i] < A[i+1] and A[i] < A[i-1]:
            castles+=1
        # Якщо i-й елемент більше від числа зліва і справа то рахується горою
        elif A[i] > A[i+1] and A[i] > A[i-1]:
            castles+=1
    return 'Кількість замків = ' + str(castles)

print(build_castles1(A))