import os
print("\033[95m")
print('''

                   _..
  /}_{\           /.-'
 ( a a )-.___...-'/	1-)Linux Asistanı 2-)Anamenü
 ==._.==         ;
      \ i _..._ /,
      {_;/   {_//  


''')
lnx = input("Hangisini Seçiyorsunuz > ")
if(lnx=="1"):
	os.system("python3 lnx/asistan.py")
elif(lnx=="2"):
	os.system("python3 termkity.py")
