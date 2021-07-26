import os
print('''

                   _..
  /}_{\           /.-'
 ( a a )-.___...-'/	1-)Müzik İndir 2-)Anamenü 
 ==._.==         ;	3-)Sayı Tahmin
      \ i _..._ /,
      {_;/   {_//  


''')
lnx = input("Hangisini Seçiyorsunuz > ")
if(lnx=="1"):
	os.system("python3 eglence/mzkindir.py")
elif(lnx=="2"):
	os.system("python3 termkity.py")
elif(lnx=="3"):
	os.system("python3 eglence/sayitahmin.py")