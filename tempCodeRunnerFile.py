import os

def rename_images_in_folders(dataset_path):
    # Iterate through each folder inside the dataset
    for folder in os.listdir(dataset_path):
        folder_path = os.path.join(dataset_path, folder)
        
        # Check if it is a directory and not a hidden/system folder
        if not os.path.isdir(folder_path) or folder.startswith("."):
            continue
        
        # List all files and sort them to maintain order
        files = sorted(os.listdir(folder_path))
        
        # Rename files
        for index, file in enumerate(files, start=1):
            old_file_path = os.path.join(folder_path, file)
            file_extension = os.path.splitext(file)[1]  # Preserve original extension
            new_file_name = f"{folder}_{index}{file_extension}"
            new_file_path = os.path.join(folder_path, new_file_name)
            
            # Rename the file
            os.rename(old_file_path, new_file_path)
            
        print(f"Renamed files in folder: {folder}")

# Define the dataset directory path
dataset_directory = "asl_dataset"  # Update this path if needed
rename_images_in_folders(dataset_directory)

print("Renaming complete!")