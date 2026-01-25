import shutil
from pathlib import Path

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

files = []
directories = []
#Contains just files & extensions, no dirs 
master_dict = {}

#Create folders for orginization

image_dir = script_location / "images"
power_points_dir = script_location / "power_points"
word_docs_dir = script_location / "word_docs"

file_types = [image_dir,power_points_dir,word_docs_dir]

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

print(f"Files found: {[f.name for f in files]}")
print("*"*20)
print(f"Directories found: {directories}")
print("*"*20)

# 3. ACTION - Sort the files in the master directory depending on the extension (value)
#Iterate thru dict by name, check value extension type 

for key, value in master_dict.items():
    if value == ".pptx":
        file_location = script_location / (key+value)
        shutil.move(file_location,power_points_dir )
    if value == ".docx":
        file_location = script_location / (key+value)
        shutil.move(file_location, word_docs_dir)
    if value == ".jfif":
        file_location = script_location / (key+value)
        shutil.move(file_location,image_dir) 
    if value == ".jpg":
        file_location = script_location / (key+value)
        shutil.move(file_location,image_dir) 
    if value == ".png":
        file_location = script_location / (key+value)
        shutil.move(file_location,image_dir)     

