
# coding: utf-8

# In[6]:

'''
Author:
    Erfan Azad (erfan@dartmouth.edu)

Date:
    27 January 2017
    
Description:
    This script opens a CSV database of products
    and automatically creates a .md file with
    corresponding YAML for each product.
'''

import csv
    
def makeProductFileUsingRow(row, outputFilename):
    content = "---\n" #initialize YAML 
    content += "product_name: \"{}\"\n".format(row[4].strip()) #Name
    print(row[4].strip())
    content += "index_letter: {}\n".format(row[4].strip()[0].upper().strip()) #Index letter
    content += "class: {}\n".format(row[2].strip()) #Class
    content += "subclass: {}\n".format(row[3].strip()) #Subclass

    #Componenets
    content += "components:\n"
    comps = row[7].split("-")[1:]
    masses = [mass.strip().split("_") for mass in row[10].split("-")[1:]]
    materials = [material.strip().split("_") for material in row[8].split("-")[1:]]
    processes = [process.strip().split("_") for process in row[9].split("-")[1:]]
    counter = 1
    for comp in comps:
        content += "  - {}:\n".format(comp.strip())
        for mass in masses:
            if (int(mass[0]) == counter):
                content += "    - mass: {}\n".format(mass[1])
        content += "    - materials:\n"
        for material in materials:
            if (int(material[0]) == counter and material[1] != ""):
                content += "      - {}\n".format(material[1])
        content += "    - processes:\n"
        for process in processes:
            if (int(process[0]) == counter and process[1] != ""):
                content += "      - {}\n".format(process[1])
        counter += 1

    content += "manufacturer: \"{}\"\n".format(row[11].strip()) #Manufacturer
    content += "cost: {}\n".format(row[12].strip()) #Cost
    content += "DOP: {}\n".format(row[14].strip()) #Date of purchase
    content += "POP: {}\n".format(row[13].strip()) #Place of purchase
    content += "product_description: \"{}\"\n".format(row[15].strip()) #Product Description
    content += "materials_and_processes_description: \"{}\"\n".format(row[16].strip())  # Materials and Processes description
    if(row[0].strip() == ""):
        content += "primary_photo_path: \"\"\n"    #Primary Photo Path
    else:
        content += "primary_photo_path: /photos/{}.jpg\n".format(row[0].strip().split("/")[0].strip()) #Primary Photo Path
    content += "link_to_manufacturer_website: \"{}\"\n".format(row[18].strip()) #Link to manufacturer
    content += "additional_photos:\n"
    if(row[1].strip() == "N/A" or row[1].strip() == ""):
        content += "  - additional_photo_path: \"\"\n"   #No Additional Photo
    else:
        photos = row[1].strip().split('-')[1:]
        for photo in photos:
            content += "  - additional_photo_path: /photos/{}.jpg\n".format(photo.strip()) #Additional Photo
    
    content += "HIMvideos:\n"                      # How it is made videos
    HIMvideos = row[19].strip().split("*")[1:]
    for video in HIMvideos:
        content += "  - {}\n".format(video.strip())
        
    content += "---\n" #End of YAML
    
    output = open(outputFilename, 'w')
    output.write(content)
    output.close()
    
    
def main():
    raw = open("Products Information Spreadsheet - Sheet1.csv", 'r')
    data = csv.reader(raw, delimiter=',')

    outputFilenameCounter = 3000
    for row in data:
        if outputFilenameCounter > 3208:
            break; # the rest of the product datasheet is not ready yet!
        print(outputFilenameCounter)
        if (outputFilenameCounter != 3000): #ignore the header row
            filename = "../_products/{}.md".format(outputFilenameCounter)
#             filename = "test/{}.md".format(outputFilenameCounter)
            makeProductFileUsingRow(row, filename)
        else:
            print(row)
        outputFilenameCounter += 1
        


# In[7]:

if __name__ == "__main__":
    main()


# In[ ]:



