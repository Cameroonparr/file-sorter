import shutil
from pathlib import Path

#Sort files into folders depending on type
#Improve variable names (key & value)
def sort_func(script_location):
    #Iterate thru master_dict, check if extension is valid, determine appropriate folder based on extension, combine into path
    for key, value in master_dict.items():
         if value in ext_map:
                file_type = value
                file_dir = ext_map[value]
                file_location = script_location/(key + value)
                shutil.move(file_location,file_dir )

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

image_dir = script_location / "pics"
power_points_dir = script_location / "power_points"
word_docs_dir = script_location / "word_docs"
pdf_dir = script_location/"pdf_files"
excel_dir = script_location/"excel_files"

#Points which folders extensions should go to 

ext_map = {
    ".pptx": power_points_dir,
    ".ppt": power_points_dir,
    ".docx": word_docs_dir,
    ".doc": word_docs_dir,
    ".jfif": image_dir,
    ".jpg": image_dir,
    ".png": image_dir,
    ".xls.": excel_dir,
    ".xlsx": excel_dir,
    ".csv": excel_dir,
    ".pdf": pdf_dir,
}

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


