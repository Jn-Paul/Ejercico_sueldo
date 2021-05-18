<br/><br/><br/>
# Solución ejercicio 

## DESCRIPCIÓN DE LA SOLUCIÓN

El programa está estructurado con 3 partes:

1. Ingreso de datos y variables
2. Funciones 
3. Programa principal

Iniciamos el programa leyendo el archivo .txt que incluye los datos de los empleados con el siguiente formato:

```
Nombre=CodigoDiahh:mm-hh:mm,CodigoDiahh:mm-hh:mm,CodigoDiahh:mm-hh:mm
Ejemplo:
Astrid=ASTRID = MO10: 00-12: 00
```
Con esta información procedemos a iterar cada linea de datos del archivo txt.
Es necesario tener la información normalizada para poder realizar una lectura adecuada de la información para lo cual usamos los siguientes métodos.
```
datos[linea]=datos[linea].replace(" ","").upper()
```
Con la información normalizada procedemos a realizar la extracción del nombre de cada empleado, para lo cual se creo la función 
```
Extnombre(datos[linea])
```
Esta función realiza:
1. Busca el símbolo "=" para identificar el nombre.
2. Si no encuentra un nombre retorna "desconocido".
3. Si no se ingreso un nombre o "=" retornara nombre sin formato.
4. Si es un nombre valido retornara el nombre.

Ahora procesamos la demas informacion y de eso se encarga la función proceso 
```
Proceso(datos[linea])
```
Esta función inicialmente separa la información de cada persona teniendo como parámetro separador "," con el fin de poder tener un registro exclusivo del día y las horas laboradas, el cual será leído como un ítem del ciclo for.\
Dentro de la función proceso se realiza:
1. La búsqueda de las horas laboradas
2. Búsqueda de los días trabajados
3. Calculo del sueldo de cada empleado.

Este código posee validaciones con el fin de garantizar un cálculo adecuado del sueldo y poder continuar su ejecución si algún dato es ingresado sin formato. La cuales serán visibles mediante un print con las observaciones debidas.

```
hin,hfin,std=BusquedaH(item)
```
BusquedaH, se encarga de realizar la búsqueda de las horas laboradas, teniendo como parámetro identificador ":" esta función retorna:
1. hin= hora inicial  
2. hfin= hora final
3. std= stado con valores 0 y 1 donde 0 significa que el formato de la hora no es adecuado y 1 que se encontró la hora adecuadamente 

```
BusquedaD(item,semana['laboral'])
```
BusquedaD, se encarga de buscar el día de la semana laborado, esta función retornara 1 si encontró un día valido y 0 si no lo encontró.

```
Pago(paga,hin,hfin,pagos)
```
Finalmente, la función Pago se encarga de calcular el sueldo de los empleados en función del día laborado y las horas trabajadas

## ARQUITECTURA
### Requerimientos
```
Leer un archivo txt que contenga los datos
Determinar el horario de trabajo de cada empleado
Calcular el valor a pagar de cada empleado, considerando el tiempo de trabajo.
```
### Diseño
El código está basado mediante el siguiente diagrama de flujo\
<img  align="center" width="200" height="500"  src="https://raw.githubusercontent.com/Jn-Paul/Ejercico_sueldo/main/Imagen/P_principal.JPG">
\
Extraer nombre
<img  align="center" width="400" height="280" style="float: center;" src="https://raw.githubusercontent.com/Jn-Paul/Ejercico_sueldo/main/Imagen/F_Exnombre.JPG">

\
Procesamiento de Datos
<img  align="center" width="420" height="530" style="float: center;" src="https://raw.githubusercontent.com/Jn-Paul/Ejercico_sueldo/main/Imagen/P_Datos.JPG">

\
Busqueda de Hora
<img  align="center" width="420" height="280" style="float: center;" src="https://raw.githubusercontent.com/Jn-Paul/Ejercico_sueldo/main/Imagen/F_Exhoras.JPG">

\
Busqueda de Día de la semana
<img  align="center" width="380" height="240" style="float: center;" src="https://raw.githubusercontent.com/Jn-Paul/Ejercico_sueldo/main/Imagen/F_Exdia.JPG">

\
Calculo sueldo de empleados
<img  align="center" width="430" height="300" style="float: center;" src="https://raw.githubusercontent.com/Jn-Paul/Ejercico_sueldo/main/Imagen/S_Empleado.JPG">

## ENFOQUE

Mi enfoque para desarrollar el proyecto fue:
Identificar patrones para buscar la información relevante, los elementos que identifique son: "=", ":" y la codificacion de los días.
Lo siguiente es tratar cada función como un estado. en donde si se cumplen las condiciones debidas se podra ir accediendo al sigueinte hasta poder calcular el sueldo de cada empleado. 

## INSTRUCCIONES 
Clonar el proyecto en el ordenador 

1. Tener instalado python la versión 3.x.x
2. Abrir el archivo sueldo.py
3. Ejecutarlo 
4. Observar los resultados en consola
