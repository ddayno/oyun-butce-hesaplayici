
def sayi_al(soru):
    while True:
        try:
            sayi = int(input(soru))

            if sayi > 0:
                return sayi
            else:
                print("Lutfen 0'dan buyuk bir sayi gir.")

        except ValueError:
            print("Hatali giris! Lutfen tam sayi yaz.")


def maliyet_hesapla(calisan, maas, ay):
    return calisan * maas * ay


def butce_kontrol(toplam, butce):
    if toplam > butce:
        print("UYARI: Proje butceyi asiyor!")
    elif toplam == butce:
        print("Proje butceye tam olarak esit!")
    else:
        print("Proje butceye uygun!")


def hesaplama_yap():
    calisan = sayi_al("Kac calisan var? ")
    maas = sayi_al("Bir calisanin aylik maasi kac dolar? ")
    ay = sayi_al("Oyun kac ayda gelistirilecek? ")

    toplam = maliyet_hesapla(calisan, maas, ay)

    print("Toplam gelistirme maliyeti:", toplam, "dolar")

    butce = sayi_al("Projenin butcesi kac dolar? ")

    butce_kontrol(toplam, butce)

    rapor_bilgileri = {
        "Calisan sayisi": calisan,
        "Aylik maas": maas,
        "Gelistirme suresi": ay,
        "Toplam maliyet": toplam,
        "Proje butcesi": butce
    }

    with open("rapor.txt", "w", encoding="utf-8") as dosya:
        dosya.write("OYUN GELISTIRME BUTCE RAPORU\n")
        dosya.write("-------------------------\n")

        for bilgi, deger in rapor_bilgileri.items():
            dosya.write(f"{bilgi}: {deger}\n")

    print("Rapor basariyla kaydedildi!")


while True:
    print("\n===== OYUN BUTCE HESAPLAYICI =====")
    print("1 - Yeni butce hesapla")
    print("2 - Programdan cik")

    secim = input("Seciminiz: ")

    if secim == "1":
        hesaplama_yap()
    elif secim == "2":
        print("Program kapatiliyor...")
        break
    else:
        print("Gecersiz secim! Lutfen 1 veya 2 gir.")

