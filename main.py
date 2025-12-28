import random
karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password = ""
sayi = int(input("Kaç haneli şifre istiyorsunuz?"))
for i in range(sayi):
    karakter = random.choice(karakterler)
    password += karakter
print(password)
