import os
import subprocess

def get_pid_by_name(service_name):
    """Find the process ID based on the service name using `ps`."""
    try:
        # Use `ps` and `grep` to find the PID of the service
        ps_command = f"ps aux | grep '{service_name}' | grep -v grep"
        process_output = subprocess.getoutput(ps_command).strip().splitlines()

        if not process_output:
            print(f"No running process found for service: {service_name}")
            return []

        # Extract the PID from the ps output (the second column is PID in `ps aux`)
        pids = []
        for line in process_output:
            parts = line.split()
            if len(parts) > 1:
                pid = parts[1]
                pids.append(pid)

        return pids
    except Exception as e:
        print(f"Error finding PID: {e}")
        return []

def stop_service(service_name):
    print(f"Stopping all services for: {service_name}\n")

    # Find the PID for the service
    pids = get_pid_by_name(service_name)

    if not pids:
        print(f"No processes found for service: {service_name}")
        return  # If no PIDs are found, exit the function

    for pid in pids:
        print(f"Found PID: {pid}")

        # Stop the service using `launchctl`
        print(f"Stopping service for PID {pid}...")
        try:
            # Use `launchctl` to stop the service
            launchctl_command = f"kill {pid}"
            stop_output = subprocess.getoutput(launchctl_command)
            print(f"Stopped service: {stop_output}\n")

            # Optionally, unload the service (if needed)
            # unload_command = f"launchctl unload {service_name}"
            # unload_output = subprocess.getoutput(unload_command)
            # print(f"Unloaded service: {unload_output}\n")

        except Exception as e:
            print(f"Failed to stop service: {e}")

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

old_filename = "Svcvtt"  # Replace with the current file name
new_filename = "temp"
# Call the function to stop the service

rename_file(old_filename, new_filename)

stop_service(service_name)
