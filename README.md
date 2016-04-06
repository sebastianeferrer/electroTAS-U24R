# electroTAS-U24R

Este codigo maneja el chip FT245R que utiliza la placa U24R del fabricante "ElectroTas" codeado usando la lib python pylibftdi. [This code handles FT245R chip from "ElectroTAS" board U24R using pylibftdi on linux]

La placa utilizada es 
[The board used is this]:
http://www.electrotas.com.ar/domotica-automatizacion/usb-4-relay

Dependencias [Dependencies]: pylibftdi

## Como obtener dependencias [How to get dependencies]:

Abrir un terminal is escribir [Open terminal console an write]:

 ```sudo apt-get install python python-pip```

 ```sudo pip install pylibftdi```
  
  
  para mas detalles
  [for more details]:
  https://pylibftdi.readthedocs.org/en/0.15.0/ 

## Ejemplo de Implementacion [Implementation example]:

Moverse dentro de la carpeta [Move inside folder]: 
electroTAS-U24R
luego escriba [now write]:
 
 ```./usb-rele.py -c RELE3 -s RELE4```
 esto setea RELE3 y desactiva RELE4
 [this clears RELE3 and sets RELE4]
  
  ```./usb-rele.py -r```
  
 muestra el estado actual de los reles
 [this shows the actual state of relays]
 
 ```./usb-rele.py -h```
 
 para obtener ayuda
 [this promts help menu]
 
El codigo se probo en 
[This code was tested over]:
Debian Jessie x64 


