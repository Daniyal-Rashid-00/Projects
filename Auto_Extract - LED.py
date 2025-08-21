# LED Auto-Extract 

import os
import time
import zipfile

# Path to the folder you want to monitor
DOWNLOAD_FOLDER = r"D:\1-Download"
CHECK_INTERVAL = 3  # Seconds between folder scans

def extract_zip(file_path):
    try:
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            extract_path = os.path.dirname(file_path)
            zip_ref.extractall(extract_path)
            print(f"Extracted: {file_path}")
        # Schedule deletion after 60 seconds
        time.sleep(60)
        delete_folder_contents(os.path.dirname(file_path))
    except Exception as e:
        print(f"Failed to extract {file_path}: {e}")

def delete_folder_contents(folder_path):
    try:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                os.remove(file_path)
                print(f"Deleted file: {file_path}")
            for dir in dirs:
                dir_path = os.path.join(root, dir)
                os.rmdir(dir_path)
                print(f"Deleted folder: {dir_path}")
        print(f"All contents deleted in: {folder_path}")
    except Exception as e:
        print(f"Failed to delete contents of {folder_path}: {e}")

def monitor_folder(folder_path):
    processed_files = set()  # Keep track of already-extracted files

    while True:
        try:
            # List all files in the folder
            files = [f for f in os.listdir(folder_path) if f.endswith(".zip")]

            for file_name in files:
                file_path = os.path.join(folder_path, file_name)

                # Check if the file is new
                if file_path not in processed_files:
                    print(f"New zip file detected: {file_path}")
                    extract_zip(file_path)
                    processed_files.add(file_path)  # Mark file as processed

            time.sleep(CHECK_INTERVAL)  # Wait before rescanning the folder
        except Exception as e:
            print(f"Error while monitoring folder: {e}")
            time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    print(f"[Made by Daniyal]\nMonitoring folder: {DOWNLOAD_FOLDER}\n----------------------------------------------------------------------")
    monitor_folder(DOWNLOAD_FOLDER)
