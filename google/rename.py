import xlwt
import os
import shutil

files = [f for f in os.listdir('.') if os.path.isfile(f)]

for file in files:
	if file[len(file)-4:len(file)] != '.csv':
		continue
	print(file)
	#os.rename(file, file[len(file)-4:len(file)]+'jimmy'+'.csv')
	shutil.move(file, file+'jimmy')
	#rename the files to jimmy