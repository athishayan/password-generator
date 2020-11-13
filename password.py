import string
from random import *
chartrs = string.ascii_letters + string.punctuation + string.digits
password = "".join(choice(chartrs) for i in range(randint(8,16)))
print(password)
