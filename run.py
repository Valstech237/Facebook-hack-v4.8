import os

try:
    import platform
    import wget,sys
except:
    os.system('pip install wget')

bit = platform.architecture()[0]
if '64' in str(bit):
   os.system('git pull')
   if os.path.isfile('menu.py') is True:
      from menu import ListTools as runing
      exit(runing())
   else:
      exit('\nFile Menu Tidak Tersedia.')
else:
   os.system('wget https://raw.githubusercontent.com/khamdihi-dev/Prem/main/data/ibrut.zip')
   if os.path.isfile('ibrut.zip') is True:
      exit(os.system(f'unzip ibrut.zip;python {sys.argv[0]}'))
   else:
      exit('\nDownload gagal silahkan coba lagi..')
