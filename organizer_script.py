import shutil
import os
import json
from pathlib import Path

#Fix bug converning duplicates
#Implement json or yaml file to rreplace ext_map
#Automate script

def sort_func(script_location):
    #Iterate thru master_dict, check if extension is valid, determine appropriate folder based on extension, combine into path
    for file_name, ext in master_dict.items():
         #List of files found in target directory 
         if ext in ext_map:
                
                file_dir = ext_map[ext]
                file_location = script_location/(file_name + ext)
                print(file_location)
                path_check = Path(file_location/file_dir)

                print("*"*20)
                print(f"file name = {file_name}")
                print(f"file extension = {ext}")
                print(f"file_location is {file_location}")
                print(f"file_dir is {file_dir}")
                print("*"*20)
                print(f" Path to be checked - {path_check}")
                print("*" * 20)

                #Compare file name to files in target directory, if match is found, print "Already exists", else move file to target directory
                if path_check.exists():
                    print("Path exists")
                    if not os.listdir(path_check):
                        print("Directory is empty, moving file...")
                        shutil.move(file_location, path_check)
                    else:
                        print("Directory populated.. checking")
                        for file in path_check.iterdir():
                            print(f"Files found in target dir {file}")
                            if file.stem == file_name:
                                print(f"File {file_name} already exists in target directory")
                            else:
                                shutil.move(file_location, path_check)


#Create directories 
def dir_create(dir_name):
    try:
        dir_name.mkdir()
        print(f"'{dir_name}' created.")
    except FileExistsError:
        print(f"'{dir_name}' already exists.")
    except PermissionError:
        print(f"Permission denied: Unable to create '{dir_name}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# 1. Setup Path - Wherever script is 
script_location = Path(__file__).resolve().parent
print(f"Script location: {script_location}")
print("*"*20)

#Setup JSON configuration 
ext_map = open('config.json')
ext_map = json.load(ext_map)

files = []
directories = []
#Contains just files & extensions, no dirs 
master_dict = {}

#Create folders for orginization

image_dir = script_location / "pics"
power_points_dir = script_location / "power_points"
word_docs_dir = script_location / "word_docs"
pdf_dir = script_location/"pdf_files"
excel_dir = script_location/"excel_files"

file_types = [image_dir,power_points_dir,word_docs_dir,pdf_dir,excel_dir]

#Create directories to sort files into
for file_type in file_types:
    dir_create(file_type)

# 2. SCAN: Use .iterdir() to get Path objects

for item in script_location.iterdir():
    
    # IDENTIFY: Check if it's a file or directory
    if item.is_dir():
        directories.append(item.name)
        continue 
    
    if item.is_file():
        # Skip script from being moved 
        if item.name == Path(__file__).name:
            continue

        files.append(item)
        
        # Populate master_dict: key=filename (no extension), val=extension
        master_dict[item.stem] = item.suffix

#MAIN
sort_func(script_location)


