#Appka do pracy
#baza danych z plikami tiff i jpg
#zmiana nazwy z MEG-D-3000_1 na MEG_D_3000 (1), czyli
#zmiana "-" na "_" i "_x" na "(x)"

import os
import glob2
import re

# Define the directory containing the files
directory = '/Users/mac/Desktop/Desktop - MacBook Pro (Ania)/Data_Science/my_exercises/Project_change_file_names'

# Define the pattern to search for files (e.g., all .tif files)
pattern_jpg = os.path.join(directory, '*.jpg')
pattern_tif = os.path.join(directory, '*.tif')

# Get a list of all files matching the pattern
jpg = glob2.glob(pattern_jpg)
tif = glob2.glob(pattern_tif)
files = jpg + tif
print(files)

# Loop through each file and rename it according to the conditions
for file in files:
    # Extract the file name from the full path
    old_name = os.path.basename(file)
    print(old_name)
    # Apply the replacement conditions
    # Replace '-' with '_'
    newer_name = old_name.replace('-', '_')
    # Use regex to replace _<digit> with (<digit>)
    new_name = re.sub(r'_(\d)(?!.*_\d)', r' (\1)', newer_name)
    
    print(new_name)
    new_file_path = os.path.join(directory, new_name)
    os.rename(file, new_file_path)


    


