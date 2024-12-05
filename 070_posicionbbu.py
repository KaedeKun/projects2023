import ipaddress
import json
from netaddr import *
import ipaddress
import csv
import sys
from rich.theme import Theme
from rich.console import Console
custom_theme = Theme({'success': 'green', 'error': 'bold red','informational' : 'bold white'})

console = Console(theme=custom_theme)

#---------------------------------------------------------------------------------------
#MUESTRA DE REGIONES CON NUMERACION
# with open('opt/Regiones.csv') as regiones:
#     read_regiones = csv.reader(regiones, delimiter=",")
#     for row in read_regiones:
#         print(row)
#---------------------------------------------------------------------------------------


#---------------------------------------------------------------------------------------
# PROGRAMA PARA APROVISONAR DIRECCIONAMIENTO + CONFIGURACION PARA 1 BBU O RANGO DE BBUS
#
#
#---------------------------------------------------------------------------------------
# SOLICITA LA INFORMACION SOBRE LA CANTIDAD DE BBUS Y DIRECCIONAMIENTO DE O&M PARA RTNs
#---------------------------------------------------------------------------------------
def suma3erocteto(segmento):
        return(segmento+1310720)

def formateoIP(direccion_bbu):
    return((json.dumps(direccion_bbu, indent=4, sort_keys=True, default=int))[1:-3])


num_region = (input('Ingresa la región del Router: '))
num_router  = (input('Ingresa el numero del Router: '))

def validar_router(num_router):
    while True:
            try:
                if num_router.isdigit() == True:
                    pass
                else:
                    print('Numero de Router no valido')
                    exit()
            except  ValueError:
                    print('Error en el ingreso del numero')
                    exit()
            return num_router

def validar_region(num_region):
    while True:
            try:
                if num_region.isdigit() == True:
                    pass
                elif 1 <= num_region <=15:
                    print('Region no valida')
                    break
            except ValueError:
                    print('Error en el ingreso de la region')
                    exit()
            return num_region
    

#RTNOyM_dir = (input('ingresar *Segmento* de red O&M para RTN (default /27): '))


#baseRTNOyM_dir = IPNetwork(RTNOyM_dir+'/27')
if (int(validar_region(num_region)) >0 ) and (int(validar_router(num_router)) >0 ):
    baseBBUDir = IPNetwork('11.'+validar_region(num_region)+'.'+validar_router(num_router)+'.0/24')
else:
     print('digitos no validos')
     sys.exit()

# baseRTNServ_Dir = IPNetwork('10.'+region_router+'.'+num_router+'.0/24')
# #Convierte la entrada a INT antes que nada
cantidad_bbus = (int(input('Ingresa la cantidad de BBUs a configurar: ')))
if cantidad_bbus > 1:
        min, max = input("Ingrese la cantidad de BBUs a configurar, separado por guíon:").split("-")
        print('BBU de inicio :', min)
        print('BBU de final :', max)
else:
        print("la cantidad de BBU es :", cantidad_bbus)

# #---------------------------------------------------------------------------------------
BBU_Cont = 1
baseBBUDir = list(baseBBUDir.subnet(30))[0:cantidad_bbus]
for count, ips in enumerate(baseBBUDir, start=1):
        first_oym = list(ips.subnet(32))[1] #OBTIENE LA PRIMERA IP UTIL DEL SEGMENTO
        first_formated = json.dumps(first_oym, indent=4, sort_keys=True, default=str)[1:-4] #FORMATO SIN CARACTERES EXTRAÑOS
        #console.print(count, ips, style='green')
        #console.print(count,"-",first_oym,"\n", style='bold green')
        OyM_BBU    = ipaddress.ip_address(first_formated)
        IuB_BBU    = suma3erocteto(OyM_BBU) # SUMA IP + 20 del Origen (O&M)
        s1_BBU     = suma3erocteto(IuB_BBU) # SUMA IP + 20 del anterior (s1)
        s1_5g_BBU  = suma3erocteto(s1_BBU) # SUMA IP + 20 del anterior (s1_5G)
        console.print(f'BBU:{count}', style="bold white")
        console.print("- O&M :",OyM_BBU,"\t","- IuB   :",IuB_BBU)
        console.print("- S1  :",s1_BBU,"\t","- S1_5G :",s1_5g_BBU)
        console.print("\n")
        BBU_Cont+=1
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------





































def mostrar_menu(opciones):
    print('Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')

def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a


def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()

def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()

def accion1():
    print('Has elegido la opción 1')

def accion2():
    print('Has elegido la opción 2')

def accion3():
    print('Has elegido la opción 3')

def salir():
    print('Saliendo')

def menu_principal():
    opciones = {
        '1': ('Opción 1', accion1),
        '2': ('Opción 2', accion2),
        '3': ('Opción 3', accion3),
        '4': ('Salir', salir)
    }

    generar_menu(opciones, '4')


#if __name__ == '__main__':
    #menu_principal()
# num_bbu = int(input('ingrese el número de la BBU : '))

# base = IPNetwork(u'11.7.1.0/24')
# barra30 = list(base.subnet(30))

# print(json.dumps(barra30[num_bbu], indent=4, sort_keys=True, default=str))
