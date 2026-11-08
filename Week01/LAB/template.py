"""
RECORD CHECK  -  my version
===========================

Name  : Ismail 
Lane  :  IT    
Date  : 02/10/2026

Run it:   miniproject_week01.py
"""


label = input("name")
first = int(input("first number"))
second = int(input("second number"))

difference = first - second
percent = (first / second) * 100


print()
print("=" * 34)
print(f" record check - {label}")
print("=" * 34)
print(f" first : {first:>10}")
print(f" second : {second:>10}")
print(f" diffrence {difference:>+10}")
print(f" percent : {percent:>10}")
print("=" * 34)