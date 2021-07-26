import urllib.request
print("\n Dosya adını istediğiniz gibi belirleyebilirsiniz.Dosya uzantısı,indireceğiniz dosya uzantısı ile aynı olmak zorundadır.Bulunduğu dizine indirir\n")
dosya_linki = input("Dosya linkini giriniz >")
dosya_adi = input("Dosya adını uzantısı ile beraber giriniz > ")
urllib.request.urlretrieve(dosya_linki, dosya_adi)