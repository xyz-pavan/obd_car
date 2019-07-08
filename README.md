# obd_car
On-board diagnostics:
On-board diagnostics (OBD) is a vehicle's self-diagnostic and reporting capability. OBD systems give the vehicle owner or a repair technician access to the status of the various vehicle subsystems.
We are dealing with obd 2.

Problem statement:
We are using ELM327 obd adapter (connector from car obd to pc).
The ELM327 is connected between car’s obd to raspberry pi.
We request certain parameter values from obd and store those parameter values from time to time.





STEP1:
Serial Connection between Car’s obd and raspberry pi.
Checking the communication between obd and raspberry pi.
Refer to code(obd_port_connection).
We are using pyobd library for this task.






STEP2:
Reading the parameter value from obd and displaying in 
Raspberry pi terminal .
We are communicating with raspberry pi in the car using ssh 
Refer to code(test.py).






STEP3:
Continuously display the values when there is connection.
Five parameters have been requested every time.
There is delay of 0.3 seconds between each parameter request because
Only 5 requests can be done from  in 1 second .
The parameters we displayed are :
1.RPM
2.SPEED
3.COOLANT TEMPERATURE
4.ENGINE_LOAD
5.Fuel_level.
Fuel level is not supported by the car we are testing.
There is code given by obd when there is a request 
to  fuel_level and fuel_type.
Refer to code(obd_values_display.py)




Step4:
We are continuously displaying the values of the parameters when is 
an  available connection between obd and raspberry pi.
Now we store the values that are requested into a text file until there is a connection between raspberry pi and OBD .
Refer to the code(obd_values_store.py).







