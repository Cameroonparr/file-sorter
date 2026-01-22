import shutil
from pathlib import Path

# 1. Setup Path
script_location = Path(__file__).resolve().parent
print(f"Script location: {script_location}")
print("*"*20)

files = []
directories = []
#Contains just files & extensions, no dirs 
master_dict = {}

image_dir = script_location / "images"
misc_dir = script_location / "misc"
power_points_dir = script_location / "power_points"
word_docs_dir = script_location / "word_docs"

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
        

