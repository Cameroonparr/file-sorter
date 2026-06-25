import shutil
import os
import json
from pathlib import Path

#####################################################################

def sort_func(script_location, ext_map,files):
    #Iterate thru master_dict, check if extension is valid, determine appropriate folder based on extension, combine into path
    for item in files:
         #List of files found in target directory 
         ext = item.suffix
         if ext in ext_map:
                file_name = item.stem
                file_dir = ext_map[ext]
                print(item)
                path_check = script_location / file_dir

                print("*"*20)
                print(f"file name = {file_name}")
                print(f"file extension = {ext}")
                print(f"file_location is {item}")
                print(f"file_dir is {file_dir}")
                print("*"*20)
                print(f" Path to be checked - {path_check}")
                print("*" * 20)

                #Compare file name to files in target directory, if match is found, print "Already exists", else move file to target directory
                if path_check.exists():
                    print("Path exists")
                    if not os.listdir(path_check):
                        print("Directory is empty, moving file...")
                        shutil.move(item, path_check)
                    else:
                        print("Directory populated.. checking")
                        existing = {f.stem for f in path_check.iterdir()}
                        if file_name not in existing:
                                    shutil.move(item, path_check)
                        else:
                                print(f"{file_name} already exists, skipping")

#####################################################################
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

#####################################################################

def main():

    files = []
    # 1. Setup Path - Wherever script is 
    script_location = Path(__file__).resolve().parent
    print(f"Script location: {script_location}")
    print("*"*20)

    #Setup JSON configuration 
    #With closes json file
    #Load json file contents into a dir
    with open(script_location/'config.json') as f:
        ext_map = json.load(f)["ext_map"]

    #Create directories to sort files into
    for file_type in set(ext_map.values()):
        dir_create(script_location/file_type)

    # 2. SCAN: Use .iterdir() to get Path objects

    for item in script_location.iterdir():
            # Populate file list with path objects
            if item.is_file():
                #Skip script or config.json from being moved
                if  item.name == Path(__file__).name:
                    continue
                if item.name == "config.json":
                    continue 
                files.append(item)
    
    sort_func(script_location, ext_map, files)
     
#####################################################################

if __name__ == "__main__":
     main()


