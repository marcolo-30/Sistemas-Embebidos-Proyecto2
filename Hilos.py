#parte serial tomada de https://www.electronicwings.com/raspberry-pi/raspberry-pi-uart-communication-using-python-and-c
#usar python 2.7
import time, serial, queue, threading
import statistics
import I2C
import subprocess #o usar "import punto2_1" para usar código desde python para temperatura

ser = None
RxTx = queue.Queue()
xI2CTx = queue.LifoQueue() 
yI2CTx = queue.LifoQueue()
zI2CTx = queue.LifoQueue()

def TempThread():
    while 1:
        subprocess.call("./tempbash.sh")
	#punto2_1.tempera()
        time.sleep(1)
        
def I2CThread():
    while 1:
        I2C.i2cRTX()
        xI2CTx.put(I2C.xAccl)
        yI2CTx.put(I2C.yAccl)
        zI2CTx.put(I2C.zAccl)

def RxThread():
    while 1:
       x = '#'
       #print('Entro Rx')
       #x = '##PROMEDIO-003-##\n'
       #RxTx.put(x)
       if ser.inWaiting() > 0:
        while ser.inWaiting() > 0:
            #print('Leyendo dato')
            aux = ser.read()
            x = x + aux
        #print('leyo')
        RxTx.put(x)
        print(x)
       else:
            time.sleep(0.2)
        
def TxThread():
    Datos = ['###PROMEDIO','010','##\\n']
    auxN = int(Datos[1])
    
    while 1:
        x, y, z = [],[], []
        #print('Entro Tx')
        if RxTx.empty():
            time.sleep(0.2)
        else:
            #print('Inicio Tx')
            N = RxTx.get()
            Datos = N.split('-')
            #print(str(Datos[0]))
            #print(str(Datos[2]))
        if str(Datos[0]) == '###PROMEDIO' and str(Datos[2]) == ('##' + '\\n'):
            if xI2CTx.empty():
                time.sleep(0.2)
            else:
                if auxN != int(Datos[1]):
                    auxN = int(Datos[1])
                for i in range(auxN):
                    
                    x.append(int(xI2CTx.get()))
                    #print(x[i])
                    y.append(int(yI2CTx.get()))
                    #print(y[i])
                    z.append(int(zI2CTx.get()))
                    #print(z[i])
                 
                PromedioX = statistics.mean(x)
                PromedioY = statistics.mean(y)
                PromedioZ = statistics.mean(z)        
                if ser:
                    Cadena = 'Promedio X =' + str(PromedioX) + 'Promedio Y =' + str(PromedioY) + 'Promedio Z =' + str(PromedioZ)
                    print(Cadena)
                    ser.write(Cadena)
        else:
            print('PROMEDIO INVALIDO')
                    
                
def mainThread(comPortName):
    global ser 
    #print('Entro Main')
    ser = serial.Serial \
            (
              port=comPortName,
              baudrate=115200,
              parity=serial.PARITY_NONE,
              stopbits=serial.STOPBITS_ONE,
              bytesize=serial.EIGHTBITS
            )
    #threading.Thread(target=TempThread).start()
    threading.Thread(target=I2CThread).start()
    threading.Thread(target=RxThread).start()
    threading.Thread(target=TxThread).start()
   
    try:
        while 1:
            time.sleep(1)
    except:
        ser = None

if __name__ == "__main__":
  mainThread("/dev/ttyAMA0")
