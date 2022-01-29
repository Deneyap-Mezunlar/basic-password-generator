import random
import string
from sys import argv

print("Merhaba! SeoLeX'in şifre üreticine hoşgeldin.")

length = int()

if len(argv) < 2: # Argument not specified / Arguman belirtilmemisse
    try:
        length = int(input("\nOluşturmak istediğin şifrenin karakter sayısını gir! \n"))
    except ValueError:
        print("Sadece sayi girmelisiniz.")
        exit(1)
else:
    try:
        length = int(argv[1])
    except ValueError:
        print("Sadece sayi girmelisiniz.")
        exit(1)

lower = string.ascii_lowercase
upper = string.ascii_uppercase
number = string.digits
symbol = string.punctuation

all = lower + upper + number + symbol

temp = random.sample(all,length)

password ="".join(temp)

print(password)
