import serial
import screen_read
 
ser = serial.Serial(
    port='/dev/ttys4', 
    baudrate=9600, 
    timeout=0.1,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)  

def goto_form (index):
	
	lista = ["\x01","\x0A",chr(index),"\x00","\x00"]
	ls1 = lista[0]	
	for i in range (1, len(lista)):
		ls1 = calcola_checksum(ls1, lista[i])
	lista.append(ls1)
	for i in range (0, len(lista)):
		ser.write(lista[i])

def scrivi_su_stringa (index, numero_codice):
	
	lista = ['\x02', chr(index), '\x01',chr(ord(numero_codice))]
	ls1 = ls_ser[0]	
	for i in range (1, len(lista)):
		ls1 = calcola_checksum(ls1, lista[i])
	lista.append(ls1)
	for i in range (0, len(lista)):
		ser.write(ls_ser[i])
		
def light_led (index, bit):
	lista = ["\x01","\x0E",chr(index),"\x00",chr(bit)]
	ls1 = lista[0]	
	for i in range (1, len(lista)):
		ls1 = calcola_checksum(ls1, lista[i])
	lista.append(ls1)
	for i in range (0, len(lista)):
		ser.write(lista[i])






















