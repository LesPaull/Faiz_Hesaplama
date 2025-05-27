from hesaplama_araclari1 import*

while True:
    islemsecmek = menu_goster()
    if islemsecmek == 3:
        kayitlari_goster()
        yeniden_hesaplama = input("Yeni bir işlem yapmak için 'o' ya basın: ")
        if yeniden_hesaplama.lower() != "o":
            print("Hoşcakalın!")
            break
        else:
            continue
                
    butce = butce_sor()
    faiz_orani = faiz_orani_sor()
    vade_gun = vade_sayisi_sor()
    taxrate = tax_rate_asker()

    if islemsecmek == 1:
        sonuc = faiz_hesaplama_araci(butce, faiz_orani, vade_gun, taxrate)
    elif islemsecmek == 2:
        sonuc = bilesik_faiz_hesaplama(butce, faiz_orani, vade_gun, taxrate)
    else:
        print("Yanlış bir tuşa bastınız, tekrar deneyin!")
        continue
    hesap_kaydi(butce, faiz_orani, vade_gun, taxrate, islemsecmek, sonuc)
    yeniden_hesaplama = input("Tekrar hesaplama yapmak isterseniz 'o' ya, çıkmak için herhangi bir tuşa basabilirsiniz.")
    if yeniden_hesaplama == "o":
        continue
    else:
        print("Hoşcakalın!")
        break