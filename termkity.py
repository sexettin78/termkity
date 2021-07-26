import os
import random
print("\033[94m")
a1 = ('''\033[94m
     _.---.._             _.---...__
   .-'   /\   \          .'  /\     / Merhaba! Ben Terminali Güzelleştirmek ve 
   `.   (  )   \        /   (  )   /      Özelleştirmek İçin Buradayım.
     `.  \/   .'\      /`.   \/  .'
       ``---''   )    (   ``---''	1-)Saat ve Tarih    2-)Güvenlik Bölümü
               .';.--.;`.		3-)Notlar	    4-)Geliştirici Bölümü
             .' /_...._\ `.		5-)Hesap Makinesi   6-)Eğlence Bölümü
           .'   `.a  a.'   `.		7-)Dosya İndirici   8-)Linux Bölümü
          (        \/        )
           `.___..-'`-..___.'
              \          /
               `-.____.-'   			sexettin78/termkity

''')

b1 = ('''\033[93m
					Merhaba! Ben Terminali Güzelleştirmek ve 
					    Özelleştirmek İçin Buradayım.
    _                ___       _.--.
    \`.|\..----...-'`   `-._.-'_.-'`	1-)Saat ve Tarih    2-)Güvenlik Bölümü
    /  ' `         ,       __.--'	3-)Notlar	    4-)Geliştirici Bölümü
    )/' _/     \   `-_,   /		5-)Hesap Makinesi   6-)Eğlence Bölümü
    `-'" `"\_  ,_.-;_.-\_ ',     	7-)Dosya İndirici   8-)Linux Bölümü
        _.-'_./   {_.'   ; /
       {_.-``-'         {_/			sexettin78/termkity



''')

c1 = ('''\033[96m

					     
                |\___/|       Merhaba! Ben Terminali Güzelleştirmek ve
                )     (         Özelleştirmek İçin Buradayım.
               =\     /=   
                 )===(          1-)Saat ve Tarih    2-)Güvenlik Bölümü
                /     \         3-)Notlar	    4-)Geliştirici Bölümü         
               /       \  	5-)Hesap Makinesi   6-)Eğlence Bölümü
               \       /        7-)Dosya İndirici   8-)Linux Bölümü
        _/\_/\_/\_   _/_/\_/\_		 sexettin78/termkity
 ''')



d1 = (''' \033[95m

                  Merhaba! Ben Terminali Güzelleştirmek ve 
                   ___ Özelleştirmek İçin Buradayım.
  /}_{\           /.-'
 ( a a )-.___...-'/
 ==._.==         ;		sexettin78/termkity
      \ i _..._ /,
      {_;/   {_//             
       	       1-)Saat ve Tarih    2-)Güvenlik Bölümü
   	       3-)Notlar           4-)Geliştirici Bölümü
  	       5-)Hesap Makinesi   6-)Eğlence Bölümü
 	       7-)Dosya İndirici   8-)Linux Bölümü

''')


liste = [a1,b1,d1,c1]
print(random.choice(liste))
termkity = input("Hangisini Seçiyorsunuz > ")
if(termkity=="1"):
	os.system("python3 ev/saattarih.py")
elif(termkity=="2"):
	os.system("python3 sec/main.py")
elif(termkity=="3"):
	os.system("python3 ev/xsnot.py")
elif(termkity=="4"):
	os.system("python3 gelistirici/main.py")
elif(termkity=="5"):
	os.system("python3 ev/hesapmakinesi.py")
elif(termkity=="6"):
	os.system("python3 eglence/main.py")
elif(termkity=="7"):
	os.system("python3 ev/indirici.py")
elif(termkity=="8"):
	os.system("python3 lnx/main.py")
else:
	os.system("python3 termkity.py")
