<br/><br/><br/>
# Solución ejercicio 

## DESCRIPCIÓN DE LA SOLUCIÓN

El programa esta estructurado con 3 partes:

1. Ingreso de datos y varaibles
2. Funciones 
3. Programa principal

Iniciamos el programa leyendo el archivo .txt que incluye los datos de los empleados con el sigueinte formato:
```
Nombre=CodigoDiahh:mm-hh:mm,CodigoDiahh:mm-hh:mm,CodigoDiahh:mm-hh:mm
Ejemplo:
Astrid=ASTRID = MO10: 00-12: 00
```
Con esta información procedemos a iterar cada linea de datos del archivo txt.
Es necesario tener la información normalizada para poder realizar una lectura adecuada de la informacion para lo cual usamos los siguientes metodos.
```
datos[linea]=datos[linea].replace(" ","").upper()
```
Con la informacion normalizada procedemos a realizar la extracción del nombre de cada empleado, para lo cual se creo la función 
```
Extnombre(datos[linea])
```
Esta funcion realiza:
1. Busca el simbolo "=" para identifiacar el nombre.
2. Si no encuentra un nombre retorna "desconocido".
3. Si no se ingreso un nombre o "=" retornara nombre sin formato.
4. Si es un nombre valido retornara el nombre.

Ahora procesamos la demas informacion y de eso se encarga la funcion proceso 
```
Proceso(datos[linea])
```
Esta funcion inicialmente separa la informacion de cada persona teniendo como parametro separador "," con el fin de poder tener un registro exclusivo del dia y las horas laboradas, el cual sera leido como un item del ciclo for.\
Dentro de la funcion proceso se realiza:
1. La busqueda de las horas laboradas
2. Busqueda de los días trabajados
3. Calculo del sueldo de cada empleado.

Este codigo posee validaciones con el fin de garantizar un calculo adecuado del sueldo y poder continuar su ejecución si algun dato es ingresado sin formato. La cuales seran visibles mediante un print con las observaciones devidas.

```
hin,hfin,std=BusquedaH(item)
```
BusquedaH, se encarga de realizar la busqueda de las horas laboradas, teniedo como prametro identificador ":" esta funcion retorna:
1. hin= hora inicial  
2. hfin= hora final
3. std= stado con valores 0 y 1 donde 0 significa que el formato de la hora no es adecuado y 1 que se encontro la hora adecaudamente 

```
BusquedaD(item,semana['laboral'])
```
BusquedaD, se encarga de buscar el dia de la semana laborado, esta funcion retornara 1 si encotro un dia valido y 0 si no lo encontro.

```
Pago(paga,hin,hfin,pagos)
```
Finalmente la función Pago se encarga de calcular el sueldo de los empleados en funcion del dia laborado y las horas trabajadas


## ARQUITECTURA
### Requerimientos
```
Leer un archivo txt que contenga los datos
Determinar el horario de trabajo de cada empleado
Calcular el valor a pagar de cada empleado, considerando el tiempo de trabajo.
```
### Diseño
El codigo esta basado mediante el siguiente diagrama de flujo\
<img  align="center" width="300" style="float: center;" src="https://github.com/Jn-Paul/Ejercico_sueldo/blob/main/Imagen/P_principal.jpg">
\
Extraer nombre
<img  align="center" width="400" style="float: center;" src="https://github.com/Jn-Paul/Ejercico_sueldo/blob/main/Imagen/F_Exnombre.jpg">
\
Procesamiento de Datos
<img  align="center" width="400" style="float: center;" src="https://github.com/Jn-Paul/Ejercico_sueldo/blob/main/Imagen/P_Datos.jpg">
\
Busqueda de Hora
<img  align="center" width="400" style="float: center;" src="https://github.com/Jn-Paul/Ejercico_sueldo/blob/main/Imagen/F_Exhoras.jpg">
\
Busqueda de Día de la semana
<img  align="center" width="400" style="float: center;" src="https://github.com/Jn-Paul/Ejercico_sueldo/blob/main/Imagen/F_Exdia.jpg">
\
Calculo sueldo de empleados
<img  align="center" width="400" style="float: center;" src="https://github.com/Jn-Paul/Ejercico_sueldo/blob/main/Imagen/S_Empleado.jpg">


## ENFOQUE

Mi enfoque para desarrollar el proyecto fue:
1. Identificar patrones para buscar la infomracion relevante 
2. Los patrones de diseño en los que me enfoque son: =, :, la codificacion de los dias.
3. 

## INSTRUCCIONES 
Clonar el proyecto en el ordenador 

1. Tener instalado python la versión 3.x.x
2. Abrir el archivo sueldo.py
3. Ejecutarlo 
4. Observar los resultados en consola

