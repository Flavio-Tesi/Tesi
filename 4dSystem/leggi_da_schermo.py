import serial
 
ser = serial.Serial(
    port='/dev/ttyS4', 
    baudrate=9600, 
    timeout=0.5,
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
	
#	hesa = "%02x" % ord(chr(index))	
#	print hesa
#	print hesa[0]
#	print hesa[1]
#	stringa = "".join(["\\", "x",hesa[0], hesa[1]])

def create_string_hex (index):
	
	stringa = "\\x%x" % index
	
	print stringa
	return stringa

def goto_form (index):
	
	ind = create_string_hex (index)
	
	lista = ["\x01","\x0A",ind,"\x00","\x00"]
			
	ls1 = ord(lista[0])
	print "ciaooooooo"
	print lista[0]
	print ls1
	print ind
			
	
	for i in range (0, len(lista)):
		print "%02x" % ord(lista[i])		
		
			
	for i in range (1, len(lista)):
		ls1 = calcola_checksum(ls1, ord(lista[i]))
		
	ls1 = hex(ord(ls1)) 	# DA ESADECIMALE A STRINGA??
	
	lista.append(ls1)
	
	for i in range (0, len(lista)):
		print lista[i]		


def verifica (lista):
	if len(lista)>0:
		if (lista[0],lista[1],lista[2],lista[3],lista[4],lista[5]) == ("1","7","0","5","0","9"):
			goto_form(1)
			
			while True: 
				s = ser.read(1)
				if len(s)>0:	
					print "%02x" % ord(s)
			del lista[0:6]
			return
							
		elif (lista[0],lista[1],lista[2],lista[3],lista[4],lista[5]) == ("9","0","5","0","7","1"):		
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

while True: 
	s = ser.read(1) 
	if len(s)>0:	
		pacchetto="".join([pacchetto,s])
	else:
		if len(pacchetto)>=3:
			spacchetta(pacchetto)
			pacchetto=""
						
			
			print "%02x" % ord(ser.read(1))
			
ser.close()
