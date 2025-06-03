from pynput import keyboard
from functools import partial
import json

class KeyComboListener:
    def __init__(self, callback):
        """
        Initialize the KeyComboListener.

        :param combo: The key combination to listen for (e.g., ('cmd', 'shift', ',')).
        :param callback: The function to call when the key combination is pressed.
        """
        self.combo = set(k.lower() for k in json.load(open('config/settings.json'))["shortcut"])
        self.callback = callback
        self.current_keys = set()  # Track currently pressed keys

    def on_press(self, key):
        """
        Handle key press events.
        """
        try:
            # Add the key to the current set of pressed keys
            if hasattr(key, 'char') and key.char:
                self.current_keys.add(key.char)
            elif hasattr(key, 'name'):
                self.current_keys.add(key.name)

            # Check if the current keys match the desired combination
            if self.combo.issubset(self.current_keys):
                self.callback()
        except Exception as e:
            print(f"Error in on_press: {e}")

    def on_release(self, key):
        """
        Handle key release events.
        """
        try:
            # Remove the key from the current set of pressed keys
            if hasattr(key, 'char') and key.char:
                self.current_keys.discard(key.char)
            elif hasattr(key, 'name'):
                self.current_keys.discard(key.name)
        except Exception as e:
            print(f"Error in on_release: {e}")

    def start_listening(self):
        """
        Start listening for the specified key combination.
        """
        print(f"Listening for key combination: {self.combo}")
        with keyboard.Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()


# Test usage
if __name__ == "__main__":
    def test_callback(number):
        print(f"Key combination triggered! {number}")

    # Create an instance of KeyComboListener
    listener = KeyComboListener(partial(test_callback, 5))

    # Start listening for the key combination
    listener.start_listening()

