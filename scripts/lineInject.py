'''
Author: Erfan Azad
Date: 11 Jan 2017
Description: Script to inject a string in a text file 
			 in the requested line or by following a pattern.
'''
import os
import sys

def getEndOfYAMLIndex(filename):
	'''
	Gets a filename and returns the index
	of the line where "---" appears for the
	second time. 
	NOTE: "---" indicates the start and
	end of the YAML portion of a file.

	Returns: The index of the end of YAML or None
	'''
	YAML_started = False
	index = 0
	file = open(filename, 'r')
	lines = file.readlines()
	for line in lines:
		if ((line == "---\n") and (YAML_started == False)):
			YAML_started = True
		elif ((line == "---\n") and (YAML_started == True)):
			return [index, lines]
		index += 1
	file.close()
	return None

def main():
	fileTypeIndex = input("What is the type of file you are writing to? (type the corresponding number)\n [materials --> 0]\n [processes --> 1]\n [products  --> 2]\n")
	
	materials_lineToWrite = "relations:\n  - materials:\n  - processes:\n  - products:\n" #for processes
	processes_lineToWrite = "  - materials:\n  - processes:\n  - products:\n" #for processes
	products_lineToWrite = "" #for products

	injection_strings = [materials_lineToWrite, processes_lineToWrite, products_lineToWrite]

	for filename in os.listdir("."): # for all the files in the directory
		if (filename[0:4].isdigit()): # if they are starting with 4 numbers e.g. 2001.md 
			print(filename)
			[EndIndex, content] = getEndOfYAMLIndex(filename)
			if (EndIndex != None): # if end of YAML has been found
				file = open(filename, 'w')
				content.insert(EndIndex, injection_strings[fileTypeIndex])
				file.writelines(content)
				file.close()




if __name__ == "__main__":
	print("starting...")
	main()
	print("...Done!")
		


