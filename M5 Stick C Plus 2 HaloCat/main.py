import os, sys, io
import M5
from M5 import *
import time
import network
wlan = None
text = None
new = None
i = None
index = None
rssi = None
current_pass = None
passkey = None
minutes = None
# Describe this function...
def replicatewifi():
  global text, new, i, index, rssi, current_pass, passkey, minutes, wlan
  displaybattery()
  for i in range(240):
    wlan = network.WLAN(network.AP_IF)
    wlan.active(True)
    wlan.config(essid=current_pass)
    M5.Lcd.drawPixel(i, 110, 0xcc33cc)
    M5.Lcd.drawPixel(i, 111, 0xcc33cc)
    M5.Lcd.drawPixel(i, 112, 0xcc33cc)
    time.sleep(0.00625)
  M5.Lcd.clear(0x000000)
  displaybattery()
  gatchi('Attack detected (owo)')
  time.sleep(120)
  wifi_diagnostic()
# Describe this function...
def splashscreen():
  global text, new, i, index, rssi, current_pass, passkey, minutes, wlan
  new = 0
  M5.Lcd.clear(0x000000)
  M5.Lcd.drawImage("/flash/res/img/halocat1.png", 50, 0, 0, 0, 0, 0, 5, 5)
  M5.Lcd.setCursor(60, 120)
  M5.Lcd.setTextSize(1.7)
  M5.Lcd.print('HaloCat beta', 0xcc33cc)
  time.sleep(2.6)
  new = 1
# Describe this function...
def wifi_diagnostic():
  global text, new, i, index, rssi, current_pass, passkey, minutes, wlan
  M5.Lcd.clear(0x000000)
  displaybattery()
  for index in range(240):
    rssi = (int(wlan.status('rssi'))) * -1
    M5.Lcd.drawPixel(index, rssi, 0x993399)
    if rssi > 98:
      for count in range(2):
        M5.Lcd.drawImage("/flash/res/img/alarm.png", 0, 0)
        Speaker.setVolumePercentage(1)
        Speaker.playWavFile('/flash/res/audio/alarm+(1).wav')
      replicatewifi()
    time.sleep(0.025)
  M5.Lcd.clear(0x000000)
  index = 0
# Pwnagatchi type text display
def gatchi(text):
  global new, i, index, rssi, current_pass, passkey, minutes, wlan
  M5.Lcd.setFont(Widgets.FONTS.ASCII7)
  M5.Lcd.setTextSize(1.8)
  M5.Lcd.setCursor(15, 60)
  M5.Lcd.print(text, 0x993399)
# Describe this function...
def displaybattery():
  global text, new, i, index, rssi, current_pass, passkey, minutes, wlan
  M5.Lcd.setFont(Widgets.FONTS.ASCII7)
  M5.Lcd.setTextSize(1)
  M5.Lcd.setCursor(220, 5)
  M5.Lcd.print(str((Power.getBatteryLevel())), 0xcc33cc)
  M5.Lcd.setCursor(0, 5)
  minutes = str(((time.localtime())[4]))
  if len(minutes) == 1:
    minutes = (str('0') + str(minutes))
  M5.Lcd.print(str(((str(((time.localtime())[3])) + str(((str(':') + str(minutes))))))), 0xcc33cc)
def setup():
  global wlan, new, rssi, current_pass, index, text, passkey, minutes, i
  M5.begin()
  Widgets.setRotation(3)
  Widgets.fillScreen(0x000000)
  time.timezone('GMT-7')
  M5.Lcd.setRotation(3)
  current_pass = 'YOUR_WIFI_SSID'
  passkey = 'YOUR_WIFI_PASSWORD'
  rssi = 0
  wlan = network.WLAN(network.STA_IF)
  wlan.active(True)
  wlan.connect(current_pass, passkey)
  splashscreen()
def loop():
  global wlan, new, rssi, current_pass, index, text, passkey, minutes, i
  M5.update()
  while new == 1:
    wifi_diagnostic()
if __name__ == '__main__':
  try:
    setup()
    while True:
      loop()
  except (Exception, KeyboardInterrupt) as e:
    try:
      from utility import print_error_msg
      print_error_msg(e)
    except ImportError:
      print("please update to latest firmware")
