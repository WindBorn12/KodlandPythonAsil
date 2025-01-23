import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')
    channel = bot.get_channel(YOUR_CHANNEL_ID)  # Mesaj göndermek istediğiniz kanalın ID'sini buraya yazın
    if channel:
        message = await channel.send('Bot aktif! Çevre koruma ve bağış komutları için $Bilgi yazabilirsiniz.')
        await message.pin()

@bot.command()
async def Bilgi(ctx):
    await ctx.send("Merhaba! Ben bir Discord botuyum. Çevre kirliliği hakkında bilgisi olan ve bu konuda birşeyler yapmak isteyen insanlar için buradayım. Bilgi almak için şu komutları kullanabilirsin: ")
    await ctx.send('Bağış yapmak için bir kuruluş arıyorsan: $bagis')
    await ctx.send('Çevreyi korumak hakkında daha fazla bilgi almak istiyorsan: $cevrekoruma')

@bot.command()
async def bagis(ctx):
    await ctx.send('Bağış yapmak için Türkiye çapında İnternet sayfaları: ')
    await ctx.send('1_ https://online.docev.org.tr/genel-bagis.php')
    await ctx.send('2_ https://www.tema.org.tr/bagislar-ve-urunler')
    await ctx.send('3_ https://fonzip.com/cekul/bagis')
    await ctx.send('4_ https://dogadernegi.org//')
    await ctx.send('5_ https://www.cekud.org.tr/en/')

@bot.command()
async def cevrekoruma(ctx):
    await ctx.send('Çevreyi korumak hakkında daha fazla bilgi almak için: ')
    await ctx.send('1_ https://www.tema.org.tr/')
    await ctx.send('2_ https://sifiratik.co')
    await ctx.send('3_ https://www.omo.com/tr/surdurulebilirlik/cevre-kirliligini-onlemek-icin-neler-yapmaliyiz.html')
    await ctx.send('4_ https://www.cevrevakfi.org.tr/')
    await ctx.send('5_ https://www.cekud.org.tr/en/')


bot.run("")