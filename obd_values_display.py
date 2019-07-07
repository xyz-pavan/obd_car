import obd
from obd import OBDStatus
import time
connection = obd.OBD()

el = connection.query(obd.commands.ENGINE_LOAD)
if not el.is_null():
	print(el.value)
time.sleep(0.3)
fuel=connection.query(obd.commands.FUEL_LEVEL)
if not fuel.is_null():
	print("fuel-",fuel.value)
time.sleep(0.3)
rpm_array=[]
i=0
with open ('rpm_values1.txt','w') as f:
	while(OBDStatus.CAR_CONNECTED):
		print("working")
		rpm = connection.query(obd.commands.RPM)
		if not rpm.is_null():
			print(rpm.value)
			system = "RPM ",rpm.value
			rpm_array.append(system)
			f.write(str(rpm_array[i])+'\n')
			i=i+1
		time.sleep(0.3)
		speed=connection.query(obd.commands.SPEED)
		if not speed.is_null():
			print("speed",speed.value)
		time.sleep(0.3)
                el=connection.query(obd.commands.ENGINE_LOAD)
                if not el.is_null():
                        print("e-load",el.value)
                time.sleep(0.3)
                c_temp=connection.query(obd.commands.COOLANT_TEMP)
                if not c_temp.is_null():
                        print("temp= ",c_temp.value)
                time.sleep(0.3)
                f_type=connection.query(obd.commands.FUEL_TYPE)
                if not f_type.is_null():
                        print("fuel type",f_type.value)

		
	 
	
	
	


		
		
	
	
