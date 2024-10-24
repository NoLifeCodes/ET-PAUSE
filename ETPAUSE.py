import psutil
import keyboard
import os
import time
from colorama import init, Fore, Style
import winsound

init(autoreset=True)

def get_etterna_pid():
    for proc in psutil.process_iter(['pid', 'name']):
        if 'Etterna.exe' in proc.info['name']:
            return proc.info['pid']
    return None

def play_ding():
    frequency = 400  
    duration = 300  
    winsound.Beep(frequency, duration)

def toggle_process():
    global paused
    pid = get_etterna_pid()
    if pid is None:
        print("Open Fucking Etterna")
        return
    
    p = psutil.Process(pid)
    
    if paused:
        p.resume()
        paused = False
        play_ding()  # Play sound immediately on unpause
        time.sleep(0.0)
    else:
        p.suspend()
        paused = True
        play_ding()  # Play sound on pause
    
    display_gui()

def clear_terminal():
    os.system('cls')

def display_gui():
    clear_terminal()
    print("-----------------------")
    print(" ")
    print("┏┓┏┳┓ ┏┓┏┓┳┳┏┓┏┓")
    print("┣  ┃━━┃┃┣┫┃┃┗┓┣ ")
    print("┗┛ ┻  ┣┛┛┗┗┛┗┛┗┛")
    print(" ")
    print("---------------------------")
    print("uhh put something here ! ")
    print("-------------------------")
    print(" ")
    print(Style.BRIGHT + "Welcome to the Etterna Pause/Unpause Controller")
    print(Style.BRIGHT + "Made by: " + (Fore.RED + "Nolife"))
    print(" ")
    print("-------------- ")
    print(" ")
    print(Style.BRIGHT + "Press '1' to pause & unpause" + Style.RESET_ALL)
    print(" ")
    print("------------------------ ")
    print(" ")
    print(Style.BRIGHT + "Press '4' to quit")
    print(" ")
    print("-------------- ")
    print(" ")
    print("Paused: " + (Fore.RED + "True" + Style.RESET_ALL if paused else "False"))
    print(" ")
    print("----------------- ")
    print(" ")
    print("Unpaused: " + (Fore.GREEN + "True" + Style.RESET_ALL if not paused else "False"))
    print(" ")
    print("--------------- ")

def quit_application():
    clear_terminal()
    print(" ")
    print("Make sure to reopen when you play lol.")
    print(" ")
    time.sleep(1)
    exit(0)  # Exit the script

def set_cmd_title():
    os.system('title ET - PAUSE')

paused = False
last_pressed = False

def on_key_event(event):
    global last_pressed
    if event.name == '1':
        if not last_pressed:
            toggle_process()
            last_pressed = True
    elif event.name == '4':
        quit_application()

def on_key_release(event):
    global last_pressed
    if event.name == '1':
        last_pressed = False

def main():
    set_cmd_title()
    display_gui()
    
    keyboard.hook(on_key_event)
    keyboard.on_release(on_key_release)
    keyboard.wait()  # Keep the program running until quit_application is called

if __name__ == "__main__":
    main()
