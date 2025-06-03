import pyperclip
import time

class ClipboardMonitor:
    def __init__(self):
        self.previous_content = ''
    
    def monitor_clipboard(self, callback):
        """
        Continuously monitor clipboard for changes
        """
        while True:
            try:
                current_content = pyperclip.paste()
                if current_content != self.previous_content:
                    self.previous_content = current_content
                    callback(current_content)
            except Exception as e:
                print(f"Error monitoring clipboard: {e}")
            time.sleep(0.5)  # Check every 0.5 seconds