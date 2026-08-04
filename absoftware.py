import tkinter as tk
import threading
import time
import keyboard

running = False

def spam_keys():
    global running
    while running:
        for key in ["a", "s", "d", "w"]:
            if not running:
                break
            keyboard.press(key)
            time.sleep(0.1)
            keyboard.release(key)

def start():
    global running
    if not running:
        running = True
        threading.Thread(target=spam_keys, daemon=True).start()

def stop():
    global running
    running = False
    for key in ["a", "s", "d", "w"]:
        keyboard.release(key)

root = tk.Tk()
root.title("Key Alternator")
root.geometry("250x120")
root.resizable(False, False)

tk.Button(root, text="Start", command=start, width=20).pack(pady=10)
tk.Button(root, text="Stop", command=stop, width=20).pack()

def on_close():
    stop()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_close)

root.mainloop()