# coding: utf-8
import os  
import time
import datetime

#Variables
LOGFILE_PATH = "/Users/gymnasiumundtechnikteam/Desktop/logfile.csv"

#Get CPU Temperature
def getCPUtemperature():  
    return os.popen('vcgencmd measure_temp').readline()  

#Load Files
loggingfile = open(LOGFILE_PATH, "a")

new_data = datetime.datetime.now().strftime("%d.%m.%y;%H:%M:%S")

loggingfile.write("\n{};{};{};{};{}".format(new_data, "Test", "Test", "Test", "Test"))