# electroTAS-U24R

This code handles FT245R chip from "ElectroTAS" board U24R using pylibftdi on linux

The board used is this: http://www.electrotas.com.ar/domotica-automatizacion/usb-4-relay

Dependencies: pylibftdi

## How to get dependencies:

Open terminal console an write:

 ```sudo apt-get install python python-pip```

 ```sudo pip install pylibftdi```
  
  
  see https://pylibftdi.readthedocs.org/en/0.15.0/ for more details.

## Implementation example:

 Move inside folder and type:
 
 ```./usb-rele.py -c RELE3 -s RELE4```
 
 this clears RELE3 and sets RELE4
  
  ```./usb-rele.py -r```
  
 this shows the actual state of relays
 
 ```./usb-rele.py -h```
 
 this promts help menu
 
 
This code was tested over Debian Jessie x64


