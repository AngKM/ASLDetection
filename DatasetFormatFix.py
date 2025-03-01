import os
import re

def rename_images_in_folders(dataset_path):
    # Iterate through each folder inside the dataset
    for folder in os.listdir(dataset_path):
        folder_path = os.path.join(dataset_path, folder)
        
        # Check if it is a directory and not a hidden/system folder
        if not os.path.isdir(folder_path) or folder.startswith("."):
            continue
        
        # List all files and extract existing numbers
        files = sorted(os.listdir(folder_path))
        existing_numbers = set()
        
        for file in files:
            match = re.match(rf"{folder}_(\d+)(\..+)?", file)
            if match:
                existing_numbers.add(int(match.group(1)))
        
        # Start renaming and filling gaps from 1 first
        next_number = 1
        for file in files:
            old_file_path = os.path.join(folder_path, file)
            
            # Skip directories
            if not os.path.isfile(old_file_path):
                continue
            
            # Ensure file has a .jpeg extension
            new_file_extension = ".jpeg"
            
            # Start from 1 and fill gaps first before continuing
            while next_number in existing_numbers:
                next_number += 1
            
            new_file_name = f"_{folder}_{next_number}{new_file_extension}"
            new_file_path = os.path.join(folder_path, new_file_name)
            
            # Rename the file
            os.rename(old_file_path, new_file_path)
            
            # Add the used number to the set
            existing_numbers.add(next_number)
            print(f"Renamed {file} -> {new_file_name}")
            
            next_number += 1  # Ensure it increments correctly for subsequent files
        
        print(f"Renaming completed for folder: {folder}")

# Define the dataset directory path
dataset_directory = "AlphabetDataset/asl_dataset"  # Update this path if needed
rename_images_in_folders(dataset_directory)

print("Renaming complete!")