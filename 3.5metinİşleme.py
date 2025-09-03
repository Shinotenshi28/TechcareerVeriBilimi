metin=input("Metin Giriniz:")
def kelime_sayaci(metin):
    # Noktalama işaretlerini kaldır ve metni küçük harfe çevir
    import string
    metin_temiz = metin.translate(str.maketrans('', '', string.punctuation)).lower()
    
    # Kelimeleri listeye çevir
    kelimeler = metin_temiz.split()
    
    # Toplam kelime sayısı
    toplam_kelime = len(kelimeler)
    
    # En uzun kelime
    en_uzun = max(kelimeler, key=len) if kelimeler else ""
    
    # En sık geçen kelime
    from collections import Counter
    kelime_sayilari = Counter(kelimeler)
    en_sik = kelime_sayilari.most_common(1)[0][0] if kelimeler else ""
    
    return toplam_kelime, en_uzun, en_sik

toplam, uzun, sık = kelime_sayaci(metin)
print("Toplam kelime:", toplam)
print("En uzun kelime:", uzun)
print("En sık geçen kelime:", sık)