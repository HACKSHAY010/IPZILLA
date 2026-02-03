import requests
import socket
import time
print(r"""


__/\\\\\\\\\\\__/\\\\\\\\\\\\\____/\\\\\\\\\\\\\\\__/\\\\\\\\\\\__/\\\______________/\\\_________________/\\\\\\\\\____
 _\/////\\\///__\/\\\/////////\\\_\////////////\\\__\/////\\\///__\/\\\_____________\/\\\_______________/\\\\\\\\\\\\\__
  _____\/\\\_____\/\\\_______\/\\\___________/\\\/_______\/\\\_____\/\\\_____________\/\\\______________/\\\/////////\\\_
   _____\/\\\_____\/\\\\\\\\\\\\\/__________/\\\/_________\/\\\_____\/\\\_____________\/\\\_____________\/\\\_______\/\\\_
    _____\/\\\_____\/\\\/////////__________/\\\/___________\/\\\_____\/\\\_____________\/\\\_____________\/\\\\\\\\\\\\\\\_
     _____\/\\\_____\/\\\_________________/\\\/_____________\/\\\_____\/\\\_____________\/\\\_____________\/\\\/////////\\\_
      _____\/\\\_____\/\\\_______________/\\\/_______________\/\\\_____\/\\\_____________\/\\\_____________\/\\\_______\/\\\_
       __/\\\\\\\\\\\_\/\\\______________/\\\\\\\\\\\\\\\__/\\\\\\\\\\\_\/\\\\\\\\\\\\\\\_\/\\\\\\\\\\\\\\\_\/\\\_______\/\\\_
        _\///////////__\///______________\///////////////__\///////////__\///////////////__\///////////////__\///________\///__
        
        
author shay :)""")

url=input("enter the Domain eg:(example.com) or IP ")
url=url.strip(" ")
url=url.replace("https://","")
url=url.replace("http://","")


def netcheck():
    try:
        requests.get(f"https://ipinfo.io")

    except:
        print("Check your internet connection and try again latter ")
        exit()

netcheck()

def valid_or_not():
    try:
        ip = socket.gethostbyname(url)
        print(ip)
        return ip
    except:
        print(f"{url} is a invalid url/Domain")
        exit()

ip = valid_or_not()

url = f"https://ipinfo.io/{ip}/json"


response = requests.get(url)
data = response.json()

print("Fetching information ")
print("connecting to the the servers ",end="")
for x in range(6):
    print(".",end="")
    time.sleep(0.5)
print("\n--- IP Information ---\n")

print("IP Address   :", data.get("ip"))
print("Hostname     :", data.get("hostname"))
print("City         :", data.get("city"))
print("Region       :", data.get("region"))
print("Country      :", data.get("country"))
print("Location     :", data.get("loc"))
print("Organization :", data.get("org"))
print("Postal Code  :", data.get("postal"))
print("Timezone     :", data.get("timezone"))
print("Anycast      :", data.get("anycast"))

input("PRESS ENTER TO EXIT")