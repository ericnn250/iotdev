import sys
import Adafruit_DHT
import time
import datetime

while True:
	humidity, temperature = Adafruit_DHT.read_retry(11,4)
	print ('Temp: ' + str(temperature))
	print ('Humid: ' + str(humidity))
	x = datetime.datetime.now()
	print("=========")
	
	if temperature <=28:
		print("Excess")	
	time.sleep(1)

