import serial
 
ser = serial.Serial(
    port='/dev/ttyUSB0', 
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

def goto_form (index):
	
	lista = ["\x01","\x0A",chr(index),"\x00","\x00"]
	ls1 = lista[0]	
	for i in range (1, len(lista)):
		ls1 = calcola_checksum(ls1, lista[i])
	lista.append(ls1)
	for i in range (0, len(lista)):
		ser.write(lista[i])

def verifica (lista):
	if len(lista)>0:
		lista_control1 = ['1','7','0','5','0','9']
		lista_control2 = ['9','0','5','0','7','1']
		
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


def scrivi_su_stringa (numero_codice):
	
	ls_ser = ['\x02', '\x00', '\x01',chr(ord(numero_codice))]
	ls1 = ls_ser[0]	
	for i in range (1, len(ls_ser)):
		ls1 = calcola_checksum(ls1, ls_ser[i])
	ls_ser.append(ls1)
	for i in range (0, len(ls_ser)):
		ser.write(ls_ser[i])
		
	

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
























