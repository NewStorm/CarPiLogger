# coding: utf-8
import os  
import time
import datetime

#Variables
LOGFILE_RELATIVE_PATH = "/logfile.csv"
CURRENT_PATH = os.path.dirname(os.path.realpath(__file__))
print(CURRENT_PATH)

#Get CPU Temperature
def getCPUtemperature():  
    return os.popen('vcgencmd measure_temp').readline()  

#Load Files
loggingfile = open(CURRENT_PATH + LOGFILE_RELATIVE_PATH, "a")

new_data = datetime.datetime.now().strftime("%d.%m.%y;%H:%M:%S")

loggingfile.write("\n{};{};{};{};{}".format(new_data, "Test", "Test", "Test", "Test"))