import subprocess

def minimize_all_windows():
    try:
        # Use xdotool to minimize all open windows
        subprocess.run(['xdotool', 'search', '--onlyvisible', '--class', '', 'windowminimize'], check=True)
        print("All windows minimized successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    minimize_all_windows()
