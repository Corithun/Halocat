# Halocat
![!](halokitty.gif)



  An open-source wifi RSSI monitor and security system
Burning this project through the M5 stack store wouldn't quite work as the defense part of this relies on the Wifi SSID being used as a variable, but to my knowledge the network module doesn't directly support that.
This is a defense system meant to protect against attacks from the Pwnagotchi and such arp spoofing/deauth attacks.
Essentially it takes the RSSI and displays it as a pixel on the M5 stick and refreshes every 6 seconds once all 240 pixels are used up and to update the time.
When the RSSI drops below -98, the alarm system is detected and a decoy wifi network is created in an attempt to confuse deauthentication scripts
You can view a simplified version of the signal on the go using a discord webhook, though the M5 stick cannot support requests, I've inserted a script that displays the current RSSI as an SSID.
The CRC code on the side attempts to turn every one of the SSIDs into an intager, as most people don't set their own SSIDs to a number, and upon finding one which is a number sends a request to a discord webhook.
One thing to note is that the "problematic.pyw" is written for windows.
Be sure to edit the wifi password and ssid in main.py for the M5 stick, also be sure to edit the discord webhook in problematic.pyw

