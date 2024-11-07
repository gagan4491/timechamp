import os
import subprocess


def rename_file(old_filename, new_filename):
    # Construct the full paths for the old and new file names
    old_file_path = f"/Applications/Svcvtt.app/Contents/MacOS/{old_filename}"
    new_file_path = f"/Applications/Svcvtt.app/Contents/MacOS/{new_filename}"

    # Check if the old file exists
    if not os.path.exists(old_file_path):
        print(f"Error: {old_file_path} does not exist.")
        return

    # Rename the file using sudo and mv command
    try:
        subprocess.run(['sudo', 'mv', old_file_path, new_file_path], check=True)
        print(f"File renamed from {old_filename} to {new_filename}.")
    except subprocess.CalledProcessError as e:
        print(f"Error: Could not rename the file. {e}")



# Replace 'application.com.snovasys.timechamp' with the actual service name you're searching for
service_name = "Svcvtt"

old_filename = "temp"  # Replace with the current file name
new_filename = "Svcvtt"
# Call the function to stop the service

rename_file(old_filename, new_filename)
