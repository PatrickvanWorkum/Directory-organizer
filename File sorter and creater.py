import os
import shutil


def search_and_copy_files(directory, target_name, custom_name, destination_directory):
    file_counter = 1
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith(".jpg") and filename == target_name:
                directory_name = os.path.basename(root)
                source_path = os.path.join(root, filename)
                new_file_name = f"{custom_name}_{directory_name}.jpg"
                destination_path = os.path.join(destination_directory, new_file_name)
                shutil.copyfile(source_path, destination_path)
                file_counter += 1


# Usage example:
directory_path = "DIRECTORY_NAME"  # Replace with the actual directory path
jpg_name = "NAME.jpg"  # Replace with the target JPG file name
custom_name = "NAME"  # Replace with your desired custom name
destination_directory = (
    "DIRECTORY_NAME"  # Replace with the desired destination directory path
)

search_and_copy_files(directory_path, jpg_name, custom_name, destination_directory)
