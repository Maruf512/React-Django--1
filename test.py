import string
import random

length = 6

code = ''.join(random.choices(string.ascii_uppercase, k=length))


print(code)
