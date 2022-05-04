from time import sleep
from requests import get
#from pprint import PrettyPrinter
#from datetime import datetime

def sprint(msc, txt):
	for i in txt:
		print(i, end="")
		sleep(msc / 100)
	print("\n",end="")


BASE_URL = "https://currencyscoop.p.rapidapi.com/"
LIST = 'currencies'
LATEST = 'latest'
HISTORICAL = 'historical'
HDR = {"X-RapidAPI-Host": "currencyscoop.p.rapidapi.com","X-RapidAPI-Key": "a961669892mshac1f9f1c344e277p1c5fd4jsne37627860753"}

#NOW = datetime.now()
#NDate = str(f"{NOW.year}-0{NOW.month}-0{NOW.day}")


def convert_unit(base,conv,mny,date=""):
	if date == "":
		param = {"base": f"{base}"}
		cs_list = get_list(BASE_URL + LATEST, HDR, 'rates', prms=param)
	else:
		param = {"base": f"{base}","date":f"{date}"}
		cs_list = get_list(BASE_URL + HISTORICAL, HDR, 'rates', prms=param)

	for i, j in cs_list:
		if conv == i:
			result = mny * j
			break
	return result

def make_list(liste, value=None):
	key = []
	name = []
	list = []
	for i in liste.keys():
		key.append(i)
	for i in liste.values():
		if value != None:
			name.append(i[value])
		else:
			name.append(i)
	for i in range(0, len(key)):
		list.append((key[i], name[i]))
	return list


def get_list(url, hdr, lh, le=None, prms=None):
	list_data = get(url, headers=hdr, params=prms).json()
	ls = list_data['response'][lh]
	list = make_list(ls, le)
	return list


def show_list(list):
	for i, j in list:
		print(f"{i}:{j}")
	print("\n")


sprint(1,"Uygulamamıza Hoşgeldiniz")
sprint(1,"Bu uygulama para çevirme işlemi yapıyor")
sleep(1)
while True:
	cmd=input("Listeyi görmek için = SL\nPara birimi çevirmek için= CC \nKomutunuzu Giriniz:")

	if cmd == 'SL':
		show_list(get_list(BASE_URL+LIST,HDR,'fiats','currency_name'))
	elif cmd == 'CC':
		base = input("Baz alıncak para birimini giriniz:")
		conv = input("Çevrilcek para birimini giriniz:")
		date = input("2006-06-28 Formatında olucak şekilde \nÇevrilmesini istediğiniz tarihi giriniz(tarih girilmezse günümüz algılanacaktır):")
		mny = int(input("Kaç para çevrilecekse onu giriniz:"))

		result = convert_unit(base, conv, mny, date)
		print(result,'\n')
	else:
		print("Lütfen geçerli bir komut giriniz.")