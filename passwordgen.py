import random
import sys

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "[]{}()*;/,._-"

try:
    if input("Symbols? (y/n): ").lower().strip()[:1] == "n":
        symbols = ""
except KeyboardInterrupt:
    print ("\nbyee!! \n")
    sys.exit()

all = lower + upper + numbers + symbols

length = 16
password = "".join(random.sample(all,length))
print(password)
