import pprint


print("=============================")
print("The Missing Painting")
print("=============================")


print()
print('Gizemli bir şekilde kaybolan bir tabloyu bulmak için ' \
'görevlendirildiniz. Tablonun kaybolduğu yerin ipuçlarini toplayarak ve ' \
'şüphelileri sorgulayarak tabloyu bulmaniz gerekiyor.')
print()

name = input("Lutfen adinizi giriniz: ")

print()

name = input(f"Sen artik dedektifsin   {name}  , lutfen bulman gereken tabloya odaklan!!: ")

print()
print(f"Dedektif  {name}  , tabloyu bulmak için ipuçlarini toplayacak ve şüphelileri sorgulayacaksınız.")
print("Hazir misin? Basliyoruuzzz!!") 

print()
print("=================================")
print("Vaka Basliyor!!!")
print("=================================")
print()

print('Saat 23.45')
print('Istanbul, Beyoglu, Galata Kulesi civarinda bir sanat galerisi. Tablonun kayboldugu yer burasi.')
print('Galeri sahibi, tabloyu en son gece saatlerinde burada gordugunu soyluyor.')
print()

print("Tablonun adi 'Gizemli Manzara' ve sanatci 'Ahmet Yilmaz'.")
print('Tablonun degeri: 1.000.000 TL')
print()

print("Tabloyu bulmak icin ipuclari toplamaniz gerekiyor.")
print('Polis geldiginde kapi kilitliydi ve odada baska kaciliran esya yoktu sadece o sanat parcasiydi ve neden oydu??')
print()

print("Tabloyu bulmak icin ipuclari toplamak icin galerinin icine giriyorsunuz ve gorevleriniz .")
print("1. Galerinin icinde ipuclari aramak")
print("2. Süphelileri sorgulamak")
print("3. Yalanlari ortaya cikarmak")
print("4. Tabloyu kimin caldigini bulmak")

print()
print("==============================")
print("Ne Yapmak Istedigini Bana Belirtir Misin?")
print("==============================")
print()

print("1 - Odayi araştir")
print("2 - Şüphelileri sorgula")
print("3 - Kanitlari incele")
print("4 - Oyundan çik")

print()

choice = input("Lütfen yapmak istediğiniz işlemi seçin (1-4): ")

if choice == "1":
    print('Odayi araştiriyorsunuz...')
    print('Oda oldukça karışık ve dağınık. Masanın üzerinde bir not buluyorsunuz.')
    print('Notta şunlar yazıyor: "Tabloyu çaldım, ama kimseye söylemeyeceğim. Eğer tabloyu geri almak istiyorsanız, bana 100.000 TL getirin."')
    print('Notu okuduktan sonra, odada başka bir ipucu arıyorsunuz ve bir kamera kaydı buluyorsunuz.')
    print('Kamera kaydında, bir kişinin galerinin arka kapısından çıktığını görüyorsunuz ve elinde tabloyu taşıyor gibi görünüyor.')

elif choice == "2":
   print('Şüpheliler')
print('1. Galerinin Sahibi Ahmet: Tablonun kaybolduğu gece galerideydi ve tabloyu en son kendisi gördüğünü söylüyor.')
print('2. Galerinin güvenlik görevlisi Emre: Tablonun kaybolduğu gece galerideydi ve tabloyu en son kendisinin gördüğünü söylüyor.')
print('3. Galerinin temizlik görevlisi Deniz: Tablonun kaybolduğu gece galerideydi ve tabloyu en son kendisinin gördüğünü söylüyor.')
print('4. Galerinin sanat danışmanı Ayşe: Tablonun kaybolduğu gece galerideydi ve tabloyu en son kendisinin gördüğünü söylüyor.')
print('5. Galerinin koleksiyoner Mehmet: Tablonun kaybolduğu gece galerideydi ve tabloyu en son kendisinin gördüğünü söylüyor.')

print()
suspect = input("Lütfen sorgulamak istediğiniz şüphelinin numarasını girin (1-5): ")
if suspect == "1":
        print()
        print(" Ahmet- Galeri Sahibi: Tablonun kaybolduğu sırada galerideydim. Tablonun kaybolduğunu fark ettiğimde hemen polisi aradım.")
        print()

elif suspect == "2":
        print()
        print(" Emre - Guvenlik Gorevlisi : O gece kameraları kontrol ediyordum. Ama onu neden çalayım ki?")
        print()

elif suspect == "3":
        print()
        print("Deniz - Temizlik Gorevlisi : O gece ben hep yaptigim gibi cikmadan onceki temizigimi yapip ciktim galeriden")
        print()

elif suspect == "4":
        print()
        print("Ayse - Sanat Danismani : Tabloyu satın almak istemiştim. Ama satın alamadıysam çalacağım anlamına gelmez. ")
        print()

elif suspect == "5":
        print()
        print("Mehmet - Sanat Eleştirmeni : Tablonun kaybolduğunu duyduğumda çok şaşirdim. Ama ben çalmadim.")
        print()
else:
        print()
        print("Böyle bir şüpheli bulunamadi.")    
     
      
if choice == "3":

    print("Kanitlari inceliyorsunuz...")

    print("Notu ve kamera kaydini inceledikten sonra, notun yazi tipinin galerinin bilgisayarinda bulunan bir yazi tipine benzediğini fark ediyorsunuz.")

    print("Kamera kaydinda görülen kişinin, galerinin güvenlik görevlisi olduğunu fark ediyorsunuz.")
    
if choice == "4":
    print()

    print("Oyundan çikiliyor...")

else:
    print()

    print(" Geçersiz seçim! Lütfen 1, 2, 3 veya 4 seç.")

while True:
    print("Ana Menü")
    choice = input("Seçimin: ")

    if choice == "1":
        ...

    elif choice == "2":
        ...

    elif choice == "4":
        print("Oyundan çıkılıyor...")
        break








