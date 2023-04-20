import os
import sys
import time
from time import sleep
import pyautogui as p
from datetime import datetime
from colorama import Fore, init as colorama_init

colorama_init()
os.system("cls")

print(f"{Fore.LIGHTWHITE_EX}most gay friend remover by mask#3333 / pray#6969")
print(f"{Fore.LIGHTWHITE_EX}made with pyautogui lol")
print("-------------------------------------------")


use_manual_input = input(f"{Fore.YELLOW}[?] Do you want to input the names manually? (y/n): {Fore.RESET}").lower() == "y"

if use_manual_input:
    
    while True:
        try:
            num_names = int(input(f"{Fore.YELLOW}[?] How many names do you want to input? (1-5): {Fore.RESET}"))
            if 1 <= num_names <= 5:
                break
            else:
                print(f"{Fore.RED}[ERROR] Invalid number of names. Please enter a number between 1 and 5.{Fore.RESET}")
        except ValueError:
            print(f"{Fore.RED}[ERROR] Invalid input. Please enter a number.{Fore.RESET}")

    
    names = [input(f"[>] {Fore.LIGHTRED_EX}Friend {i+1} here: ") for i in range(num_names)]
else:
    
    try:
        with open("name.txt") as f:
            names = [line.strip() for line in f]
    except FileNotFoundError:
        print(f"{Fore.RED}[ERROR] Could not find name.txt file.{Fore.RESET}")
        sys.exit()

def sprint(content: str, status: str = "c") -> None:
    current_time = datetime.now().strftime("%H:%M:%S")
    sys.stdout.write(f"[>] {current_time} : {content}{Fore.RESET}\n")

g = Fore.LIGHTGREEN_EX
c = Fore.CYAN
b = Fore.LIGHTBLUE_EX
lr = Fore.LIGHTRED_EX

os.system("cls")

time.sleep(1)
for name in names:
    p.typewrite(f"/")
    sleep(1)
    p.typewrite(f"friend remove {name}")
    sleep(0)
    p.press("enter")
    sleep(1)
    sprint(f"{Fore.CYAN}[Succeeded] {Fore.WHITE}Removed {name}")
    sleep(2)

os.system("pause")
