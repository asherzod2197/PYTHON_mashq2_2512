def capitalize_words(matn):
    sozlar = matn.split()
    
    yangi_sozlar = []
    for soz in sozlar:
        if soz:
            yangi = soz[0].upper() + soz[1:].lower()
            yangi_sozlar.append(yangi)
        else:
            yangi_sozlar.append(soz)
    
    return " ".join(yangi_sozlar)


matn = input("Matnni kiriting: ")
natija = capitalize_words(matn)
print("Natija:", natija)
