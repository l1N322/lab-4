#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    count = tuple(map(int, input().split()))
    temprature = tuple(map(int, input().split()))
    if not count or not temprature or len(count) != len(temprature):
        print("Неверные данные", file=sys.stderr)
        exit(1)

    rain = 0
    snow = 0

    for i, c in enumerate(count):
        temp = temprature[i]

        if temp > 0:
            rain += c
        else:
            snow += c

    print(f"Осадки в виде дождя: {rain} мм")
    print(f"Осадки в виде снега: {snow} мм")