import os
import shutil
def clear_directory(directory_path):
    if os.path.exists(directory_path):
        for item in os.listdir(directory_path):
            item_path = os.path.join(directory_path, item)
            if os.path.isfile(item_path):
                os.remove(item_path)  # Remove the file
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path) 

def copy_files_recursive(source_dir_path, dest_dir_path):
    # Clear destination directory if it exists
    if os.path.exists(dest_dir_path):
        clear_directory(dest_dir_path)
    else:
        os.mkdir(dest_dir_path)

    # Ensure source path exists before proceeding
    if os.path.exists(source_dir_path):
        for item in os.listdir(source_dir_path):
            item_path = os.path.join(source_dir_path, item)
            dest_item_path = os.path.join(dest_dir_path, item)
            
            if os.path.isfile(item_path):
                shutil.copy(item_path, dest_item_path)  # Copy the file to destination
            elif os.path.isdir(item_path):
                # Create subdirectory in the destination
                os.mkdir(dest_item_path)
                copy_files_recursive(item_path, dest_item_path)  # Recursively copy subdirectory contents