
# coding: utf-8

# In[1]:

'''
Author:
    Erfan Azad (erfan@dartmouth.edu)

Date:
    10 February 2017
    
Description:
    This script opens a CSV database of materials
    and automatically creates a .md file with
    corresponding YAML for each material.
'''

import csv


# In[23]:

def makeMaterialFileUsingRow(row, outputFilename):
    content = "---\n" # Start YAML
    
    content += "material_name: \"{}\"\n".format(row[3].strip()) # Name
    content += "index_letter: {}\n".format(row[3].strip()[0].upper())
    content += "material_class: {}\n".format(row[4].strip())    # Class
    content += "material_subclass: \"{}\"\n".format(row[5].strip()) # Subclass
    content += "primary_photo_path: /photos/{}.jpg\n".format(row[0].strip()) # Primary photo
    
    content += "additional_photos:\n"   # Additional Photos
    Additional_photoes = row[2].strip().split("-")[1:]
    for photo in Additional_photoes:
        content += "  - additional_photo_path: /photos/{}.jpg\n".format(photo.strip())
    
    content += "general_applications: \"{}\"\n".format(row[7].strip().replace("\"","\'")) # General Applications
    content += "description: \"{}\"\n".format(row[6].strip().replace("\"","\'"))          # Description  
    
    content += "relations:\n"    # Relations
    content += "  - materials:\n" # PLACEHOLDER: In case we wanted to relate one material to another later using cloudCannon
    content += "  - processes:\n"
    related_processes = row[8].strip().split("-")[1:]
    for process in related_processes:
        content += "    - \"{}\"\n".format(process.strip())
    content += "  - products:\n"
    related_products = row[9].strip().split("-")[1:]
    for product in related_products:
        content += "    - \"{}\"\n".format(product.strip())

    
    content += "---\n" # End YAML
    
    output = open(outputFilename, 'w')
    output.write(content)
    output.close()
    


# In[25]:

def main():
    raw = open("Materials_Datasheet_Info - Sheet1.csv", 'r')
    data = csv.reader(raw, delimiter=',')

    outputFilenameCounter = 1000
    for row in data:
        if(outputFilenameCounter != 1000):
            filename = "../_materials/{}.md".format(outputFilenameCounter)
            makeMaterialFileUsingRow(row, filename)

        else:
            print(row)
        outputFilenameCounter += 1


# In[ ]:

if __name__ == "__main__":
    main()

