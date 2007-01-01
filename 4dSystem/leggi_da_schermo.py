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

def spacchetta(pacchetto):
	for i in range(0,len(pacchetto)):
		print "%02x" % ord(pacchetto[i])
	return 0

pacchetto = ""
while True: 
	s = ser.read(1) 
	if len(s)>0:	
		pacchetto="".join([pacchetto,s])
	else:
		if len(pacchetto)>0:
			spacchetta(pacchetto)
			pacchetto=""
			
ser.close()


