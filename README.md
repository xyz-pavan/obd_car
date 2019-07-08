# obd_car
**On-board diagnostics:**
On-board diagnostics (OBD) is a vehicle's self-diagnostic and reporting capability. OBD systems give the vehicle owner or a repair technician access to the status of the various vehicle subsystems.\
We are dealing with obd 2.
\
\
\

**Problem statement:**
We request certain parameter values from car diagnostics obd and store those parameter values from time to time.\
We are using ELM327 obd adapter (connector from car obd to pc).\
The ELM327 is connected between car’s obd to raspberry pi.\
\
\
\

The ELM327 is a programmed microcontroller produced by ELM Electronics for translating the on-board diagnostics (OBD) interface found in most modern cars\

Parameters supported by ELM327 :\
1.Read diagnostic trouble codes, both generic and manufacturer-specific, and display their meaning (over 3000 generic code definitions in the database).\
2.Clear trouble codes and turn off the MIL (Malfunction Indicator Light", more commonly known as the "Check Engine Light")\
3.Display current sensor data\
4.Engine RPM\
5.Calculated Load Value\
6.Coolant Temperature\
7.Fuel System Status\
8.Vehicle Speed\
9.Short Term Fuel Trim\
10.Long Term Fuel Trim\
11.Intake Manifold Pressure\
12.Timing Advance\
13.Intake Air Temperature\
14.Air Flow Rate\
15.Absolute Throttle Position\
16.Oxygen sensor voltages/associated short term fuel trims\
17.Fuel System status\
18.Fuel Pressure\
\
\
To know more about ELM327 refer[ELM327](https://en.wikipedia.org/wiki/ELM327) webiste.



**STEP1:**"\
Serial Connection between Car’s obd and raspberry pi.\
Checking the communication between obd and raspberry pi.\
Refer to code([obd_port_connection.py](https://github.com/xyz-pavan/obd_car/blob/master/obd_port_connection.py)).\
We used open source library library for dealing with obd 2 and ELM327 i.e, pyobd.
 [PYOBD ](https://python-obd.readthedocs.io/en/latest/) source.

![alt text](https://github.com/xyz-pavan/obd_car/blob/master/Selection_005.png)

\
\
\

**STEP2:**\
Reading the parameter value from obd and displaying in 
Raspberry pi terminal .\
We are communicating with raspberry pi in the car using ssh \
Refer to code([obd_values_display.py](https://github.com/xyz-pavan/obd_car/blob/master/obd_values_display.py)).\




\
\
\

**STEP3:**\
Continuously display the values when there is connection.\
Five parameters have been requested every time.\
There is delay of 0.3 seconds between each parameter request because
Only 5 requests can be done from  in 1 second .\
The parameters we displayed are :\
1.RPM\
2.SPEED\
3.COOLANT TEMPERATURE\
4.ENGINE_LOAD\
5.Fuel_level.\
Fuel level is not supported by the car we are testing.\
There is code given by obd when there is a request 
to  fuel_level and fuelhttps://github.com/xyz-pavan/obd_car/blob/master/Selection_003.png_type.\
#Refer to code(obd_values_display.py)\
![alt text](https://github.com/xyz-pavan/obd_car/blob/master/Selection_003.png)
\
In the above code temp.py is actually obd_values_display.py.
Here the car is not connected so the obd is giving empty code (NULL CODE).

\
\



**Step4:**\
We are continuously displaying the values of the parameters when is 
an  available connection between obd and raspberry pi.\
Now we store the values that are requested into a text file until there is a connection between raspberry pi and OBD .\
Refer to the code([obd_values_store.py](https://github.com/xyz-pavan/obd_car/blob/master/obd_values_store.py)).







