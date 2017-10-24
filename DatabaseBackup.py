#!/usr/bin/python
#########################################################
#							#
# This python script is used for mysql database backup	#
# using mysqldump utility.				#
#							#
# Written by: Rahul Kumar				#
# Website: https://tecadmin.net				#
# Created date: Dec 03, 2013				#
# Last modified: Dec 03, 2013				#
# Tested with: Python 2.6.6				#
# Script Revision: 1.1					#
#							#
#########################################################
#							#
# Edited by: Sam Pepper					#
#							# 
#########################################################

import os
import time
import datetime

DB_HOST = 'localhost'
DB_USER = 'root'
DB_USER_PASSWORD = 'password'
DB_NAME = 'Charts'
BACKUP_PATH = '/backup/dbbackup/'

DATETIME = time.strftime('%m%d%Y-%H%M%S')

TODAYBACKUPPATH = BACKUP_PATH + DB_NAME + "-" + DATETIME

f = open('LastWorkingDatabase.txt' , 'w')
f.write(TODAYBACKUPPATH)
f.close() 

print "creating backup folder"
if not os.path.exists(TODAYBACKUPPATH):
    os.makedirs(TODAYBACKUPPATH)


db = DB_NAME
dumpcmd = "mysqldump -u " + DB_USER + " -p" + DB_USER_PASSWORD + " " + db + " > " + TODAYBACKUPPATH + "/" + db + ".sql"
os.system(dumpcmd)

print "Database successfully backed up."
print "Your backup has been created in the: '" + TODAYBACKUPPATH + "' directory."
