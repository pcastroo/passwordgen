import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "[]{}()*;/,._-"

if input("Symbols? (y/n): ").lower().strip()[:1] == "n":
    symbols = ""

all = lower + upper + numbers + symbols

length = 16
password = "".join(random.sample(all,length))
print(password)
