# sudo_escapo🔮🤣

A Python script to minimize all open windows on your Linux system using `wmctrl`.

## Installation

### Prerequisites

1. **Install `wmctrl`**:

   For Debian-based systems (e.g., Ubuntu), use:
   ```bash
   sudo apt-get install wmctrl
   ```

   For Red Hat-based systems (e.g., Fedora), use:
   ```bash
   sudo dnf install wmctrl
   ```

   For Arch-based systems, use:
   ```bash
   sudo pacman -S wmctrl
   ```

   For other systems, please refer to your package manager's documentation.

### Install the `sudo_escapo` Package

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/alybali/sudo-escapo.git
   cd sudo-escapo
   ```

2. **Install the Python Package**:
   ```bash
   pip install .
   ```

## Usage

### Minimize All Windows

Run the command to minimize all open windows:
```bash
escapo
```

### Minimize All Windows with `sudo`

Run the command with `sudo` to minimize all open windows:
```bash
sudo_escapo
```

## Troubleshooting

### `wmctrl` Not Found

If you see an error indicating that `wmctrl` is not found, make sure it is installed correctly on your system as per the installation instructions above.

## Development

### Directory Structure

```
sudo_escapo/
├── escapo
│   ├── __init__.py
│   └── main.py
├── README.md
└── setup.py
```

### Update the Package

To update the package with any changes, uninstall the previous version and reinstall it:

```bash
pip uninstall sudo_escapo
pip install .
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

Created by Swiss. [GitHub Profile](https://github.com/alybali)
