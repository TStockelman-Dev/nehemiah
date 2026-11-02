import os
import shutil
from pathlib import Path

def clean_directory(destination_path):
    path = Path(destination_path)
    if path.exists():
        for item in path.iterdir():
            if item.is_dir():
                shutil.rmtree(item)
            else:
                item.unlink()

def copy_recursively(source, destination):

    os.makedirs(destination, exist_ok = True)

    for item in os.listdir(source):
        source_path = os.path.join(source, item)
        destination_path = os.path.join(destination, item)

        if os.path.isdir(source_path):
            copy_recursively(source_path, destination_path)
        else:
            shutil.copy(source_path, destination_path)



def content_copy(source, destination):
    
    # Check if the source directory exists
    if not os.path.exists(source):
        raise FileNotFoundError("The source directory does not exist.")

    if not os.path.exists(destination):
        os.mkdir(destination)
    
    # Create the destination directory if it does not exist

    clean_directory(destination)
    copy_recursively(source, destination)
    
    

    
    
    
    
    