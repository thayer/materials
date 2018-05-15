
# coding: utf-8

# In[36]:

'''
Erfan Azad <erfan@dartmouth.edu>
This file contains a script for creating a .csv file from all the .md contents/files in the 
_processes folder. This is done in order to be able to have a datasheet to future manupulation
of all the processes at once, similar to material/productCreator scripts.
'''


# In[8]:

import os
import sys
import csv

def main():
    fo = open("processes_information.csv", 'wt')
    writer = csv.writer(fo)
    headerRow = ['name', 'class', 'subclass', 'subsubclass','photo', 'location', 'description']
    rows = [headerRow]


    directory = "../_processes"
    for filename in os.listdir(directory):
        if filename.endswith(".md"):
            fi = open(directory+"/"+filename, 'r')
            row = []
            lines = fi.readlines()
            lineNumIndex = 0
            for line in lines:
                if "process_name" in line:
                    name = line.split(':',1)[1].strip()
                    row.append(name)
                elif "process_class" in line:
                    processClass = line.split(':',1)[1].strip()
                    row.append(processClass)
                elif "process_subclass" in line:
                    subclass = line.split(':',1)[1].strip()
                    row.append(subclass)
                elif "process_sub_subclass" in line:
                    subsubclass = line.split(':',1)[1].strip()
                    row.append(subsubclass)
                elif "primary_photo_path" in line:
                    photo = line.split('/')[-1].strip().split('.')[0].strip()
                    row.append(photo)
                elif "places:" in line:
                    nextLineIndex = lineNumIndex+1
                    location = ""
                    while(lines[nextLineIndex][0:3] == "  -"):
                        location += '-' + (str)(lines[nextLineIndex]).strip() + "\n"
                        nextLineIndex += 1
                    row.append(location.strip())
                elif "---" in line and lineNumIndex > 1:
                    if len(row) < 6: #There were no 'places' field 
                        row.append("")
                    subList = lines[lineNumIndex+1:len(lines)]
                    description = ""
                    for line in subList:
                        description += (str)(line)
                    row.append(description.strip())
                lineNumIndex += 1
            fi.close() 
            rows.append(row)

    writer.writerows(rows)
    fo.close()


# In[ ]:

if __name__ == "__main__":
    main()

