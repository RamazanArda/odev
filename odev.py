meme_dict = {
    "CRINGE": "Garip ya da utandırıcı bir şey.",
    "LOL": "Komik bir şeye verilen cevap.",
    "ROFL": "Bir şakaya karşılık verilen cevap.",
    "SHEESH": "Onaylamama ifadesi.",
    "CREEPY": "Tüyler ürpertici, ürkütücü anlamına gelen söz.",
    "AGGRO": "Agresifleşmek, sinirlenmek anlamına gelen söz.",
    "OMG": "Aman tanrım anlamında şaşırma ifadesi.",
    "NGL": "Gerçekten öyle, yalan söylemiyorum anlamına gelen söz."
}

while True:
    word = input("Sözlükten anlamını öğrenmek istediğiniz bir kelimeyi girin: ").lower()

    while word not in meme_dict.keys():
        olus = input("Bu kelime sözlükte bulunamadı Kelime eklemek istermisiniz? (evet/hayır)? : ").lower()
        if olus == "evet":
            yenikelime = input("yeni sözcüğü girin: ").lower()
            yenianlam = input("Bu kelime ne anlama geliyor: ")
            meme_dict[yenikelime] = yenianlam
            print("sözcüğünüz sözlüğe başarı ile eklendi.")
        else:
            print('tamam o zaman devam edelim')
            break
            
        
    if word in meme_dict.keys():
        print(meme_dict[word])
