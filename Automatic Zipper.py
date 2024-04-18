import os
import zipfile


def zip_directory(directory_path, zip_path, excluded):

    try:
        os.makedirs(destination_directory, exist_ok=False)
    except FileExistsError:
        print("Directory exists already")

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zip_file:
        for root, _, files in os.walk(directory_path):
            for file in files:
                if file in excluded:
                    pass
                else:
                    file_path = os.path.join(root, file)
                    relative_path = os.path.relpath(file_path, directory_path)
                    zip_file.write(file_path, arcname=relative_path)

        print(f"Finished zipping directory; {directory_path}")


def unzip(files, saving_path):
    count = 0
    for file in files:
        count += 1
        with zipfile.ZipFile(file, "r") as zip_ref:
            zip_ref.extractall(path=saving_path)

    print(f"Finished unzipping {count} files into {saving_path}")


if __name__ == "__main__":

    directory_path = rf"C:\Users\Patrick Van Workum\Pictures\Screenshots\test"
    zip_directory_name = "Test.zip"
    destination_directory = (
        rf"C:\Users\Patrick Van Workum\Pictures\Screenshots\test\Zipped"
    )

    excluded = ["Screenshot 2024-02-14 210842.png"]

    zip_path = os.path.join(destination_directory, zip_directory_name)
    zip_directory(directory_path, zip_path, excluded)

    """
    Implement own zip library??
    expanding zipping to multi directory zipping option
    """
