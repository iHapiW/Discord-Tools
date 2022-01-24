from random import randint

class Proxy:
  def __init__(self):
    with open("config/proxy.list", "r") as f:
      data = f.read().split("\n")
      self.Proxies = []
      for proxy in data:
        if proxy != '':
          self.Proxies.append(proxy)

  def get_proxy(self) -> str:
    last = len(self.Proxies)-1
    if last == -1: return None
    return self.Proxies[ randint(0, last) ]

  def rm_proxy(self, proxy: str) -> None:
    with open("config/proxy.list", "r") as f:
      data = f.read()
      temp = []
      for proxy in data.split("\n"):
        temp.append(proxy)
      temp.remove(proxy)
      self.Proxies = temp
    with open("config/proxy.list", "w") as f:
      f.write("\n".join(temp))
