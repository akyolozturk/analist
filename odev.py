#1-Kullanıcının girdiği boy ve ağırlık değerlerine göre vücut kitle indeksini
#(VKİ = ağırlık/(boyboy)) hesaplayınız.
#Python programlama dilinde “round()” fonksiyonu, bir sayıyı belirli 
#bir hassasiyete göre yuvarlamak için kullanılır.Örneğin,“round(3.14159, 2)”ifadesi,
#3.14159 sayısını 2 basamak kadar yuvarlar. 

boy=int(input("Boyunuzu giriniz(cm): "))
kilo=float(input("kilonuzu giriniz: "))
vki=kilo/((boy/100)**2)
print("Vücut kitle index'iniz {}".format(round(vki,2)))
print("Durumunuz: ")
if vki <=18.5:
    print("Zayıf")
    print("{} kilogram almanız gerekiyor".format(round(18.5((boy/100)**2)-kilo,2)))
elif vki <=24.9:
    print("Normal")
elif vki<=29.9:
    print("Fazla kilolu")
    print("{} kilogram vermeniz gerekiyor".format(round(kilo-24.9*((boy / 100) ** 2)),2))
elif vki<=39.9:
    print("Obez")
    print("{} kilogram vermeniz gerekiyor".format(round(kilo - 24.9 * ((boy / 100) ** 2)), 2))
else:
    print("Aşırı obez")
    print("{} kilogram vermeniz gerekiyor".format(round(kilo - 24.9 * ((boy / 100) ** 2)), 2))



#2-Maaşı ve zam oranı girilen işçinin zamlı maaşını hesaplayarak ekranda gösteriniz.


yeniMaas=0
maas=input("Maaşı Gir : ")
zam=input("Zam Oranı(%) : ")
yeniMaas=int(maas)+(int(maas)*int(zam)/100)
print("Zamlı Maaş :",yeniMaas)



#3-Kullanıcının girdiği üç sayı arasında en büyük olanı
# bulan ve sonucu yazdıran bir program yazınız.

a = int(input("a sayisi : " ))
b = int(input("b sayisi : " ))
c = int(input("c sayisi : " ))

if a>b and a>c:
    print("a en büyük sayıdır")
elif b>a and b>c:
    print("b en büyük sayıdır")
else:
    print("c en büyük sayıdır")


#4-Dairenin alanını ve çevresini hesaplayan python kodunu yazınız.(Dairenin yarıçapını kullanıcıdan alınız)

yaricap = input("Lutfen dairenin yaricapini giriniz:" )

dairenincevresi = 23.14 yaricap
daireninalani= 3.14yaricapyaricap
print("Dairenin cevresi: " + str(dairenincevresi))
print("Dairenin alani: " + str(daireninalani))

#5.soru 
metin = input('Metni Girin : \n')
ters=metin[::-1]

print('Girilen metnin tersi = %s' % (ters))
if ters == metin:
    print('Girilen metin palindrom')
else:
    print('Girilen metin palindrom değil.')

