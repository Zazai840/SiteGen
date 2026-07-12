import os
import shutil
def copy_to_destination(source_directory, destination):
    if os.path.exists(destination):
        shutil.rmtree(destination)
        os.mkdir(destination)
    else:
        os.mkdir(destination)

    list_of_contents = os.listdir(source_directory)
    for content in list_of_contents:
        source_path = os.path.join(source_directory, content)
        destination_path = os.path.join(destination, content)
        if os.path.isfile(source_path):
            shutil.copy(source_path, destination_path)
        else:
            copy_to_destination(source_path, destination_path)
            




