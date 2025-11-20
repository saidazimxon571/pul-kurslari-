import requests

print('Asalamu Aleykum bank malumotlari bazasiga hush kelibsiz :)')
data = requests.get('https://cbu.uz/uz/arkhiv-kursov-valyut/json/').json()


def qaysi_davlat():
    pul_birligi = input('qanday valyuta qidiryabsiz qidiryabsiz kiriting: (UZS) >> ').upper()
    for i in data:
       if pul_birligi==i['Ccy']:
           print(f'Bunday valyuta bizda topildi  \n qiymati: {i['Rate']} ')
           sorov=input('pulingizning qiymatini bilishni xoxlaysizmi (ha/yoq) >> ').lower()
           if sorov=='ha':
               bor_pul=input('ozgartirmoqchi bolgan pulingizni summasini kiriting >>>  ')
               pul=float(bor_pul)/float(i['Rate'])
               return f'sizning pulingiz {i['CcyNm_UZ']} da {pul} {pul_birligi} boladi :)'
           else:
               return 'dastur tugatildi!'
    return f'biznimg malumotlarimizda {pul_birligi} nomli valyuta topilmadi !'

print(qaysi_davlat())
