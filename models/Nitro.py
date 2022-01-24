import ctypes
import threading
from random import randint
from string import ascii_letters, digits

import requests
from requests import exceptions

from controller.Utils import perror, psuccess
from models.Proxy import Proxy

class Nitro:
  def __init__(self):
    self.chars = ascii_letters + digits

  def generate(self):
    code = ""
    for i in range(19):
      rand = randint(0, len(self.chars) - 1)
      code += self.chars[rand]
    return code

  def check_code(self, code: str, proxy: str) -> bool:
    proxies = {
        "https": f"http://{proxy}"
        }

    res = requests.get(
        f"https://discordapp.com/api/v6/entitlements/gift-codes/{code}",
        proxies=proxies
        )

    if res.status_code == 200: return True
    return False

class Generator(threading.Thread):

  def __init__(self, name, nitro: Nitro, proxy: Proxy):
    threading.Thread.__init__(self)
    self.name = name
    self.nitro = nitro
    self.proxy = proxy
           
  def run(self):
    while True:
      code = self.nitro.generate()
      proxy_addr = self.proxy.get_proxy()
      if proxy_addr == None:
        perror("No Proxy")
        return self.raise_exception()
      proxy_addr = str(proxy_addr)

      try:

        res = self.nitro.check_code(code, proxy_addr)
        if res:
          psuccess(f"Valid : {code}")
          with open("Found!.txt", "a+") as f:
            f.write(f"{code}\n")
        else:
          perror(f"Not Valid: {code}")

      except exceptions.ConnectTimeout:
        pass
      except exceptions.ProxyError:
        pass
      except exceptions.SSLError:
        pass
      except exceptions.ConnectionError:
        pass
      except Exception as e:
        perror(f"UnHandled Exception Occured: {e}")

  def get_id(self):
    if hasattr(self, '_thread_id'):
      return self._thread_id
    for id, thread in threading._active.items():
      if thread is self:
        return id

  def raise_exception(self):
      thread_id = self.get_id()
      res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id,
            ctypes.py_object(SystemExit))
      if res > 1:
        ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)
        perror('Exception raise failure')
