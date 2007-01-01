import serial
 
ser = serial.Serial(
    port='/dev/ttyS4', 
    baudrate=9600, 
    timeout=0.5,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)  

def verifica (lista):
	if len(lista)>0:
		if (lista[0],lista[1],lista[2],lista[3],lista[4],lista[5]) == ("1","7","0","5","0","9"):
			ser.write ("\x43")
			ser.write ("\x00")
			ser.write ("\x3F")
			ser.write ("\x00")
			ser.write ("\x3F")
			ser.write ("\x00")
			ser.write ("\x22")
			ser.write ("\x00")
			ser.write ("\x1F")
			
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


def calcola_checksum (comando, parametro):
	com = ord(comando)
	for i in range (0, len(parametro)):
		com = com ^ ord(parametro[i])
	com = chr(com)
	return com
		
				
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
			
	#		comando = chr(int("0x01", 16))
	#		par1 = chr(int("0x0A",16))
	#		par2 = chr(int("0x01",16))
	#		par3 = chr(int("0x00",16))
	#		par = "".join([par1,par2,par3])
	#		checksum = calcola_checksum(comando,par)
	#		print "%02x" % ord(checksum)
			
			ser.write("\x01")
			ser.write("\x0A")
			ser.write("\x01")
			ser.write("\x00")
			ser.write("\x00")
			ser.write("\x0A")
			
			
						
			
			print "%02x" % ord(ser.read(1))
			
ser.close()
