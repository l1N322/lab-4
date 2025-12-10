#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    a = list(map(int, input().split()))
    if not a:
        print("Заданный список пуст", file=sys.stderr)
        exit(1)

    neg = 1
    has_neg = False
    for num in a:
        if num < 0:
            neg *= num
            has_neg = True
    if not has_neg:
        neg = 0

    max = a[0]
    i_max = 0
    for i, num in enumerate(a):
        if num > max:
            max = num
            i_max = i

    sum_pos = sum(num for num in a[:i_max] if num > 0)

    reverse = a[::-1]

    print(f"Произведение отрицательных элементов: {neg}")
    print(f"Сумма положительных элементов до максимума: {sum_pos}")
    print(f"Список в обратном порядке: {reverse}")