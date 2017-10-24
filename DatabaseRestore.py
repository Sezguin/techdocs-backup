#!/usr/bin/python
#########################################################
#							#
# Restore functionality included for the database.	#
#							#
# Created by: Sam Pepper				#
#							#
#########################################################

import os

DB_HOST 		= 'localhost'
DB_USER 		= 'root'
DB_USER_PASSWORD 	= 'password'
DB_NAME 		= 'Charts'

f = open('LastWorkingDatabase.txt','r')
RESTOREBACKUPPATH = f.read()
f.close()

db = DB_NAME
dumpcmd = "mysql -u " + DB_USER + " -p " + db + " < " + RESTOREBACKUPPATH + "/" + db + ".sql"
os.system(dumpcmd)

print "\n###########################################################\n"
print "Database restored successfully."
print "Your database was restored from the: '" + RESTOREBACKUPPATH + "' directory."
print "\n###########################################################\n"
