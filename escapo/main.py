import subprocess
import sys

def check_wmctrl():
    try:
        subprocess.run(['wmctrl', '-m'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError:
        print("wmctrl is not installed. Please install it using your package manager.")
        sys.exit(1)
    except FileNotFoundError:
        print("wmctrl is not found. Please install it using your package manager.")
        sys.exit(1)

def minimize_all_windows():
    check_wmctrl()
    try:
        # Use wmctrl to minimize all open windows
        subprocess.run(['wmctrl', '-k', 'on'], check=True)
        print("All windows minimized successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    minimize_all_windows()
