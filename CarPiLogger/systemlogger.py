# coding: utf-8
import os  
import time
import datetime

#Variables
LOGFILE_RELATIVE_PATH = "/logfile.csv"
CURRENT_PATH = os.path.dirname(os.path.realpath(__file__))
print(CURRENT_PATH)

#Sytem Information Methods
def getCPUtemperature():  
    return os.popen('vcgencmd measure_temp').readline()

def getVolts():
    res = os.popen('vcgencmd measure_volts').readline()
    return(res.replace("volt=","").replace("V\n",""))

def getCPUClock():
    res = os.popen('vcgencmd measure_clock arm | tr -d "frequency(45)="').readline()
    return res
                                                                 
def getRAMinfo():
    p = os.popen('free')
    i = 0
    while 1:
        i = i + 1
        line = p.readline()
        if i==2:
            return(line.split()[1:4])

def getDiskUsePercentage():
    res = os.popen('df -P | grep rootfs | tr -s " " " " | cut -d " " -f 5').readline()
    return res

def getUSVBatteryCurrent():
    res = os.popen('python piusv.py U_Batt').readline();
    return res

def getUSVExtCurrent():
    res = os.popen('python piusv.py U_ext').readline();
    return res

#Rumpf
#Load Files
loggingfile = open(CURRENT_PATH + LOGFILE_RELATIVE_PATH, "a")

#Generate Timestamp
timestamp = datetime.datetime.now().strftime("%d.%m.%y;%H:%M:%S")

#loggingfile.write("\n{};{};{};{};{};{};{};{};{}".format(timestamp, "CPU_Usage", "CPU_Temp", "CPU_Clock", "MEMORY_USE","DISK_USE","USV_BATT_CURR","RASP_CURR","USV_EXT_CURR"))
loggingfile.write("\n{};{};{};{};{};{};{};{}".format(timestamp, "CPU_Usage", getCPUtemperature(), getCPUClock(), getRAMinfo()[2], getDiskUsePercentage(), getUSVBatteryCurrent(),getVolts(),getUSVExtCurrent()))
