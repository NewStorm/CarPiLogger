#from os.path import expanduser
import os
import datetime
import shutil
from fileinput import filename

HOME = os.path.expanduser("~")
LOG_PATH_LIST = ["/var/log/piupsmon.log", "/var/log/syslog", HOME+"logfile.csv"]

if not os.path.isdir(HOME+"/logs/"):
        os.mkdir(HOME+"/logs/")
        
TIMESTAMP = datetime.datetime.now().strftime("%d_%m_%y_%H_%M_%S")
LOG_FOULDER = HOME+"/logs/"+TIMESTAMP+"/"
os.mkdir(LOG_FOULDER)
for path in LOG_PATH_LIST:
    if os.path.exists(path):
        filename = os.path.basename(path)
        shutil.copy2(path, HOME+"/logs/"+TIMESTAMP+"/" + filename)
        
print shutil.make_archive(HOME + "/" + TIMESTAMP, "gztar",HOME+"/logs/"+TIMESTAMP+"/" )