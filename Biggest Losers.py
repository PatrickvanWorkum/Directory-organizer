import os


def get_file_size(file_path):
    """Returns the size of a file in bytes."""
    return os.path.getsize(file_path)


def get_top_largest_files(directory_path, NUM_FILES=5):
    """Returns the top N largest files in a directory."""
    files = []
    for dirpath, _, filenames in os.walk(directory_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            file_size = get_file_size(file_path)
            files.append((file_path, file_size))

    # Sort files by size in descending order
    files.sort(key=lambda x: x[1], reverse=True)

    # Return the top N files
    return files[:NUM_FILES]


# Example usage
directory_path = "DIRECTORY_NAME"  # Specify the directory path
NUM_FILES = 10  # Number of top files to retrieve

top_files = get_top_largest_files(directory_path, NUM_FILES)

print(f"Top {NUM_FILES} Largest Files:")
for file_path, file_size in top_files:
    print(f"{file_path} - {file_size} bytes")
