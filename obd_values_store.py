import obd
from obd import OBDStatus
import time
f = open('car_values.txt','w')
connection = obd.OBD()
i=0
while(i==0):
	if(OBDStatus.NOT_CONNECTED):
		i=1
	else:
		
		print("working")
		f.write(' '.join(( "SPEED--",str(2),"  ")))
		rpm = connection.query(obd.commands.RPM)
		if not rpm.is_null():
			print(rpm.value)
		f.write(' '.join(( "RPM--",str(rpm.value),"  ")))
		time.sleep(0.3)
		speed=connection.query(obd.commands.SPEED)
		if not speed.is_null():
			print("speed",speed.value)
		f.write(' '.join(( "SPEED--",str(speed.value),"  ")))
		time.sleep(0.3)
		el=connection.query(obd.commands.ENGINE_LOAD)
		if not el.is_null():
			print("e-load",el.value)
		f.write(' '.join(( "ENGINE LOAD--",str(el.value),"  ")))
		time.sleep(0.3)
		c_temp=connection.query(obd.commands.COOLANT_TEMP)
		if not c_temp.is_null():
			print("temp= ",c_temp.value)
		time.sleep(0.3)
		f.write(' '.join(( "COOLANT TEMP--",str(c_temp.value),"\n")))
		f_type=connection.query(obd.commands.FUEL_TYPE)
		if not f_type.is_null():
			print("fuel type",f_type.value)
		#f.write(' '.join(( "FUEL_TYPE",str(f_type),"  ")))
				
	
	
	
	

		
	 
	
	
	


		
		
	
	
