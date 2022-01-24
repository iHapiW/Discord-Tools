from models.Proxy import Proxy
from models.Nitro import Nitro, Generator
from controller.Utils import  perror

def run():
  try:
    global pool

    proxy = Proxy()
    nitro = Nitro()
    pool = []
    for i in range(100):
      thread = Generator(f"Thread {i}", nitro, proxy)
      thread.start()
      pool.append(thread)

  except KeyboardInterrupt as K:
    raise K

  except FileNotFoundError:
    perror("./config/proxy.list Not Found")


