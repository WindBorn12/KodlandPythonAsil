from flask import Flask
import random
import os


def rastgele_resim_sec(klasor_yolu):
    dosyalar = [f for f in os.listdir(klasor_yolu)]

    secilen_resim = random.choice(dosyalar)
    return os.path.join(klasor_yolu, secilen_resim)


klasor_yolu = "static/Images/duck"  












rastgele_bilgiler = ["Teknolojik bağımlılıktan mustarip olan çoğu kişi, kendilerini şebeke kapsama alanı dışında bulduklarında veya cihazlarını kullanamadıkları zaman yoğun stres yaşarlar.",
                     "2018 yılında yapılan bir araştırmaya göre 18-34 yaş arası kişilerin %50'den fazlası kendilerini akıllı telefonlarına bağımlı olarak görüyor.",
                     "Teknolojik bağımlılık çalışması, modern bilimsel araştırmanın en ilgili alanlarından biridir.",
                     "2019'da yapılan bir araştırmaya göre, insanların %60'ından fazlası akıllı telefonlarındaki iş mesajlarına işten ayrıldıktan sonraki 15 dakika içinde yanıt veriyor."]


app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<h1>Hello, World!</h1>     <a href="/ikincisayfa">İkinci sayfa için tıklayınız     <a href="/RastgeleBilgi">Rastgele bilgi icin tiklayiniz  <a href="/RastgeleResim">Rastgele resim'


@app.route("/ikincisayfa")
def ikincisayfa():
    return '<h1>İkinci sayfa!</h1>    <a href="/">İlk sayfa için tıklayınız'

@app.route("/RastgeleBilgi")
def RastgeleBilgi():
    return f'<h1>{random.choice(rastgele_bilgiler)}   <a href="/">İlk sayfa için tıklayınız'

@app.route("/RastgeleResim")
def RastgeleResim():
    global secilen_resim,klasor_yolu
    secilen_resim = rastgele_resim_sec(klasor_yolu)

    return f'<img src="{secilen_resim}">'







app.run(debug=True)
