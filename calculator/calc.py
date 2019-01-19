#!/usr/bin/env python3
# -*- coding: utf-8 -*-

number1 = input("First number: ")
expression = raw_input("Math expression: ")
number2 = input("Second number: ")
if expression == "+":
    result = number1 + number2
elif expression == "-":
    result = number1 - number2
elif expression == "*":
    result = number1 * number2
elif expression == "/":
    result = number1 / number2
print(result)
