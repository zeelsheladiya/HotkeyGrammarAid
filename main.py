import threading
import time

from utils.clipboard_utils import ClipboardMonitor
from utils.keyboard_utils import KeyComboListener
from utils.llm_utils import LLM

MAIN_TEXT = ""

def on_clipboard_change(content):
    """
    Callback function that runs whenever clipboard content changes
    """
    global MAIN_TEXT
    MAIN_TEXT = content
    print(f"New text got coppied!")

def main():
    global MAIN_TEXT

    llm = LLM()

    clipboard_monitor = ClipboardMonitor()
    # Run clipboard monitor in a background thread
    threading.Thread(target=clipboard_monitor.monitor_clipboard, args=(on_clipboard_change,), daemon=True).start()

    # Start keyboard listener in a separate thread
    keyboard_monitor = KeyComboListener(lambda: llm.grammar_service_callback(MAIN_TEXT))
    threading.Thread(target=keyboard_monitor.start_listening, daemon=True).start()

    while True:
        pass

if __name__ == "__main__":
    main()