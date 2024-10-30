import os
import shutil

# Define the path to the source directory
source_dir = r'C:\Users\user\computer-vision-projects\flower-classification\images'

def organize_images(source_dir):
    # Get all PNG files
    for filename in os.listdir(source_dir):
        if filename.endswith('.png'):
            # Get the first two digits of the filename
            folder_name = filename[:2]

            # Create the path for the new directory
            target_dir = os.path.join(source_dir, folder_name)

            # Create the directory if it doesn't exist
            os.makedirs(target_dir, exist_ok=True)

            # Move the file to the appropriate directory
            shutil.move(os.path.join(source_dir, filename), os.path.join(target_dir, filename))

    print("Files have been successfully moved.")

if __name__ == "__main__":
    organize_images(source_dir)
