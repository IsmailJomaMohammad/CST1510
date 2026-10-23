"""
RECORD CHECK  -  my version
===========================

Name  : Ismail 
Lane  :  IT    
Date  : 02/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

label = input("name / hostname / IP: ")
first = float(input("first number: "))
Second = float(input("second number:"))

difference = first - second
percent = (first / second) * 100


print()
print("=" * 34)
print(f" record check - {label}")
print("=" * 34)
print(f" first : {first:>10.2f}")
print(f" second : {second:>10.2f}")
print(f" diffrence {difference:>+10.2f}")
print(f" percent : {percent:>10.2f}")
print("=" * 34)