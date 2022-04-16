import os
import zipfile
import shutil

dir_name = 'Raw Zip'
extension = ".zip"

# Unzip
for item in os.listdir(dir_name): # loop through items in dir
    if item.endswith(extension): # check for ".zip" extension
        file_name = os.path.join(dir_name, item)
        zip_ref = zipfile.ZipFile(file_name) # create zipfile object
        zip_ref.extractall(dir_name) # extract file to dir
        zip_ref.close() # close file

#Move to other folder
source_folder = "Raw Zip"
dest_folder = "Raw CSV Files"
for item in os.listdir(source_folder): 
    if(item.startswith("API") and item.endswith("csv")): 
        file_name = os.path.join(source_folder, item)
        shutil.move(file_name, os.path.join(dest_folder, item))
        
# Cleaning csv from zip folder
for item in os.listdir(dir_name):
    if item.endswith("csv"):
        file_name = os.path.join(dir_name, item)
        os.remove(file_name)