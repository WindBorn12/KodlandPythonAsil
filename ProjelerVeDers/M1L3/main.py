import random
def sifreolusturucu():
    karakter = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    sifre = ""
    for i in range(10):
        sifre += random.choice(karakter)
    return sifre