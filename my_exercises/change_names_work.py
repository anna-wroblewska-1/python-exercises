#App for work
#make folders for tiff and jpg
#get in every folder
#and take tiff files to tiff folder & jpg -> same
#change name from MEG-D-3000_1 to MEG_D_3000 (1), so
#change "-" to "_" and "_x" to "(x)"

import os
import re
import shutil

# Get path with script
#base_path = os.path.dirname(os.path.abspath(__file__))
base_path = '/Users/mac/Desktop/Desktop - MacBook Pro (Ania)/Data_Science/my_exercises'

# Path to folder which i want to search 
folder_path = os.path.join(base_path, 'File_names_changer')

# New paths for new folders
jpg_output_path = os.path.join(base_path, 'jpg_output')
tiff_output_path = os.path.join(base_path, 'tiff_output')

# Make new folders if they dont exist
os.makedirs(jpg_output_path, exist_ok=True)
os.makedirs(tiff_output_path, exist_ok=True)

# Function for searching in folders and copy files
def extract_image_files(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg')):
                src_path = os.path.join(root, file)
                dst_path = os.path.join(jpg_output_path, file)
                shutil.copy2(src_path, dst_path)
            elif file.lower().endswith(('.tiff', '.tif')):
                src_path = os.path.join(root, file)            
                dst_path = os.path.join(tiff_output_path, file)
                shutil.copy2(src_path, dst_path)

# Search in every folder for files and copy them
extract_image_files(folder_path)

# Loop through each file and rename it according to the conditions
def change_name(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):  # Ensure we're working with files only
            # Apply the replacement conditions
            # Replace '-' with '_'
            newer_name = filename.replace('-', '_')
            # Use regex to replace _<digit> with (<digit>)
            new_name = re.sub(r'_(\d)(?!.*_\d)', r' (\1)', newer_name)
        
            new_file_path = os.path.join(directory, new_name)
            os.rename(file_path, new_file_path)

change_name(jpg_output_path)
change_name(tiff_output_path)


    


