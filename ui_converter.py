import os
import subprocess

def convert_ui_to_py(ui_file, py_file):
    """Converts a .ui file to a .py file using pyuic5."""
    try:
        # Run the pyuic5 command to convert the file
        command = f"pyuic5 -x {ui_file} -o {py_file}"
        subprocess.run(command, shell=True, check=True)
        print(f"Successfully converted {ui_file} to {py_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error converting UI file: {e}")

if __name__ == "__main__":
    # Set the file paths
    ui_file = "UAV_Main.ui"
    py_file = "ui_uav_main.py"
    
    # Convert the UI file to Python
    convert_ui_to_py(ui_file, py_file)
