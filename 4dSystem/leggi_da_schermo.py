import serial

 
ser = serial.Serial(

    port='/dev/ttyS4', 

    baudrate=115200, 

    timeout=1,

    parity=serial.PARITY_NONE,

    stopbits=serial.STOPBITS_ONE,

    bytesize=serial.EIGHTBITS

)  

while True: 

	s = ser.read(1) 

	if len(s)>0:

		print "%02x" % ord(s)


ser.close()
