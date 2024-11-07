import re
import os

# Example input with alphanumeric text before the IP address
selected_text = "[root@fd-int-nagios (192.168.4.102) ]  cat /usr/local/bin/restartPostfix.sh"

# Regex to capture IP address, path, and command (e.g., cat restartPostfix.sh)
match = re.search(r'\[.*\(([\w\s]*([\d\.]+))\)\s+(.*?)]\s+(.*)', selected_text)

if match:
    # Step 1: Extract the raw IP part which may have alphanumeric text
    raw_captured = match.group(1).strip()  # Captures 'Qp7 10.150.2.19'

    # Step 2: Use regex to clean the alphanumeric text, leaving only the digits (IP address)
    clean_digits = re.sub(r'\b\w*[a-zA-Z]+\w*\b', '', raw_captured).strip()  # Captures '10.150.2.19'
    print("Captured IP Address:", clean_digits)

    # Step 3: Extract the file path (e.g., '/usr/local/bin')
    file_path = match.group(3).strip().replace('~','')
    if file_path:
        print("hekki")
    print("Captured File Path:", file_path)

    # Step 4: Extract the file name (e.g., 'restartPostfix.sh')
    file_name = match.group(4).strip()
    print("Captured File Name:", file_name)

    full_path = file_path+"/"+file_name
    print("Full Path:", full_path)

else:
    print("No match found")
