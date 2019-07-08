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
		f.write(' '.join(( "FUEL_TYPE",str(f_type),"  ")))
		time.sleep(0.3)


		short_term_fuel_trim= connection.query(obd.commands.RPM)
		if not short_term_fuel_trim.is_null():
			print("short_term_fuel_trim--",short_term_fuel_trim.value)
		f.write(' '.join(( "short_term_fuel_trim--",str(short_term_fuel_trim.value)," ")))
		time.sleep(0.3)

		##############################################
		long_term_fuel_trim=connection.query(obd.commands.SPEED)
		if not long_term_fuel_trim.is_null():
			print("long_term_fuel_trim--",long_term_fuel_trim.value)
		f.write(' '.join(( "long_term_fuel_trim--",str(long_term_fuel_trim.value),"  ")))
		time.sleep(0.3)

		##############################################
		intake_manifold_pressure=connection.query(obd.commands.ENGINE_LOAD)
		if not intake_manifold_pressure.is_null():
			print("intake_manifold_pressure--",intake_manifold_pressure.value)
		f.write(' '.join(( "intake_manifold_pressure--",str(intake_manifold_pressure.value),"  ")))
		time.sleep(0.3)

		##############################################
		timing_advance=connection.query(obd.commands.COOLANT_TEMP)
		if not timing_advance.is_null():
			print("timing_advance--",timing_advance.value)
		time.sleep(0.3)
		f.write(' '.join(( "timing_advance--",str(timing_advance.value)," ")))
		

		##############################################
		air_flow_rate=connection.query(obd.commands.FUEL_TYPE)
		if not air_flow_rate.is_null():
			print("air_flow_rate",air_flow_rate.value)
		f.write(' '.join(( "air_flow_rate--",str(air_flow_rate.value),"  ")))
		time.sleep(0.3)

		##############################################
		absolute_throttle_position=connection.query(obd.commands.FUEL_TYPE)
		if not absolute_throttle_position.is_null():
			print("absolute_throttle_position",absolute_throttle_position.value)
		f.write(' '.join(( "Absolute_throttle_position--",str(absolute_throttle_position.value),"  ")))
		time.sleep(0.3)

		##############################################
		fuel_pressure=connection.query(obd.commands.FUEL_TYPE)
		if not fuel_pressure.is_null():
			print("fuel_pressure --",fuel_pressure.value)
		f.write(' '.join(( "fuel_pressure--",str(fuel_pressure.value),"  ")))
		time.sleep(0.3)
				
	
	
	
	

		
	 
	
	
	


		
		
	
	
