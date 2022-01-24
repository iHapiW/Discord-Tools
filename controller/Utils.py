from termcolor import colored

def psuccess(text: str):
  print(f"\n[{colored('+','green')}] {text}")

def perror(text: str):
  print(f"\n[{colored('-','red')}] {text}")

def pinput(text: str):
  return input(f"\n[{colored('?','blue')}] {text}")
