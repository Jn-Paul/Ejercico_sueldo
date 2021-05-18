#lectura del archivo
archivo=open("DatosP.txt", "rt")
datos=archivo.readlines()
archivo.close()

#variabes
n=len(datos) #longitud del archivo
semana={'laboral':['MO','TU','WE','TH','FR'],'fin':['SA','SU'],'sl':[25,15,20],'sf':[30,20,25]}


#Funciones 
def Extnombre(lst):
    if lst.find('=') != -1:
        lst=lst[0:lst.find('=')]
        if len(lst) >=1 and lst.isnumeric()!=True:
            return lst
        else:
            return 'desconocido'
    else:
        return '(nombre fuera de formato o sin nombre)'

def BusquedaD(item,lst):
    for dia in lst:
        pos=item.find(dia)
        aux=0
        if pos >-1:
            dia=item[pos:pos+2]
            aux=1               #identifica que encontro un dia semana
            break
    return aux
        
def BusquedaH(item):
    fnd=item.find(':')
    if fnd != -1:
        inicial=item[fnd-2:fnd]
        fnd=item.find(':',fnd+1)
        if fnd != -1 and inicial.isnumeric()==True:
            final=item[fnd-2:fnd]
            return int(inicial), int(final),1
        else:
            return 0,0,0
    else:
        return 0,0,0

def Pago(paga,hin,hfin,pagos):
    casos=[0<=hin<=9, 0<=hfin<=9, 9<=hin<=18, 9<=hfin<=18, 18<=hin<=23, 18<=hfin<=23]
    if casos[0] and casos[1]:
        paga+=pagos[0]*(hfin-hin)
    elif casos[2] and casos[3]:
        paga+=pagos[1]*(hfin-hin)
    elif casos[4] and casos[5]:
        paga+=pagos[2]*(hfin-hin)
    return paga

def Proceso(lst):
    lst=lst.split(",")
    sueldo=0
    print('Observaciones: ')
    for item in lst:
        hin,hfin,std=BusquedaH(item)
        if std==1 and 0<=hin<=23 and 0<=hfin<=23:
            if BusquedaD(item,semana['laboral']) ==1:
                sueldo=Pago(sueldo,hin,hfin,semana['sl'])
            elif BusquedaD(item,semana['fin']) ==1:
                sueldo=Pago(sueldo,hin,hfin,semana['sf'])
            else:
                print('     Elemento: '+ item, 'sin formato de dia')
        else:
            print('     Elemento: '+ item,' presenta errores el formato de hora')
    return sueldo
     
#Programa Principal
for linea in range(0,n):
    datos[linea]=datos[linea].replace(" ","").upper()
    nombre=Extnombre(datos[linea])
    #print(nombre)
    #Proceso(datos[linea])
    print("Aporte:\n", datos[linea])
    print("Produccion: \nEl monto a pagar "+ nombre ,"es: ",Proceso(datos[linea]), "USD\n" )
