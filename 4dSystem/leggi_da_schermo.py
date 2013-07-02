import serial

 
ser = serial.Serial(

    port='/dev/ttyUSB0', 

    baudrate=9600, 

    timeout=1,

    parity=serial.PARITY_NONE,

    stopbits=serial.STOPBITS_ONE,

    bytesize=serial.EIGHTBITS

)  



def verifica (lista):
	
	if len(lista)>0:
	
		if lista[0] == "1":
			if lista[1] == "7":
				if lista[2] == "0":
					if lista[3] == "5":
						if lista[4] == "0":
							if lista[5] == "9":
								ser.write ("\xFF")
								ser.write ("\xB4")
								ser.write ("\x00")
								ser.write ("\x00")
								ser.write ("\x00")
								ser.write ("\x1F")
								while True: 
									s = ser.read(1)
									if len(s)>0:	
										print "%02x" % ord(s)
								del lista[0:6]
								return
							
		if lista[0] == "9":
			if lista[1] == "0":
				if lista[2] == "5":
					if lista[3] == "0":
						if lista[4] == "7":
							if lista[5] == "1":
								print "OK! USER 2"
								del lista[0:6]
								return
							
	else:
		print "ERROR!"
		del lista[0:99]
		return				






sr = ""
lista = []



while True: 

	
	s = ser.read(1) 
	
	if len(s)>0:	
				
		se = "%02x" % ord(s)
		
		sr = " ".join([sr, se])
		
		if sr == " 07 0d 00 00 30 3a":
			 lista.append ("0")
			 sr = ""
		
		if sr == " 07 0d 00 00 31 3b":
			 lista.append ("1")
			 sr = ""
		
		if sr == " 07 0d 00 00 32 38":
			 lista.append ("2")
			 sr = ""
		
		if sr == " 07 0d 00 00 33 39":
			 lista.append ("3")
			 sr = ""
		
		if sr == " 07 0d 00 00 34 3e":
			 lista.append ("4")
			 sr = ""
		
		if sr == " 07 0d 00 00 35 3f":
			 lista.append ("5")
			 sr = ""
		
		if sr == " 07 0d 00 00 36 3c":
			 lista.append ("6")
			 sr = ""
			 
		
		if sr == " 07 0d 00 00 37 3d":
			 lista.append ("7")
			 sr = ""
		
		if sr == " 07 0d 00 00 38 32":
			 lista.append ("8")
			 sr = ""
		
		if sr == " 07 0d 00 00 39 33":
			 lista.append ("9")
			 sr = ""
		
		if sr == " 07 0d 00 00 3c 36":
			 if len(lista)>0:
				del lista[-1]	
			 sr = ""
			 
		if sr == " 07 0d 00 00 08 02":
			verifica (lista)
			sr = ""

			 
ser.close()


