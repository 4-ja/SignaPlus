import os
from pyshortcuts import make_shortcut

def ensure_settings_exists():
    # 1. Define folder names
    in_folder = 'To_Be_Signed'
    out_folder = 'Signed_Documents'
    filename = 'settings.txt'
    
    # 2. Physically create the folders if they are missing
    for folder in [in_folder, out_folder]:
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"Created directory: {folder}")

    # 3. Create settings.txt with these paths included
    if not os.path.exists(filename):
        default_settings = (
            "[SETTINGS]\n"
            "SignatoryName=John Doe\n"
            "InputPath=To_Be_Signed\n"
            "OutputPath=Signed_Documents\n"
            "SignaturePath=Signature/signature.png\n"
            "AutoRunOnStartup=True\n"
            "ShowNotifications=True\n"
        )
        with open(filename, 'w') as f:
            f.write(default_settings)
            print("Created settings.txt")

def create_desktop_shortcut():
    # We want the shortcut to point to main.py, not this utils file!
    # This finds 'main.py' in the same folder as this script.
    base_dir = os.path.dirname(os.path.abspath(__file__))
    target = os.path.join(base_dir, 'main.py')
    
    if os.path.exists(target):
        make_shortcut(target, name='AutoSignatory', terminal=False)
        print("Desktop shortcut verified/created.")