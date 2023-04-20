import os
from datetime import datetime
from time import sleep
import sys
import pyautogui as p
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
import time

colorama_init()
os.system("cls")

print(f"{Fore.LIGHTWHITE_EX}most gay friend remover by mask#3333")
print(f"{Fore.LIGHTWHITE_EX}made with pyautogui lol")
print("-------------------------------------------")
friend1 = input(f"[>] {Fore.LIGHTRED_EX}Friend 1 here: ")
friend2 = input(f"[>] {Fore.LIGHTRED_EX}Friend 2 here: ")
friend3 = input(f"[>] {Fore.LIGHTRED_EX}Friend 3 here: ")
friend4 = input(f"[>] {Fore.LIGHTRED_EX}Friend 4 here: ")
friend5 = input(f"[>] {Fore.LIGHTRED_EX}Friend 5 here: ")

def sprint(content: str, status: str = "c") -> None:
    current_time = datetime.now().strftime("%H:%M:%S")
    sys.stdout.write(f"[>] {current_time} : {content}{Fore.RESET}\n")

g = Fore.LIGHTGREEN_EX
c = Fore.CYAN
b = Fore.LIGHTBLUE_EX
lr = Fore.LIGHTRED_EX

os.system("cls")


time.sleep(1)
for i in range(1):
    p.typewrite(f"/")
    sleep(1)
    p.typewrite(f"friend remove {friend1}")
    sleep(0)
    p.press("enter")
    sleep(1)
    sprint(f"[Succeded] Removed {friend1}")
    sleep(2)
    p.typewrite(f"/")
    sleep(1)
    p.typewrite(f"friend remove {friend2}")
    sleep(0)
    p.press("enter")
    sleep(1)
    sprint(f"[Succeded] Removed {friend2}")
    sleep(2)
    p.typewrite(f"/")
    sleep(1)
    p.typewrite(f"friend remove {friend3}")
    sleep(0)
    p.press("enter")
    sleep(1)
    sprint(f"[Succeded] Removed {friend3}")
    sleep(2)
    p.typewrite(f"/")
    sleep(1)
    p.typewrite(f"friend remove {friend4}")
    sleep(0)
    p.press("enter")
    sleep(1)
    sprint(f"[Succeded] Removed {friend4}")
    sleep(2)
    p.typewrite(f"/")
    sleep(1)
    p.typewrite(f"friend remove {friend5}")
    sleep(0)
    p.press("enter")
    sleep(1)
    sprint(f"[Succeded] Removed {friend5}")

os.system("pause")