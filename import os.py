import os
import shutil

def backup_file():
    # Step 1: Ask the user to specify the full path to the file
    file_path = input("Please enter the full path to the file on the remote computer: ")

    # Step 2: Check if the file exists
    if not os.path.isfile(file_path):
        print("The file does not exist. Please check the path and try again.")
        return

    # Step 3: Create the new file path with a '.old' suffix
    backup_path = file_path + ".old"
    
    try:
        # Step 4: Copy the original file to the backup location
        shutil.copy(file_path, backup_path)
        print(f"Backup successful! File copied to: {backup_path}")
    except Exception as e:
        print(f"An error occurred during the backup: {e}")

if __name__ == "__main__":
    backup_file()
