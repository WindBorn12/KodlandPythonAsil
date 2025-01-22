meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "BRUH": "Saçma bulunan şeye verilen cevap",
            "NGL": "yalan soylemeyecegim"
            }

word = input("anlamadiginiz kelimeyi yaziniz").upper()

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("boyle bir kelime yok")
