import serial
 
ser = serial.Serial(
    port='/dev/ttyS4', 
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
			print "evvivaaaa"
			goto_form(1)
			
			while True: 
				s = ser.read(1)
				if len(s)>0:	
					print "%02x" % ord(s)
			del lista[0:6]
			return
							
		elif lista == lista_control2:		
			print "OK! USER 2"
			del lista[0:6]
			return
								
		else:
			print "ERROR!"
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
		print "Comando=%02x" % ord(comando)
		print "Parametro:",
		for i in range(0,len(parametro)):
			print "%02x" % ord(parametro[i]),
		print ""	
		print "Checksum=%02x" % ord(checksum)
	return 0

pacchetto = ""
lista = []

while True: 
	s = ser.read(1) 
	if len(s)>0:	
		pacchetto="".join([pacchetto,s])
	else:
		if len(pacchetto)>=3:
			spacchetta(pacchetto)
			numero_codice = pacchetto[-2]
			
			if numero_codice == "\x08":
				verifica(lista)
			
			elif numero_codice == "\x3c":
				if len(lista)>0:
					del lista [-1]
			
			else:lista.append (numero_codice)
			
			pacchetto = ""
			
	#		print "%02x" % ord(ser.read(1))
			
ser.close()
























