print("Müziği durdurmak için ctrl+c  ayrıca hata alırsanız metforadan tam kurulum yapın")
mzk = input("Müzik Yolu Giriniz > ")
os.system("mpv --no-video "+mzk)