import requests
import json
import math
import subprocess
import re

webhook_url = "https://discord.com/api/webhooks/YOUR_WEBHOOK_LINK"
background_char = ":black_medium_square:"
display_char = ":small_red_triangle_down:"
def displayrssi(rssi):
  rssi = math.floor(rssi/9)
  content = ""
  for i in range(rssi-1):
    content += background_char
  content += display_char
  for p in range(15-rssi):
    content += background_char
  data = {
      "content": content,
      "username": "RSSI",
  }

  headers = {
      "Content-Type": "application/json"
  }

  response = requests.post(webhook_url, data=json.dumps(data), headers=headers)

def get_wifi_names():
    networks = []
    try:
        output = subprocess.check_output(["netsh", "wlan", "show", "networks"], encoding="utf-8")
        ssids = re.findall(r"SSID \d+ : (.+)", output)
        networks = list(set(ssids))
    except subprocess.CalledProcessError as e:
        print("Error:", e)
    return networks

wifilist = get_wifi_names()
num = 0
for network in wifilist:
  try:
    num = int(network)
  except:
    pass



while True:
  displayrssi(num)


