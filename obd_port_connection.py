import obd
import obd_io
from obd import OBDStatus
import serial
from obd_utils import scanSerial


connection = obd.OBD() # auto connect

port="/dev/ttyUSB0"
if(OBDStatus.ELM_CONNECTED):
	#supp = port.sensor(0)[1]
	print("NOT- CONNECTED")
	#print(supp)
else:
	r = connection.query(obd.commands.RPM)


	if not r.is_null():
		print(r.value)
	print(r.value)
		

# no connection is made
#OBDStatus.NOT_CONNECTED # "Not Connected"
#OBDStatus.NOT_CONNECTED # "Not Connected"

# successful communication with the ELM327 adapter
#OBDStatus.ELM_CONNECTED # "ELM Connected"

# successful communication with the ELM327 adapter,
# OBD port connected to the car, ignition off
# (not available with argument "check_voltage=False")
#OBDStatus.OBD_CONNECTED # "OBD Connected"

# successful communication with the ELM327 and the
# vehicle; ignition on
#OBDStatus.CAR_CONNECTED # "Car Connected"

#connection = obd.OBD("/dev/ttyUSB0") # create connection with USB 0

# OR

#ports = obd.scan_serial()      # return list of valid USB or RF ports
#print ports                    # ['/dev/ttyUSB0', '/dev/ttyUSB1']
#connection = obd.OBD(ports[0]) 
