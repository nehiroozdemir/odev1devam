#6.soru

yas = int(input("Yaşınızı giriniz: "))
if yas >= 18:
    print("Ehliyet alabilirsiniz")
else:
    print("Ehliyet alamazsınız")

#7.soru
fiyat = float(input("Ürünün fiyatını giriniz:"))
indirim = float(input("İndirim oranını giriniz:"))
indirimli_fiyat =fiyat - (fiyat*indirim/100)
print("Ürünün indirimli fiyatı :" ,indirimli_fiyat)

# 8.soru
a = True
b = False

print("a AND b:", a and b)
print("a OR b:", a or b)
print("NOT a:", not a)

# 9.soru
urun1=float(input("1.ürünün fiyatını giriniz:"))
urun2=float(input("2.ürünün fiyatını giriniz:"))
urun3=float(input("3.ürünün fiyatını giriniz:"))
toplam =urun1+urun2+urun3

if toplam>200 :
    toplam=toplam -(toplam*0.10)

print("Ödenecek tutar:", toplam)

#10.soru
dogum_yili=int(input("Doğum yılınızı giriniz :"))
guncel_yil=2025
yasi=dogum_yili-guncel_yil
if 0 <= yasi <=12 :
    print("Çocuksunuz")
elif 13 <= yasi <=17 :
    print("Ergensiniz")
else:
    print("Yetişkinsiniz")