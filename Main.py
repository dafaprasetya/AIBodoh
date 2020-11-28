import os
import sys
import time
import random
import socket
from Core import impup
from Core.Lakukan import tanya
import webbrowser
from datetime import datetime
import pytube



start = "starting system..."
for a in start:
    time.sleep(0.1)
    sys.stdout.write(a)
    sys.stdout.flush()

os.system('pip install pytube' if  os.name == 'nt' else 'pip3 install pytube')

os.system("cls" if os.name == 'nt' else 'clear')

host = socket.gethostname()
ip = socket.gethostbyname(host)


filesize = os.path.getsize("user/user.txt")
now = datetime.now()

waktu = now.strftime("%H:%M \n")

if filesize <= 1:
	user = open('user/user.txt', 'r+')

	nama = input("Masukan Nama : ")
	user.write(nama)

	user.close()
	user = open('user/user.txt', 'r')
	baca = user.read()
	bacot = 'Hi {} Welcome^-^\n'.format(baca)
	for ba in bacot:
		time.sleep(0.1)
		sys.stdout.write(ba)
		sys.stdout.flush()

else:
    user = open('user/user.txt','r')
    b = user.read()
    teks = "Hi {} welcome back\n".format(b)
    for w in waktu:
    	time.sleep(0.1)
    	sys.stdout.write(w)
    	sys.stdout.flush()
    for a in teks:
    	time.sleep(0.1)
    	sys.stdout.write(a)
    	sys.stdout.flush()
    
def Main():
	menyapa = tanya.menyapa
	jawaban_menyapa = tanya.jawaban_menyapa
	global waktu
	hai = input(">>")
	if hai == "whoami":
		impup.whoami()
		Main()
	if hai == "clear":
		os.system("cls" if os.name == 'nt' else 'clear')
		Main()
	if hai == "help":
		impup.help()
		Main()
	if hai == "saran":
		impup.saran()
		Main()
	if hai in tanya.fb:
		webbrowser.open("https://facebook.com")
		Main()
	if hai in tanya.wa:
		webbrowser.open("https://whatsapp.com")
		Main()
	if hai in tanya.ig:
		webbrowser.open("https://instagram.com")
		Main()	
	if hai in tanya.jambaraha:
		wakt = "sekarang jam {}".format(waktu)
		print(wakt)
		Main()
	if hai =="kirim pesan":
		impup.kirim_pesan()
		Main()
		
	if hai == "python":
		os.system("python")
		Main()
	if hai == "detik":
		baraha = int(input("Berapa?(int) "))
		impup.waktu(baraha)
		Main()
	if hai == "warna":
		warna = input("Pilih warna :\nBLACK\nRED\nGREEN\nYELLOW\nBLUE\nMANGENTA\nCYAN\nWHITE\nUNDERLINE\nRESET\nPILIH >>")
		impup.warna(warna)
	if hai == "random range":
		dari = int(input("dari : "))
		sampai = int(input("sampai : "))
		rn = ("@", "#","$","_","&","©","π")
		kalidua = rn*20
		for z in range(dari, sampai):
			time.sleep(0.01)
			os.system("cls" if os.name == 'nt' else 'clear')
			a = random.randrange(dari, sampai)
			q = random.choice(kalidua)
			print(q)
		time.sleep(1)	
		print("nomor terpilih : ", a)
		Main()
	if hai in menyapa:
		rjm = random.choice(jawaban_menyapa)
		print(rjm)
		Main()
	if hai in tanya.kamu_tahu:
		rjkm = random.choice(tanya.jktau)
		print(rjkm)
		a = input("apa harus aku tulis di memori ku?")
	if hai == 'youtube downloader':
		print('YouTube Downloader')
		url = input('masukan url : ')
		impup.downloader(url)
	else :
		os.system('color 3' if os.name == 'nt' else '')
		rjels = random.choice(tanya.jrels)
		print(rjels)
		Main()
	
Main()
