import time
import serial.tools.list_ports

ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()

portsList = []
port_var = 'COM3'


for port in ports:
    portsList.append(str(port))
    

if not any(port.startswith(port_var) for port in portsList):
    val = input("Select Port : COM")
    port_var = "COM" + str(val)

serialInst.baudrate = 9600
serialInst.port = port_var

serialInst.open()

time.sleep(2)
  
command = "ON\n"
serialInst.write(command.encode('utf-8'))
