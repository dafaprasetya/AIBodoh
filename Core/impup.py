import webbrowser
import random
import time
import string
import pytube


class style():
    black = '\033[30m'
    red = '\033[31m'
    green = '\033[32m'
    yellow = '\033[33m'
    blue = '\033[34m'
    mangenta = '\033[35m'
    cyan = '\033[36m'
    white = '\033[37m'
    underline = '\033[4m'
    reset = '\033[0m'
wa = "https://api.whatsapp.com/send?phone=6281574999858&text="
p = "prstya"
user = []

def whoami():
	user = open('user/user.txt', 'r')
	username = user.read()
	print(username)
	
def help():
	print(style.cyan + "Prstyaa command\n" + style.yellow + "1. whoami(untuk mengetahui siapa anda)\n2. help(untuk mengetahui command yang tersedia)\n3. saran(untuk mengirim saran)\n4.kirim pesan(untuk mengirim pesan via WA)"+style.reset)
	
def saran():
	saran = input("Masukan Saran : ")
	webbrowser.open_new_tab(wa + saran + " \ndari : " + user[0])


def kirim_pesan():
	penerima = input("masukan nomor penerima : ")
	dari = "\ndari : " + user[0]
	pesan = input("ketik pesan : ")
	kirpes = "https://api.whatsapp.com/send?phone=62{}&text={}.{}".format(penerima, pesan, dari)
	webbrowser.open_new_tab(kirpes)
def waktu(berapa):
	for i in range(berapa):
		time.sleep(1)
		print(i)
def warna(warni):
	war = "style" + "." +warni
	print(war)
def downloader(url):
	print('Tunggu...')
	video = pytube.YouTube(url)
	judul = video.title
	print('judul : ', judul)
	print('Downloading...')
	video.streams.first().download()
	print('Done.')

	

