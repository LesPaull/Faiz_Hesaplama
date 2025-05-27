from colorama import Fore, Style
import pandas as pd
import subprocess
import platform
import os

def menu_goster():
    print(Fore.BLUE + "FAİZ HESAPLAMA UYGULAMAMIZA HOŞGELDİNİZ\n" + Style.RESET_ALL)
    print("İşlemler")
    print("1. Faiz Hesaplama Aracı")
    print("2. Bileşik Faiz Hesaplama Aracı")
    print("3. Kayıtlara Göz At")
    while True:
        try:
            islemsecmek = int(input("yapmak istediğiniz işlemin numarasını girin: "))
            if islemsecmek == 1:
                print("Faiz Hesaplama Aracına Yönlendiriliyorsunuz!")
                return islemsecmek
            elif islemsecmek == 2:
                print("Bilesik Faiz Hesaplama Aracına Yönlendiriliyorsunuz!")
                return islemsecmek
            elif islemsecmek == 3:
                return islemsecmek
            else:
                print("yanlış bir tuşlama yaptınız!")
        except ValueError:
            print("Tekrar Deneyin.")

def kayitlari_goster():
    try:
        if platform.system() == "Darwin":  # macOS
            subprocess.call(["open", "kayitlar.csv"])
        elif platform.system() == "Linux":
            subprocess.call(["xdg-open", "kayitlar.csv"])
        elif platform.system() == "Windows":
            os.startfile("kayitlar.csv")
        else:
            print("Bu işletim sistemi desteklenmiyor.")
    except FileNotFoundError:
        print("Kayıt dosyası bulunamadı!")

def butce_sor():
    while True:
        try:
            butce = int(input("lutfen butcenizi girin: "))
            onay = input(f"butceniz {butce} TL' dir. Doğruysa 'o' ya basıp onaylayın: ")
            if onay == "o":
                print("butceniz kaydedildi!")
                return butce
            else:
                cikis = input("butce girisiniz kaydedilemedi, cikmak istiyorsanız 'q' ya basın, istemiyorsanız 'r' ye basın: ")
                if cikis == "q":
                    print("Çıktınız.")
                    exit()
        except ValueError:
            print("Lütfen sadece sayı girin!")

def faiz_orani_sor():
    while True:
        try:
            faiz_orani = float(input("Lütfen faiz oranını yüzde işareti kullanmadan giriniz: "))
            devammi = input(f"faiz oraniniz %{faiz_orani} olarak kaydedilsin istiyorsanız 'o' istemiyorsanız 'n' yazın:")
            if devammi == "o":
                print(f"faiz oraniniz %{faiz_orani} olarak kaydedilmiştir")
                return faiz_orani
            elif devammi == "n":
                print("uygulamadan çıkılıyor...")
                break
            else:
                print("hatalı tuşlama yaptınız başa döndürülüyorsunuz!")
        except ValueError:
                print("Lütfen % kullanmadan sayı girin!")

def vade_sayisi_sor():
    while True:
        try:
            vade_gun = int(input("Vade gün sayısı girin: "))
            kayit1 = input(f"Vade gün sayınız {vade_gun} olarak kaydedilecektir onaylıyorsanız 'o' ya basın: ")
            if kayit1 == "o":
                print("kayıt edildi.")
                return vade_gun
            else:
                print("yanlış bir girdi girdiniz tekrar deneyin.")
                continue
        except ValueError:
            print("Lütfen bir sayı girin!")
           
def tax_rate_asker():
    while True:
        try:
            taxrate = float(input("Varsa Vergi oranını sayı olarak girin, yoksa 0 yazın."))
            if taxrate > 0:
                print(f"vergi oranınız %{taxrate} olarak kaydedilmiştir.")
                return taxrate
            elif taxrate == 0:
                print("vergi oranı yoktur veyahut dikkate alınmayacaktır!")
                return 0
        except ValueError:
            print("Lütfen bir sayı girin!")

def faiz_hesaplama_araci(butce, faiz_orani, vade_gun, taxrate):

    brut_getiri = (((butce * faiz_orani)/100/365) * vade_gun)
    net_getiri = (((butce * faiz_orani)/100/365) * vade_gun - ((((butce * faiz_orani)/100/365) * vade_gun) * taxrate/100))
    vade_sonu_brut = (butce + (((butce * faiz_orani)/100/365) * vade_gun))
    vade_sonu_net_miktar = (butce + (((butce * faiz_orani)/100/365) * vade_gun - ((((butce * faiz_orani)/100/365) * vade_gun) * taxrate/100)))

    print(Fore.RED + "FAİZ HESAPLAMA İŞLEMİ SONUÇLARI\n" + Style.RESET_ALL)
    print(f"Brüt getiriniz: {brut_getiri:.2f} TL' dir.")
    print(Fore.GREEN + f"Net Getiriniz: {net_getiri:.2f} TL' dir." + Style.RESET_ALL)
    print(f"Vade Sonu Brüt Miktar: {vade_sonu_brut:.2f} TL' dir.")
    print(Fore.GREEN + f"Vade Sonu Net Miktar: {vade_sonu_net_miktar:.2f} TL' dir." + Style.RESET_ALL)
    return {
        "Brüt Getiri": round(brut_getiri, 2),
        "Net Getiri": round(net_getiri, 2),
        "Vade Sonu Net Miktar": round(vade_sonu_net_miktar, 2)
    }

def bilesik_faiz_hesaplama(butce, faiz_orani, vade_gun, taxrate):
    oran = faiz_orani / 100
    t = vade_gun / 365
    n = 365

    bilesik_brut_toplam = butce * (1 + oran / n) ** (n * t)
    brut_getiri = bilesik_brut_toplam - butce

    if taxrate >= 100:
        print("HATA: Vergi oranı %100'den büyük olamaz!")
        return

    vergi_tutari = brut_getiri * (taxrate / 100)

    net_getiri = brut_getiri - vergi_tutari

    vade_sonu_net = butce + net_getiri

    print(Fore.RED + "BİLEŞİK FAİZ HESAPLAMA SONUCU\n" + Style.RESET_ALL)
    print(f"Brüt Getiri: {brut_getiri:.2f} TL")
    print(f"Net Getiri: {net_getiri:.2f} TL")
    print(Fore.GREEN + f"Vade Sonu Net Miktar: {vade_sonu_net:.2f} TL" + Style.RESET_ALL)

    return {
        "Brüt Getiri": round(brut_getiri, 2),
        "Net Getiri": round(net_getiri, 2),
        "Vade Sonu Net Miktar": round(vade_sonu_net, 2)
    }

hesap_kayitlari = []

def hesap_kaydi(butce, faiz_orani, vade_gun, taxrate, islemsecmek, sonuc):
    while True:
        kayit_sorusu = input("kaydetmek isterseniz s ye, istemezseniz, r ye basın: ").lower()
        if kayit_sorusu == "s":
            hesapismi = input("hesap ismi girin: ")
            kayit = {"Hesap İsmi": hesapismi,
                "Hesaplama Tipi": "Faiz Hesaplama" if islemsecmek == 1 else "Bileşik Faiz Hesaplama",
                "Hesap Butcesi": butce,
                "Faiz Oranı": faiz_orani,
                "Vade Günü": vade_gun,
                "Vergi Oranı": taxrate,
                **sonuc
                }
            hesap_kayitlari.append(kayit)
            veri_kaydi(kayit)
            print(f"Kaydınız Hesap ismi {hesapismi} olarak yapıldı!")
            break
        elif kayit_sorusu == "r":
            print("Kayıt İşlemi İptal Edildi!")
            break

def veri_kaydi(kayit):
    try:
        df = pd.read_csv("kayitlar.csv")
    except FileNotFoundError:
        df = pd.DataFrame(columns=["Hesap İsmi", "Hesaplama Tipi", "Hesap Butcesi", "Faiz Oranı", "Vade Günü", "Vergi Oranı"])
    yeni_df = pd.DataFrame([kayit])
    if df.empty:
        df = yeni_df
    else:
        df = pd.concat([df, yeni_df], ignore_index=True)
    df.to_csv("kayitlar.csv", index = False)