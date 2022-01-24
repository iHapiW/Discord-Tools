#!/bin/python3

import sys
import os
import platform
sys.dont_write_bytecode = True

from termcolor import colored
import colorama

from controller.Utils import pinput, perror
from controller import Nitro_gen

def banner():
  if platform.system() == "Linux":
    os.system("clear")
  elif platform.system() == "Windows":
    os.system("cls")
  elif platform.system() == "Darwin":
    os.system("clear")
  else:
    print("OS Not Detected!")
    
  print("\n")
  print(colored("""       _____  _                       _   _              _     
      |  __ \\(_)                     | | | |            | |    
      | |  | |_ ___  ___ ___  _ __ __| | | |_ ___   ___ | |___ 
      | |  | | / __|/ __/ _ \\| '__/ _` | | __/ _ \\ / _ \\| / __|
      | |__| | \\__ \\ (_| (_) | | | (_| | | || (_) | (_) | \\__ \\
      |_____/|_|___/\\___\\___/|_|  \\__,_|  \\__\\___/ \\___/|_|___/
    ""","blue"))

def main():
  colorama.init()
  banner()
  print(f"\n[{colored('1','green')}] Nitro Generator")
  option = pinput("Enter Option: ")
  
  try:
    option = int(option)
  except ValueError:
    perror("Only Number!")
    sys.exit(1)
  if option == 1:
    Nitro_gen.run()
  else:
    perror("Invalid Option")

if __name__ == "__main__":
  try:
    main()
  except KeyboardInterrupt:
    perror("Exiting App...")
    sys.exit()
