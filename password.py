import random

elements = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
lunghezza_password = int(input("inserisci la lunghezza della password: "))
password = ""

for i in range(lunghezza_password):
    password = password + random.choice(elements)

print(password)
