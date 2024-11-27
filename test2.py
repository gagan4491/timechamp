import os
import time

# List of app names and their focus durations (in seconds)
apps_to_focus = {
    "Notes": 60,
    "Safari": 180,  # 3 minutes
    "Google Chrome": 600,  # 10 minutes
    "PyCharm": 1800,  # 30 minutes
    "BBedit": 600,  # 10 minutes
    "Microsoft Outlook": 180,  # 3 minutes
    "Microsoft Teams": 180,  # 3 minutes
    "Microsoft OneNote": 180,  # 3 minutes
}

def focus_app_in_background(app_name):
    script = f'''
    tell application "{app_name}"
        if it is not running then
            launch
        end if
        activate
    end tell
    '''
    os.system(f"osascript -e '{script}'")
    print(f"Focused on: {app_name}")

# Cycle through the apps
while True:
    for app, duration in apps_to_focus.items():
        focus_app_in_background(app)
        print(f"Focusing on {app} for {duration // 60} minutes ({duration} seconds).")
        time.sleep(duration)  # Stay focused on the app for the specified duration
