--- Structure ---

script/
This folder contains all the scripts and spreadsheets used for creating the pages and the QR codes


scripts/materialCreator.py
This script uses the "Materials_Datasheet_Info - Sheet1.csv" file to create all the material pages

script/processCreator.py
This script uses the "processes_information - Sheet1.csv" file to create all the process pages

script/productCreator.py
This script uses the "Products Information Spreadsheet - Sheet1.csv" file to create all the product pages

script/processes2CSV.py
Initially all process pages were created manually. This script took those pages (.md files) and created a .csv from it so later "processCreator.py" can be born to help with automatic creation of process pages from a .csv file. You should not need to use this anymore.

script/ImageSizer.py
This script resizes and pads all the photos so they will have consistant shape and size

script/QR_script.py
This script creates QR codes for url strings and then attaches numbers under them.

photos/
This folder contains all the photos that are used in materials, processes and product pages.

--- How To Run The Scripts? ---
The script are written in python. so first you need to make sure you have python on your computer.
-open terminal(mac) or command prompt (windows) and type python in them. If you get an error then you should google "how to install python"
-From within terminal/command prompt navigate to where the scripts are located (using 'cd' for changing directory)
-In that directory type "python scriptNameHere.py" (without quotes)
