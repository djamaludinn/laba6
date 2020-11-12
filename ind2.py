#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Вариант1
#В списке, состоящем из вещественных элементов, вычислить:
#1) сумму отрицательных элементов списка;
#2) произведение элементов списка, расположенных между максимальным и минимальным элементами.
#Упорядочить элементы списка по возрастанию.

if __name__ == '__main__':
    A = list(map(float, input("Ввод:" ).split()))
    res = 0
# 1)
    for i in A:
        if i < 0:
            res += i
    print(f'1) {res:.2f}')

# 2)
    S = []
    a_min = a_max = A[0]
    i_min = i_max = 0
    b = [abs(i) for i in A]
    for i, item in enumerate(b):
        if item < a_min:
            i_min, a_min = i, item
        if item >= a_max:
            i_max, a_max = i, item
    A_new = A[i_min:i_max+1]
    res = 1
    for j in A_new:
        res *= j
    print(res)
    A.sort()
    print(f"2) {A} ")
