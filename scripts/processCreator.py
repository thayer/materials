
# coding: utf-8

# In[14]:

'''
Author:
    Erfan Azad (erfan@dartmouth.edu)

Date:
    23 April 2017
    
Description:
    This script opens a CSV database of processes
    and automatically creates a .md file with
    corresponding YAML for each process.
'''


# In[3]:

import csv


# In[4]:

def makeProcessFileUsingRow(row, outputFilename):
    content = "---\n" # Start YAML
    
    content += "process_name: \'{}\'\n".format(row[0].strip()) # Name
    content += "index_letter: {}\n".format(row[0].strip()[0].upper()) # Index Letter
    content += "process_class: \'{}\'\n".format(row[1].strip().strip('"')) # Class
    content += "process_subclass: \'{}\'\n".format(row[2].strip().strip("'")) # Subclass
    content += "process_sub_subclass: \'{}\'\n".format(row[3].strip("'")) # Subsubclass
    content += "primary_photo_path: /photos/{}.png\n".format(row[4].strip()) # Primary photo path
    
    content += "places: \n" # Places
    places = row[5].strip().split("--")[1:]
    for place in places:
        content += "  - {}\n".format(place.strip())
        
    content += "description: \"{}\"\n".format(row[8].strip().replace("\"","\'")) # Description
    
    content += "relations: \n" # Relations - materials
    content += "  - materials: \n"
    materialRelations = row[6].strip().split("--")[1:]
    for material in materialRelations:
        material = material.strip().split('(')[0].strip()
        content += "    - {}\n".format(material)
    
    content += "  - processes: \n" # Relations - processes (possibly in future!)
    
    content += "  - products: \n" # Relations - products
    productRelations = row[7].strip().split("--")[1:]
    for product in productRelations:
        product = product.strip().split('(')[0].strip()
        content += "    - {}\n".format(product)
        
    content += "---\n" # End YAML
    
    output = open(outputFilename, 'w')
    output.write(content)
    output.close()
    


# In[6]:

def main():
    raw = open("processes_information - Sheet1.csv", 'r')
    data = csv.reader(raw, delimiter=',')

    outputFilenameCounter = 2000
    for row in data:
        if(outputFilenameCounter != 2000):
            filename = "../_processes/{}.md".format(outputFilenameCounter)
    #         filename = "test/{}.md".format(outputFilenameCounter)
            makeProcessFileUsingRow(row, filename) 
        else:
            print(row)
        outputFilenameCounter += 1

    raw.close()


# In[ ]:

if __name__ == "__main__":
    main()

