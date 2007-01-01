import serial
import db_query
import screen_write
 
ser = serial.Serial(
    port='/dev/ttys4', 
    baudrate=9600, 
    timeout=0.1,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)  


def calcola_checksum (comando, parametro):
	com = ord(comando)
	for i in range (0, len(parametro)):
		com = com ^ ord(parametro[i])
	com = chr(com)
	return com

def verifica (lista):
	if len(lista)>0:
		pwd1 = return_PWD(1)
		pwd2 = return_PWD(2)
		print pwd1
		print pwd2
		lista_control1 = []
		for i in range (0. len(pwd1)):
			lista_control1.append(pwd1[i])
		lista_control2 = []
		for i in range (0. len(pwd2)):
			lista_control2.append(pwd2[i])
			
		if lista == lista_control1:
			goto_form(1)
			del lista[0:6]
			return
							
		elif lista == lista_control2:		
			goto_form(2)
			del lista[0:6]
			return
								
		else:
			goto_form(3)
			del lista[0:99]
			return	
							
	else:
		print "INSERIRE CODICE!"
		del lista[0:99]
		return				
			
def spacchetta(pacchetto):
	comando = pacchetto[0]
	parametro = pacchetto[1:-1]
	checksum = pacchetto[-1]
	chk = calcola_checksum (comando, parametro)		
	if chk == checksum:
		return "OK"
	else:
		return "NO"
	

pacchetto = ""
lista = []

while True: 
	s = ser.read(1) 
	if len(s)>0:	
		pacchetto="".join([pacchetto,s])
	else:
		if len(pacchetto)>=3:
			s = spacchetta(pacchetto)
			if s == "OK":
				numero_codice = pacchetto[-2]
				if numero_codice == "\x08":
					verifica(lista)
				elif numero_codice == "\x3c":
					if len(lista)>0:
						for i in range (0, len(lista)):
							print lista[i]
						del lista [-1]
				else:
					lista.append (numero_codice)
					scrivi_su_stringa (numero_codice)
		pacchetto = ""
	
ser.close()
