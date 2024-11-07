import subprocess
import re


def get_pid_from_name(process_name):
    """
    Retrieves the PID of a process by its name using the `ps` command.
    """
    try:
        ps_command = f"ps aux | grep {process_name} | grep -v grep"
        process_output = subprocess.getoutput(ps_command)

        if process_output:
            # Extract the PID (second column of `ps aux` output)
            pid = re.findall(r'\b\d+\b', process_output)[0]  # Finds the first numeric value (PID)
            print(f"Process '{process_name}' found with PID: {pid}\n")
            return pid
        else:
            print(f"No process found with the name '{process_name}'.")
            return None
    except Exception as e:
        print(f"Error finding PID for process '{process_name}': {e}")
        return None


def get_service_info(pid):
    print(f"Gathering information for PID: {pid}\n")

    # 1. Get process details using `ps`
    try:
        print("1. Process Details (ps aux):")
        ps_command = f"ps aux | grep {pid} | grep -v grep"
        process_output = subprocess.getoutput(ps_command)
        if process_output:
            print(process_output + "\n")
        else:
            print(f"No process found for PID: {pid}\n")
    except Exception as e:
        print(f"Error fetching process details: {e}\n")

    # 2. List open files related to the service using `lsof`
    try:
        print("2. Open Files (lsof):")
        lsof_command = f"lsof -p {pid}"
        lsof_output = subprocess.getoutput(lsof_command)
        if lsof_output:
            print(lsof_output + "\n")
        else:
            print(f"No open files found for PID: {pid}\n")
    except Exception as e:
        print(f"Error fetching open files: {e}\n")

    # 3. Check for network connections using `lsof -i`
    try:
        print("3. Network Connections (lsof -i):")
        lsof_network_command = f"lsof -i | grep {pid}"
        lsof_network_output = subprocess.getoutput(lsof_network_command)
        if lsof_network_output:
            print(lsof_network_output + "\n")
        else:
            print(f"No network connections found for PID: {pid}\n")
    except Exception as e:
        print(f"Error fetching network connections: {e}\n")

    # 4. Check launchctl list for the service
    try:
        print("4. Service Information (launchctl list):")
        launchctl_command = f"launchctl list | grep {pid}"
        launchctl_output = subprocess.getoutput(launchctl_command)
        if launchctl_output:
            print(launchctl_output + "\n")
        else:
            print(f"No service information found for PID: {pid}\n")
    except Exception as e:
        print(f"Error fetching service information: {e}\n")


# Replace 'timechamp' with the actual service name you're searching for
process_name = "Svcvtt"

# Get the PID from the process name
pid = get_pid_from_name(process_name)

# If PID is found, gather information using that PID
if pid:
    get_service_info(pid)
