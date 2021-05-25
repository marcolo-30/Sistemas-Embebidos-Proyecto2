# Sistemas-Embebidos-Proyecto2
El proyecto dos busca entender el funcionamiento de hilos, utilizandolo sobre lenguaje python para cumplir con los siguientes objetivos: 

1) Capturar los datos de un sensor con comunicaciones i2c (temperatura, humedad, presión IMUS, acelerometros, entre otros) usando un script de python para ello, se debe imprimir en pantalla el valor capturado a una taza de mínimo 1 por segundo.

2) Capturar los datos de su sensor 1 Wire.

3) Usando el módulo threading de python o C (thread.h) implemente un hilo que lea de su sensor i2c a la taza más alta que permita su sensor. Otro hilo que escriba en un puerto serial a mínimo 115200 bps el promedio de las últimas N lecturas donde N puede ser configurado por el usuario con una variable de argumento de entrada serial de su programa en su programa (C o python) y otro hilo que lea del puerto serial a la misma velocidad, una trama así: (“##PROMEDIO-NNN-##\n”) donde NNN es el tamaño de la ventana de promedio, cualquier otro mensaje debe ser descartado y tomado como no válido.



| Lenguaje      | Programa |
| ------------- | ------------- |
| Captura datos I2C | [I2C python](https://github.com/marcolo-30/Sistemas-Embebidos-Proyecto2/blob/main/I2C.py) |
|Captura datos 1 Wire | [1-wire Bash](https://github.com/marcolo-30/Sistemas-Embebidos-Proyecto2/blob/main/onewire.sh) |
| C/C++, libreria BCM |[BCM](https://github.com/) |
| Python | [Python](https://github.com/)  |

