import os, sys, subprocess
import time

def tempera():
    #Dirección donde se halla el archivo de datos I/O del sensor 1-Wire
    dir = '/sys/bus/w1/devices/w1_bus_master1/28-3c01d075bc1a/driver/28-3c01d075bc1a/temperature'
    #Uso del módulo subprocess, argumentos capture_outpus y text activados
    temptr = subprocess.run(['cat', dir], capture_output=True, text=True)
    #Se a tipo entero y divide por 1000 para hallar la temperatura en grados Celsius
    temptr = int(temptr.stdout)/1000.0

    t = time.localtime() #se crea una instancia usando la librería time
    tiempo = time.strftime("%Y%m%d%H%M%S", t) #se obtiene, año, mes, día, hora, minuto y segundo

    nombre_archivo = str(temptr) + ".csv" #nombre inicial del archivo nuevo
    archivo = open(nombre_archivo, "a") #se escribe archivo nuevo

    try:
        while (True): #se ejecuta el programa hasta que se haga, ctrl c, pasa al except
            #se ejecuta por cada ciclo el codigo de acceso a datos al directorio w1_bus_master1
            temptr = subprocess.run(['cat', dir], capture_output=True, text=True)
            temptr = int(temptr.stdout)/1000.0
            #se sobreescribe/escriben los datos de temperatura de entrada del sensor
            archivo.write(str(temptr)+"°C, "+ time.strftime("%H:%M:%S", time.localtime())+"\n")
            print(temptr)
            time.sleep(10) #cada 10 segundos se ingresan datos
    except:
        archivo.close() 
        nuevo_name = tiempo + "_" + str(temptr) + ".csv"
        #se renombra el archivo de la forma:
        #AñoMesDíaHoraMinutoSegundo_últimaTemperatura
        os.rename(nombre_archivo, nuevo_name) 
        
        print("\nSalió")
