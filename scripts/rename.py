'''
Author:        Erfan Azad
Date:          5 Jan 2017
Discription:   A filename convertor for Photoes and Datasheet folders.
			   HAS TO BE MODIFIED FOR numbers LARGER THAN 2099 in the filename
'''

import os

#sorting and reversing the name orders are important 
#because otherwise there will be a clash during the renaming process
for filename in sorted(os.listdir("."), reverse=True): 
	if filename.startswith("20"):
		number = filename[0:4]
		rest = filename[4:]
		newNumber = int(number) + 1
		# newName = "{}{}".format(newNumber,filename[4:]) #for photoes
		newName = "{}{}".format(newNumber,rest) #for datasheets
		os.rename(filename, newName)
		print(filename,number,rest, newName)

