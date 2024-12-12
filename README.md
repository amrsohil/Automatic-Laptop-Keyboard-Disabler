# Automatic-Laptop-Keyboard-Disabler

This project is a Python-based tool designed to automatically manage keyboard devices on a Windows laptop. It detects external USB keyboards and dynamically disables or re-enables the internal laptop keyboard based on their connection status

## Problem Solved
I created this solution to address a personal issue. I searched for an easy way to toggle the internal keyboard based on the connection status of external keyboards, but all the methods I found required multiple steps to implement. This tool simplifies the process.


---

## Key Features
1. **Automatic Detection**: Automatically detects external USB keyboards.
2. **Dynamic Management**: Disables internal laptop keyboard when a USB keyboard connects.
3. **Re-enabling**: Re-enables the internal keyboard when the USB keyboard is disconnected.
4. **Background Process**: Runs seamlessly as a background monitoring process.
5. **Admin Privileges**: Requires administrator privileges for device management.

---

## Prerequisites
Before running the script, you'll need to install the following Python packages:

```bash
pip install pywin32 pynput
```

---

## How to Use

1. **Run with Administrator Privileges**:
   Ensure that the script or executable is run as an administrator, as device management commands require elevated privileges.

2. **Background Monitoring**:
   The script will continuously monitor keyboard connections in the background.

3. **Keyboard Management**:
   - When a USB keyboard is connected, the internal keyboard is automatically disabled.
   - When the USB keyboard is disconnected, the internal keyboard is re-enabled.

---

## Important Notes
* **Administrator Rights**: The script must be run with administrator privileges to modify device states.
* **Windows-Specific**: This tool uses Windows-specific commands and APIs to manage devices and will not work on other operating systems.
* **Device Detection**: Works best with typical laptop keyboards detected via PnP (Plug and Play).

---

## Potential Improvements
* Add logging functionality to track device events.
* Implement a system tray icon for better user interaction.
* Enhance device detection for non-standard keyboards.
* Introduce configuration options for user customization.

