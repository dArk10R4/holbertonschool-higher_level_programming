#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0

    roman_letters = [
        ['M', 1000], ['D', 500], ['C', 100], ['L', 50],
        ['X', 10], ['V', 5], ['I', 1]
    ]
    s = 0
    last = 0

    for i in reversed(roman_string):
        for j in roman_letters:
            if (i == j[0]):
                if last > j[1]:
                    s -= j[1]
                else:
                    s += j[1]
                last = j[1]

    return s
