import pypyodbc

# Create Connection
con = pypyodbc.connect('DRIVER={Microsoft Access Driver (*.mdb)};UID=admin;UserCommitSync=Yes;Threads=3;SafeTransactions=0;PageTimeout=5;MaxScanRows=8;;MaxBufferSize=2048FIL={MS Access};DriverId=25;DefaultDir=C:/Users/vasan/OneDrive/Documents;DBQ=C:/Users/vasan/OneDrive/Documents/Database2.mdb;')

cursor = con.cursor()

cursor.execute("SELECT * FROM details")

for row in cursor.fetchall():
     print(row)
