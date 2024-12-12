import win32com.client
import win32gui
import win32con
import pythoncom
import time
import sys
import subprocess
from pynput import keyboard
import threading

class KeyboardDisabler:
    def __init__(self):
        self.external_keyboard_connected = False
        self.internal_keyboard_disabled = False
        self.listener = None

    def get_active_keyboard_devices(self):
        """Get list of connected keyboard devices."""
        try:
            # Use WMI to query keyboard devices
            wmi = win32com.client.GetObject("winmgmts:")
            keyboards = wmi.ExecQuery("SELECT * FROM Win32_Keyboard")
            return [kb.DeviceID for kb in keyboards]
        except Exception as e:
            print(f"Error detecting keyboards: {e}")
            return []

    def disable_internal_keyboard(self):
        """Disable the internal laptop keyboard."""
        try:
            # Use Windows Device Manager command to disable keyboard
            devices = self.get_active_keyboard_devices()
            for device in devices:
                if 'PNP' in device:  # Typical for internal laptop keyboards
                    disable_cmd = f'pnputil /disable-device "{device}"'
                    subprocess.run(disable_cmd, shell=True, capture_output=True)
            
            print("Internal keyboard disabled.")
            self.internal_keyboard_disabled = True
        except Exception as e:
            print(f"Could not disable keyboard: {e}")

    def enable_internal_keyboard(self):
        """Re-enable the internal laptop keyboard."""
        try:
            devices = self.get_active_keyboard_devices()
            for device in devices:
                if 'PNP' in device:
                    enable_cmd = f'pnputil /enable-device "{device}"'
                    subprocess.run(enable_cmd, shell=True, capture_output=True)
            
            print("Internal keyboard re-enabled.")
            self.internal_keyboard_disabled = False
        except Exception as e:
            print(f"Could not enable keyboard: {e}")

    def monitor_keyboard_connection(self):
        """Continuously monitor keyboard connections."""
        while True:
            try:
                devices = self.get_active_keyboard_devices()
                
                # Check if external keyboard is connected
                external_keyboards = [dev for dev in devices if 'USB' in dev]
                
                if external_keyboards and not self.internal_keyboard_disabled:
                    self.disable_internal_keyboard()
                elif not external_keyboards and self.internal_keyboard_disabled:
                    self.enable_internal_keyboard()
                
                time.sleep(2)  # Check every 2 seconds
            except Exception as e:
                print(f"Monitoring error: {e}")
                time.sleep(5)

    def run(self):
        """Start the keyboard monitoring thread."""
        print("🔌 Laptop Keyboard Disabler Started")
        print("Monitoring keyboard connections...")
        
        # Create and start monitoring thread
        monitor_thread = threading.Thread(target=self.monitor_keyboard_connection, daemon=True)
        monitor_thread.start()

        # Keep main thread running
        try:
            monitor_thread.join()
        except KeyboardInterrupt:
            print("\nStopping keyboard monitor...")

def main():
    # Check for admin rights
    try:
        is_admin = subprocess.run(['net', 'session'], capture_output=True, text=True).returncode == 0
        if not is_admin:
            print("❌ This script requires administrator privileges. Please run as admin.")
            input("Press Enter to exit...")
            sys.exit(1)

        disabler = KeyboardDisabler()
        disabler.run()

    except Exception as e:
        print(f"Unexpected error: {e}")
        input("Press Enter to exit...")

if __name__ == "__main__":
    main()
