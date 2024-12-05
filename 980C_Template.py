import json
from netaddr import IPNetwork
import pandas as pd
import ipaddress
import csv
import re
from colorama import Fore,Style
from jinja2 import Template

def suma3erocteto(segmento):
        return(segmento+1310720)

def formateoIP(direccion_bbu):
    return((json.dumps(direccion_bbu, indent=4, sort_keys=True, default=int))[1:-3])

print(Fore.LIGHTBLUE_EX+'TEMPLATE HUAWEI 980C - MODELO MOVIL')
print(Style.RESET_ALL)

while True:
    region_router = (input(Fore.LIGHTGREEN_EX+'Ingresa la región del Router: '+Style.RESET_ALL))
    if re.match(r"^\d+$", region_router):
            numero = int(region_router)
            if 1 <= numero <= 15:
                break
            else:
                print(Fore.RED+"ingrese región válida")
                continue
    else:
        print(Fore.RED+"Ingrese valor numerico valido")
        continue

while True:
    num_router  = (input(Fore.LIGHTGREEN_EX+'Ingresa el numero del Router: '+Style.RESET_ALL))
    if re.match(r"^\d+$", num_router):
        break
    else:
        print(Fore.RED+"Ingresa valores numéricos")
        continue

nombre_router = (input(Fore.LIGHTGREEN_EX+'Ingresa el nombre del Router: '+Style.RESET_ALL))
print(Style.RESET_ALL)
baseBBUDir = IPNetwork('11.'+region_router+'.'+num_router+'.0/24')

while True:
    try:
        RTNOyM_Dir = (input('ingresar *Segmento* de red O&M para RTN (default /27): '))
        inter_rev = IPNetwork(RTNOyM_Dir+'/27')
        baseRTNOym_Dir = IPNetwork(inter_rev)
        #baseRTNOym_Dir = ipaddress.IPv4Network(RTNOyM_Dir+"/"+'27')
        #baseRTNOym_Dir = IPNetwork(validarIPNET)
        break
    except ValueError:
        print('Ingrese rango IP Valido')
        continue

print(Fore.LIGHTBLUE_EX+'vlan 101-129\t= IF-SERVICE-NEW-ALL27')
print(Fore.LIGHTBLUE_EX+'vlan 101-125\t= IF-SERVICE-LAST28', end ="")
print(Style.RESET_ALL)

while True:
    rango_vlans = (input('Ingresa Rango de Vlans para RTNs, por defecto el rango es 101-129 :'))
    if rango_vlans == '102-129':
        break
    elif rango_vlans == '101-125':
        break
    elif rango_vlans == "":
        break
    else:
        print(Fore.RED+"Ingresa valores válidos")
        continue

baseBBUDir = IPNetwork('11.'+region_router+'.'+num_router+'.0/24')
#baseRTNOym_Dir = IPNetwork(RTNOyM_Dir+'/27')
baseRTNServ_Dir = IPNetwork('10.'+region_router+'.'+num_router+'.0/24')

#--------------------------------------------------------------------------------------------
# SEGMENTACION Direccionamiento BBUs 980C ( O&M + Servicios )
BBUContador = 1
baseBBUDir = list(baseBBUDir.subnet(30))[0:8]
with open('opt/980_direcciones_raw_bbu.txt','w+',encoding='utf-8') as final_dirbbu:
    for ips in baseBBUDir:
        barra30bbu = list(ips.subnet(32))[1] #OBTIENE LA PRIMERA IP UTIL DEL SEGMENTO
        final_final = json.dumps(barra30bbu, indent=4, sort_keys=True, default=str)[1:-4] #FORMATO SIN CARACTERES EXTRAÑOS
        final_dirbbu.write(final_final+'\n') # GRABA LA  PRIMERA IP UTIL DE CADA SEGMENTO (8 PRIMEROS SEGMENTOS)
    BBUContador+=1
#--------------------------------------------------------------------------------------------
#Lectura de  lineas del archivo de IPs
#-----------------------------------------------------------------------------
e = open('opt/980_direcciones_raw_bbu.txt', 'r')
lines = e.readlines()
# # #-----------------------------------------------------------------------------
BBU1 = lines[0]
OyM_BBU1    = formateoIP(BBU1)
IuB_BBU1    = suma3erocteto(ipaddress.ip_address(OyM_BBU1))# SUMA IP + 20 (Iu_B)
s1_BBU1     = suma3erocteto(IuB_BBU1) # SUMA IP + 20 del anterior (s1)
s1_5g_BBU1  = suma3erocteto(s1_BBU1) # SUMA IP + 20 del anterior (s1_5G)
# #-----------------------------------------------------------------------------
BBU2 = lines[1]
OyM_BBU2    = formateoIP(BBU2)
IuB_BBU2    = suma3erocteto(ipaddress.ip_address(OyM_BBU2)) #SUMA IP + 20 (O&M)
s1_BBU2     = suma3erocteto(IuB_BBU2) #SUMA IP + 20 del anterior (Iu_B)
s1_5g_BBU2  = suma3erocteto(s1_BBU2)# SUMA IP + 20 del anterior (s1)
#-----------------------------------------------------------------------------
BBU3 = lines[2]
OyM_BBU3    = formateoIP(BBU3)
IuB_BBU3    = suma3erocteto(ipaddress.ip_address(OyM_BBU3)) #SUMA IP + 20 (O&M)
s1_BBU3     = suma3erocteto(IuB_BBU3) #SUMA IP + 20 del anterior (Iu_B)
s1_5g_BBU3  = suma3erocteto(s1_BBU3)# SUMA IP + 20 del anterior (s1)
#-----------------------------------------------------------------------------
BBU4 = lines[3]
OyM_BBU4    = formateoIP(BBU4)
IuB_BBU4    = suma3erocteto(ipaddress.ip_address(OyM_BBU4)) #SUMA IP + 20 (O&M)
s1_BBU4     = suma3erocteto(IuB_BBU4) #SUMA IP + 20 del anterior (Iu_B)
s1_5g_BBU4  = suma3erocteto(s1_BBU4)# SUMA IP + 20 del anterior (s1)
#-----------------------------------------------------------------------------
BBU5 = lines[4]
OyM_BBU5    = formateoIP(BBU5)
IuB_BBU5    = suma3erocteto(ipaddress.ip_address(OyM_BBU5)) #SUMA IP + 20 (O&M)
s1_BBU5     = suma3erocteto(IuB_BBU5) #SUMA IP + 20 del anterior (Iu_B)
s1_5g_BBU5  = suma3erocteto(s1_BBU5)# SUMA IP + 20 del anterior (s1)
#-----------------------------------------------------------------------------
BBU6 = lines[5]
OyM_BBU6    = formateoIP(BBU6)
IuB_BBU6    = suma3erocteto(ipaddress.ip_address(OyM_BBU6)) #SUMA IP + 20 (O&M)
s1_BBU6     = suma3erocteto(IuB_BBU6) #SUMA IP + 20 del anterior (Iu_B)
s1_5g_BBU6  = suma3erocteto(s1_BBU6)# SUMA IP + 20 del anterior (s1)
#-----------------------------------------------------------------------------
BBU7 = lines[6]
OyM_BBU7    = formateoIP(BBU7)
IuB_BBU7    = suma3erocteto(ipaddress.ip_address(OyM_BBU7)) #SUMA IP + 20 (O&M)
s1_BBU7     = suma3erocteto(IuB_BBU7) #SUMA IP + 20 del anterior (Iu_B)
s1_5g_BBU7  = suma3erocteto(s1_BBU7)# SUMA IP + 20 del anterior (s1)
#-----------------------------------------------------------------------------
BBU8 = lines[7]
OyM_BBU8    = formateoIP(BBU8)
IuB_BBU8    = suma3erocteto(ipaddress.ip_address(OyM_BBU8)) #SUMA IP + 20 (O&M)
s1_BBU8     = suma3erocteto(IuB_BBU8) #SUMA IP + 20 del anterior (Iu_B)
s1_5g_BBU8  = suma3erocteto(s1_BBU8)# SUMA IP + 20 del anterior (s1)
e.close()

with pd.ExcelWriter('opt/980_Excel_BaseDatos_BBUs_Eth.xlsx', mode='a', engine='openpyxl', if_sheet_exists='overlay') as writer:
        pd.DataFrame([OyM_BBU1]).to_excel     (writer, sheet_name='Excel_BaseDatos_BBUs', startcol=4, startrow=2, index=False, header=False)
        pd.DataFrame([IuB_BBU1]).to_excel     (writer, sheet_name='Excel_BaseDatos_BBUs', startcol=4, startrow=3, index=False, header=False)
        pd.DataFrame([s1_BBU1]).to_excel      (writer, sheet_name='Excel_BaseDatos_BBUs', startcol=4, startrow=4, index=False, header=False)
        pd.DataFrame([s1_5g_BBU1]).to_excel   (writer, sheet_name='Excel_BaseDatos_BBUs', startcol=4, startrow=5, index=False, header=False)
    # #--------------------------------------------------------------------------------------------------------------------------
        pd.DataFrame([OyM_BBU2]).to_excel     (writer, sheet_name='Excel_BaseDatos_BBUs', startcol=4, startrow=7, index=False, header=False)
        pd.DataFrame([IuB_BBU2]).to_excel     (writer, sheet_name='Excel_BaseDatos_BBUs', startcol=4, startrow=8, index=False, header=False)
        pd.DataFrame([s1_BBU2]).to_excel      (writer, sheet_name='Excel_BaseDatos_BBUs', startcol=4, startrow=9, index=False, header=False)
        pd.DataFrame([s1_5g_BBU2]).to_excel   (writer, sheet_name='Excel_BaseDatos_BBUs', startcol=4, startrow=10, index=False, header=False)
    #--------------------------------------------------------------------------------------------------------------------------
        pd.DataFrame([OyM_BBU3]).to_excel     (writer, sheet_name='Excel_BaseDatos_BBUs', startcol=4, startrow=12, index=False, header=False)
        pd.DataFrame([IuB_BBU3]).to_excel     (writer, sheet_name='Excel_BaseDatos_BBUs', startcol=4, startrow=13, index=False, header=False)
        pd.DataFrame([s1_BBU3]).to_excel      (writer, sheet_name='Excel_BaseDatos_BBUs', startcol=4, startrow=14, index=False, header=False)
        pd.DataFrame([s1_5g_BBU3]).to_excel   (writer, sheet_name='Excel_BaseDatos_BBUs', startcol=4, startrow=15, index=False, header=False)
    #--------------------------------------------------------------------------------------------------------------------------
        pd.DataFrame([OyM_BBU4]).to_excel     (writer, sheet_name='Excel_BaseDatos_BBUs', startcol=4, startrow=17, index=False, header=False)
        pd.DataFrame([IuB_BBU4]).to_excel     (writer, sheet_name='Excel_BaseDatos_BBUs', startcol=4, startrow=18, index=False, header=False)
        pd.DataFrame([s1_BBU4]).to_excel      (writer, sheet_name='Excel_BaseDatos_BBUs', startcol=4, startrow=19, index=False, header=False)
        pd.DataFrame([s1_5g_BBU4]).to_excel   (writer, sheet_name='Excel_BaseDatos_BBUs', startcol=4, startrow=20, index=False, header=False)
    #--------------------------------------------------------------------------------------------------------------------------
        pd.DataFrame([OyM_BBU5]).to_excel     (writer, sheet_name='Excel_BaseDatos_BBUs', startcol=4, startrow=22, index=False, header=False)
        pd.DataFrame([IuB_BBU5]).to_excel     (writer, sheet_name='Excel_BaseDatos_BBUs', startcol=4, startrow=23, index=False, header=False)
        pd.DataFrame([s1_BBU5]).to_excel      (writer, sheet_name='Excel_BaseDatos_BBUs', startcol=4, startrow=24, index=False, header=False)
        pd.DataFrame([s1_5g_BBU5]).to_excel   (writer, sheet_name='Excel_BaseDatos_BBUs', startcol=4, startrow=25, index=False, header=False)
    #--------------------------------------------------------------------------------------------------------------------------
        pd.DataFrame([OyM_BBU6]).to_excel     (writer, sheet_name='Excel_BaseDatos_BBUs', startcol=4, startrow=27, index=False, header=False)
        pd.DataFrame([IuB_BBU6]).to_excel     (writer, sheet_name='Excel_BaseDatos_BBUs', startcol=4, startrow=28, index=False, header=False)
        pd.DataFrame([s1_BBU6]).to_excel      (writer, sheet_name='Excel_BaseDatos_BBUs', startcol=4, startrow=29, index=False, header=False)
        pd.DataFrame([s1_5g_BBU6]).to_excel   (writer, sheet_name='Excel_BaseDatos_BBUs', startcol=4, startrow=30, index=False, header=False)
    #--------------------------------------------------------------------------------------------------------------------------
        pd.DataFrame([OyM_BBU7]).to_excel     (writer, sheet_name='Excel_BaseDatos_BBUs', startcol=4, startrow=32, index=False, header=False)
        pd.DataFrame([IuB_BBU7]).to_excel     (writer, sheet_name='Excel_BaseDatos_BBUs', startcol=4, startrow=33, index=False, header=False)
        pd.DataFrame([s1_BBU7]).to_excel      (writer, sheet_name='Excel_BaseDatos_BBUs', startcol=4, startrow=34, index=False, header=False)
        pd.DataFrame([s1_5g_BBU7]).to_excel   (writer, sheet_name='Excel_BaseDatos_BBUs', startcol=4, startrow=35, index=False, header=False)
    #--------------------------------------------------------------------------------------------------------------------------
        pd.DataFrame([OyM_BBU8]).to_excel     (writer, sheet_name='Excel_BaseDatos_BBUs', startcol=4, startrow=37, index=False, header=False)
        pd.DataFrame([IuB_BBU8]).to_excel     (writer, sheet_name='Excel_BaseDatos_BBUs', startcol=4, startrow=38, index=False, header=False)
        pd.DataFrame([s1_BBU8]).to_excel      (writer, sheet_name='Excel_BaseDatos_BBUs', startcol=4, startrow=39, index=False, header=False)
        pd.DataFrame([s1_5g_BBU8]).to_excel   (writer, sheet_name='Excel_BaseDatos_BBUs', startcol=4, startrow=40, index=False, header=False)

#------------------------------------------------------------------------------
# #TRANSFORMACION DE ARCHIVO EXCEL A CSV  para ser manipulado por jinja2
mostrar = pd.DataFrame(pd.read_excel('opt/980_Excel_BaseDatos_BBUs_Eth.xlsx'))
mostrar.to_csv('opt/980_BD_BBUs_eth.csv', index=None, header=True, decimal='')
tranformacion_excel = pd.DataFrame(pd.read_csv('opt/980_BD_BBUs_eth.csv'))

source_file = 'opt/980_BD_BBUs_eth.csv'
BBU_Template_file ='templates/final_template_jinja_interfaces_910_bbu_eth_csv.j2'

with open (BBU_Template_file) as f:
        BBU_Template_file = Template(f.read(), keep_trailing_newline=True)

interface_configs = ""

with open(source_file) as s:
    reader = csv.DictReader(s)
    for row in reader:
        interface_config  = BBU_Template_file.render(
            name = row['name'],
            vlan = row['vlan'][:-1],
            description = row['description'],
            vpn_instance = row['vpn_instance'],
            ip_address = row['ip_address'],
            troncal = row['troncal'], 
        )
        interface_configs+= interface_config

with open(f'980C_BBU_CONFIG_FINAL_{nombre_router}.txt','w') as lectura:
        lectura_final = lectura.write(interface_configs)

print(Fore.GREEN+Style.BRIGHT,f"CONFIGURACION PARA {nombre_router} BBU OK", end="")
print(Style.RESET_ALL)
#--------------------------------------------------------------------------------------------------------
##-----------------------------------------------------------------------------------
## SECCION RTNS
##-----------------------------------------------------------------------------------
# SEGMENTACION Direccionamiento RTN ( Solo O&M )
RTNOyMContador = 1
baseRTNOym_Dir = list(baseRTNOym_Dir.subnet(30))[0:8]
with open('opt/980_direcciones_raw_RTNOyM.txt','w+',encoding='utf-8') as dir_rtn_oym:
    for rtndir in baseRTNOym_Dir:
        barra30RTN = list(rtndir.subnet(32))[1] #OBTIENE LA PRIMERA IP UTIL DEL SEGMENTO RTN O&M
        Final_RTNOyM = json.dumps(barra30RTN, indent=4, sort_keys=True, default=str)[1:-4]#FORMATO SIN CARACTERES EXTRAÑOS
        dir_rtn_oym.write(Final_RTNOyM+'\n')# GRABA LA  PRIMERA IP UTIL DE CADA SEGMENTO (8 PRIMEROS SEGMENTOS)
    RTNOyMContador+=1
#--------------------------------------------------------------------------------------------
#Lectura de  lineas del archivo de IPs RTNs ( O&M )
#-----------------------------------------------------------------------------
lect_rtnOyM = open('opt/980_direcciones_raw_RTNOyM.txt', 'r')
lines = lect_rtnOyM.readlines()
# # #-----------------------------------------------------------------------------
RTN01_OyM   = formateoIP(lines[0])
RTN02_OyM   = formateoIP(lines[1])
RTN03_OyM   = formateoIP(lines[2])
RTN04_OyM   = formateoIP(lines[3])
RTN05_OyM   = formateoIP(lines[4])
RTN06_OyM   = formateoIP(lines[5])
RTN07_OyM   = formateoIP(lines[6])
RTN08_OyM   = formateoIP(lines[7])
lect_rtnOyM.close()
#--------------------------------------------------------------------------------------------
# SEGMENTACION Direccionamiento RTN ( Solo Servicios )
RTNServContador = 1
baseRTNServ_Dir = list(baseRTNServ_Dir.subnet(27))[0:8]
with open('opt/980_direcciones_raw_RTNServ.txt','w+',encoding='utf-8') as dir_rtn_serv:
    for rtndirserv in baseRTNServ_Dir:
        barra30rtnserv = list(rtndirserv.subnet(32))[1] #OBTIENE LA PRIMERA IP UTIL DEL SEGMENTO
        final_rtnserv = json.dumps(barra30rtnserv, indent=4, sort_keys=True, default=str)[1:-4] #FORMATO SIN CARACTERES EXTRAÑOS
        dir_rtn_serv.write(final_rtnserv+'\n') # GRABA LA  PRIMERA IP UTIL DE CADA SEGMENTO (8 PRIMEROS SEGMENTOS)
    RTNServContador+=1
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------
#Lectura de  lineas del archivo de IPs RTNs ( SERVICIOS )
#-----------------------------------------------------------------------------
lect_rtnServ = open('opt/980_direcciones_raw_RTNServ.txt', 'r')
lines = lect_rtnServ.readlines()
# # #-----------------------------------------------------------------------------
RTN01_Serv  = lines[0]
RTN01_OyM1  = formateoIP(RTN01_Serv)
RTN01_IuB   = suma3erocteto(ipaddress.ip_address(RTN01_OyM1))# SUMA IP + 20 (Iu_B)
RTN01_s1    = suma3erocteto(RTN01_IuB) # SUMA IP + 20 del anterior (s1)
RTN01_s1_5g     = suma3erocteto(RTN01_s1) # SUMA IP + 20 del anterior (s1_5G)
# #-----------------------------------------------------------------------------
RTN02_Serv  = lines[1]
RTN02_OyM1  = formateoIP(RTN02_Serv)
RTN02_IuB   = suma3erocteto(ipaddress.ip_address(RTN02_OyM1)) #SUMA IP + 20 (O&M)
RTN02_s1    = suma3erocteto(RTN02_IuB) #SUMA IP + 20 del anterior (Iu_B)
RTN02_s1_5g = suma3erocteto(RTN02_s1)# SUMA IP + 20 del anterior (s1)
# #-----------------------------------------------------------------------------
RTN03_Serv = lines[2]
RTN03_OyM1    = formateoIP(RTN03_Serv)
RTN03_IuB    = suma3erocteto(ipaddress.ip_address(RTN03_OyM1)) #SUMA IP + 20 (O&M)
RTN03_s1     = suma3erocteto(RTN03_IuB) #SUMA IP + 20 del anterior (Iu_B)
RTN03_s1_5g  = suma3erocteto(RTN03_s1)# SUMA IP + 20 del anterior (s1)
# #-----------------------------------------------------------------------------
RTN04_Serv = lines[3]
RTN04_OyM1    = formateoIP(RTN04_Serv)
RTN04_IuB     = suma3erocteto(ipaddress.ip_address(RTN04_OyM1)) #SUMA IP + 20 (O&M)
RTN04_s1     = suma3erocteto(RTN04_IuB) #SUMA IP + 20 del anterior (Iu_B)
RTN04_s1_5g  = suma3erocteto(RTN04_s1)# SUMA IP + 20 del anterior (s1)
# #-----------------------------------------------------------------------------
RTN05_Serv = lines[4]
RTN05_OyM1   = formateoIP(RTN05_Serv)
RTN05_IuB    = suma3erocteto(ipaddress.ip_address(RTN05_OyM1)) #SUMA IP + 20 (O&M)
RTN05_s1     = suma3erocteto(RTN05_IuB) #SUMA IP + 20 del anterior (Iu_B)
RTN05_s1_5g  = suma3erocteto(RTN05_s1)# SUMA IP + 20 del anterior (s1)
# #-----------------------------------------------------------------------------
RTN06_Serv = lines[5]
RTN06_OyM1    = formateoIP(RTN06_Serv)
RTN06_IuB    = suma3erocteto(ipaddress.ip_address(RTN06_OyM1)) #SUMA IP + 20 (O&M)
RTN06_s1     = suma3erocteto(RTN06_IuB) #SUMA IP + 20 del anterior (Iu_B)
RTN06_s1_5g  = suma3erocteto(RTN06_s1)# SUMA IP + 20 del anterior (s1)
# #-----------------------------------------------------------------------------
RTN07_Serv = lines[6]
RTN07_OyM1    = formateoIP(RTN07_Serv)
RTN07_IuB   = suma3erocteto(ipaddress.ip_address(RTN07_OyM1)) #SUMA IP + 20 (O&M)
RTN07_s1     = suma3erocteto(RTN07_IuB) #SUMA IP + 20 del anterior (Iu_B)
RTN07_s1_5g  = suma3erocteto(RTN07_s1)# SUMA IP + 20 del anterior (s1)
# #-----------------------------------------------------------------------------
RTN08_Serv = lines[7]
RTN08_OyM1    = formateoIP(RTN08_Serv)
RTN08_IuB    = suma3erocteto(ipaddress.ip_address(RTN08_OyM1)) #SUMA IP + 20 (O&M)
RTN08_s1     = suma3erocteto(RTN08_IuB) #SUMA IP + 20 del anterior (Iu_B)
RTN08_s1_5g  = suma3erocteto(RTN08_s1)# SUMA IP + 20 del anterior (s1)
lect_rtnServ.close()
#-----------------------------------------------------------------------------
##INSERTAR IPs EN ARCHIVO EXCEL (Template jinja2)
# #--------------------------------------------------------------------------------------------------------------------------
if rango_vlans == '101-129' or rango_vlans == '':
        with pd.ExcelWriter('opt/980_Excel_BaseDatos_RTNs_IF_SERVICE_NEW_ALL27.xlsx', mode='a', engine='openpyxl', if_sheet_exists='overlay') as writer:
            pd.DataFrame([RTN01_OyM]).to_excel      (writer, sheet_name='Excel_BaseDatos_RTN', startcol=4, startrow=2, index=False, header=False)
            pd.DataFrame([RTN01_OyM1]).to_excel     (writer, sheet_name='Excel_BaseDatos_RTN', startcol=4, startrow=3, index=False, header=False)
            pd.DataFrame([RTN01_IuB]).to_excel      (writer, sheet_name='Excel_BaseDatos_RTN', startcol=4, startrow=4, index=False, header=False)
            pd.DataFrame([RTN01_s1]).to_excel       (writer, sheet_name='Excel_BaseDatos_RTN', startcol=4, startrow=5, index=False, header=False)
            pd.DataFrame([RTN01_s1_5g]).to_excel    (writer, sheet_name='Excel_BaseDatos_RTN', startcol=4, startrow=6, index=False, header=False)
        # # #--------------------------------------------------------------------------------------------------------------------------
            pd.DataFrame([RTN02_OyM]).to_excel      (writer, sheet_name='Excel_BaseDatos_RTN', startcol=4, startrow=8, index=False, header=False)
            pd.DataFrame([RTN02_OyM1]).to_excel     (writer, sheet_name='Excel_BaseDatos_RTN', startcol=4, startrow=9, index=False, header=False)
            pd.DataFrame([RTN02_IuB]).to_excel      (writer, sheet_name='Excel_BaseDatos_RTN', startcol=4, startrow=10, index=False, header=False)
            pd.DataFrame([RTN02_s1]).to_excel       (writer, sheet_name='Excel_BaseDatos_RTN', startcol=4, startrow=11, index=False, header=False)
            pd.DataFrame([RTN02_s1_5g]).to_excel    (writer, sheet_name='Excel_BaseDatos_RTN', startcol=4, startrow=12, index=False, header=False)
        # #--------------------------------------------------------------------------------------------------------------------------
            pd.DataFrame([RTN03_OyM]).to_excel      (writer, sheet_name='Excel_BaseDatos_RTN', startcol=4, startrow=14, index=False, header=False)
            pd.DataFrame([RTN03_OyM1]).to_excel     (writer, sheet_name='Excel_BaseDatos_RTN', startcol=4, startrow=15, index=False, header=False)
            pd.DataFrame([RTN03_IuB]).to_excel      (writer, sheet_name='Excel_BaseDatos_RTN', startcol=4, startrow=16, index=False, header=False)
            pd.DataFrame([RTN03_s1]).to_excel       (writer, sheet_name='Excel_BaseDatos_RTN', startcol=4, startrow=17, index=False, header=False)
            pd.DataFrame([RTN03_s1_5g]).to_excel    (writer, sheet_name='Excel_BaseDatos_RTN', startcol=4, startrow=18, index=False, header=False)
        # #--------------------------------------------------------------------------------------------------------------------------
            pd.DataFrame([RTN04_OyM]).to_excel      (writer, sheet_name='Excel_BaseDatos_RTN', startcol=4, startrow=20, index=False, header=False)
            pd.DataFrame([RTN04_OyM1]).to_excel     (writer, sheet_name='Excel_BaseDatos_RTN', startcol=4, startrow=21, index=False, header=False)
            pd.DataFrame([RTN04_IuB]).to_excel      (writer, sheet_name='Excel_BaseDatos_RTN', startcol=4, startrow=22, index=False, header=False)
            pd.DataFrame([RTN04_s1]).to_excel       (writer, sheet_name='Excel_BaseDatos_RTN', startcol=4, startrow=23, index=False, header=False)
            pd.DataFrame([RTN04_s1_5g]).to_excel    (writer, sheet_name='Excel_BaseDatos_RTN', startcol=4, startrow=24, index=False, header=False)
        # #--------------------------------------------------------------------------------------------------------------------------
            pd.DataFrame([RTN05_OyM]).to_excel      (writer, sheet_name='Excel_BaseDatos_RTN', startcol=4, startrow=26, index=False, header=False)
            pd.DataFrame([RTN05_OyM1]).to_excel     (writer, sheet_name='Excel_BaseDatos_RTN', startcol=4, startrow=27, index=False, header=False)
            pd.DataFrame([RTN05_IuB]).to_excel      (writer, sheet_name='Excel_BaseDatos_RTN', startcol=4, startrow=28, index=False, header=False)
            pd.DataFrame([RTN05_s1]).to_excel       (writer, sheet_name='Excel_BaseDatos_RTN', startcol=4, startrow=29, index=False, header=False)
            pd.DataFrame([RTN05_s1_5g]).to_excel    (writer, sheet_name='Excel_BaseDatos_RTN', startcol=4, startrow=30, index=False, header=False)
        # #--------------------------------------------------------------------------------------------------------------------------
            pd.DataFrame([RTN06_OyM]).to_excel      (writer, sheet_name='Excel_BaseDatos_RTN', startcol=4, startrow=32, index=False, header=False)
            pd.DataFrame([RTN06_OyM1]).to_excel     (writer, sheet_name='Excel_BaseDatos_RTN', startcol=4, startrow=33, index=False, header=False)
            pd.DataFrame([RTN06_IuB]).to_excel      (writer, sheet_name='Excel_BaseDatos_RTN', startcol=4, startrow=34, index=False, header=False)
            pd.DataFrame([RTN06_s1]).to_excel       (writer, sheet_name='Excel_BaseDatos_RTN', startcol=4, startrow=35, index=False, header=False)
            pd.DataFrame([RTN06_s1_5g]).to_excel    (writer, sheet_name='Excel_BaseDatos_RTN', startcol=4, startrow=36, index=False, header=False)
        # #--------------------------------------------------------------------------------------------------------------------------
            pd.DataFrame([RTN07_OyM]).to_excel      (writer, sheet_name='Excel_BaseDatos_RTN', startcol=4, startrow=38, index=False, header=False)
            pd.DataFrame([RTN07_OyM1]).to_excel     (writer, sheet_name='Excel_BaseDatos_RTN', startcol=4, startrow=39, index=False, header=False)
            pd.DataFrame([RTN07_IuB]).to_excel      (writer, sheet_name='Excel_BaseDatos_RTN', startcol=4, startrow=40, index=False, header=False)
            pd.DataFrame([RTN07_s1]).to_excel       (writer, sheet_name='Excel_BaseDatos_RTN', startcol=4, startrow=41, index=False, header=False)
            pd.DataFrame([RTN07_s1_5g]).to_excel    (writer, sheet_name='Excel_BaseDatos_RTN', startcol=4, startrow=42, index=False, header=False)
        # #--------------------------------------------------------------------------------------------------------------------------
            pd.DataFrame([RTN08_OyM]).to_excel      (writer, sheet_name='Excel_BaseDatos_RTN', startcol=4, startrow=44, index=False, header=False)
            pd.DataFrame([RTN08_OyM1]).to_excel     (writer, sheet_name='Excel_BaseDatos_RTN', startcol=4, startrow=45, index=False, header=False)
            pd.DataFrame([RTN08_IuB]).to_excel      (writer, sheet_name='Excel_BaseDatos_RTN', startcol=4, startrow=46, index=False, header=False)
            pd.DataFrame([RTN08_s1]).to_excel       (writer, sheet_name='Excel_BaseDatos_RTN', startcol=4, startrow=47, index=False, header=False)
            pd.DataFrame([RTN08_s1_5g]).to_excel    (writer, sheet_name='Excel_BaseDatos_RTN', startcol=4, startrow=48, index=False, header=False)

        mostrarRTN = pd.DataFrame(pd.read_excel('opt/980_Excel_BaseDatos_RTNs_IF_SERVICE_NEW_ALL27.xlsx'))
        mostrarRTN.to_csv('opt/980_BD_RTNs.csv', index=None, header=True)
        tranformacion_excel_RTN = pd.DataFrame(pd.read_csv('opt/980_BD_RTNs.csv'))
else:
        with pd.ExcelWriter('opt/980_Excel_BaseDatos_RTNs_IF_SERVICE_LAST28.xlsx', mode='a', engine='openpyxl', if_sheet_exists='overlay') as writer:
            pd.DataFrame([RTN01_OyM]).to_excel      (writer, sheet_name='Excel_BaseDatos_RTN', startcol=4, startrow=2, index=False, header=False)
            pd.DataFrame([RTN01_OyM1]).to_excel     (writer, sheet_name='Excel_BaseDatos_RTN', startcol=4, startrow=3, index=False, header=False)
            pd.DataFrame([RTN01_IuB]).to_excel      (writer, sheet_name='Excel_BaseDatos_RTN', startcol=4, startrow=4, index=False, header=False)
            pd.DataFrame([RTN01_s1]).to_excel       (writer, sheet_name='Excel_BaseDatos_RTN', startcol=4, startrow=5, index=False, header=False)
            pd.DataFrame([RTN01_s1_5g]).to_excel    (writer, sheet_name='Excel_BaseDatos_RTN', startcol=4, startrow=6, index=False, header=False)
        # # #--------------------------------------------------------------------------------------------------------------------------
            pd.DataFrame([RTN02_OyM]).to_excel      (writer, sheet_name='Excel_BaseDatos_RTN', startcol=4, startrow=8, index=False, header=False)
            pd.DataFrame([RTN02_OyM1]).to_excel     (writer, sheet_name='Excel_BaseDatos_RTN', startcol=4, startrow=9, index=False, header=False)
            pd.DataFrame([RTN02_IuB]).to_excel      (writer, sheet_name='Excel_BaseDatos_RTN', startcol=4, startrow=10, index=False, header=False)
            pd.DataFrame([RTN02_s1]).to_excel       (writer, sheet_name='Excel_BaseDatos_RTN', startcol=4, startrow=11, index=False, header=False)
            pd.DataFrame([RTN02_s1_5g]).to_excel    (writer, sheet_name='Excel_BaseDatos_RTN', startcol=4, startrow=12, index=False, header=False)
        # #--------------------------------------------------------------------------------------------------------------------------
            pd.DataFrame([RTN03_OyM]).to_excel      (writer, sheet_name='Excel_BaseDatos_RTN', startcol=4, startrow=14, index=False, header=False)
            pd.DataFrame([RTN03_OyM1]).to_excel     (writer, sheet_name='Excel_BaseDatos_RTN', startcol=4, startrow=15, index=False, header=False)
            pd.DataFrame([RTN03_IuB]).to_excel      (writer, sheet_name='Excel_BaseDatos_RTN', startcol=4, startrow=16, index=False, header=False)
            pd.DataFrame([RTN03_s1]).to_excel       (writer, sheet_name='Excel_BaseDatos_RTN', startcol=4, startrow=17, index=False, header=False)
            pd.DataFrame([RTN03_s1_5g]).to_excel    (writer, sheet_name='Excel_BaseDatos_RTN', startcol=4, startrow=18, index=False, header=False)
        # #--------------------------------------------------------------------------------------------------------------------------
            pd.DataFrame([RTN04_OyM]).to_excel      (writer, sheet_name='Excel_BaseDatos_RTN', startcol=4, startrow=20, index=False, header=False)
            pd.DataFrame([RTN04_OyM1]).to_excel     (writer, sheet_name='Excel_BaseDatos_RTN', startcol=4, startrow=21, index=False, header=False)
            pd.DataFrame([RTN04_IuB]).to_excel      (writer, sheet_name='Excel_BaseDatos_RTN', startcol=4, startrow=22, index=False, header=False)
            pd.DataFrame([RTN04_s1]).to_excel       (writer, sheet_name='Excel_BaseDatos_RTN', startcol=4, startrow=23, index=False, header=False)
            pd.DataFrame([RTN04_s1_5g]).to_excel    (writer, sheet_name='Excel_BaseDatos_RTN', startcol=4, startrow=24, index=False, header=False)
        # #--------------------------------------------------------------------------------------------------------------------------
            pd.DataFrame([RTN05_OyM]).to_excel      (writer, sheet_name='Excel_BaseDatos_RTN', startcol=4, startrow=26, index=False, header=False)
            pd.DataFrame([RTN05_OyM1]).to_excel     (writer, sheet_name='Excel_BaseDatos_RTN', startcol=4, startrow=27, index=False, header=False)
            pd.DataFrame([RTN05_IuB]).to_excel      (writer, sheet_name='Excel_BaseDatos_RTN', startcol=4, startrow=28, index=False, header=False)
            pd.DataFrame([RTN05_s1]).to_excel       (writer, sheet_name='Excel_BaseDatos_RTN', startcol=4, startrow=29, index=False, header=False)
            pd.DataFrame([RTN05_s1_5g]).to_excel    (writer, sheet_name='Excel_BaseDatos_RTN', startcol=4, startrow=30, index=False, header=False)
        # #--------------------------------------------------------------------------------------------------------------------------
            pd.DataFrame([RTN06_OyM]).to_excel      (writer, sheet_name='Excel_BaseDatos_RTN', startcol=4, startrow=32, index=False, header=False)
            pd.DataFrame([RTN06_OyM1]).to_excel     (writer, sheet_name='Excel_BaseDatos_RTN', startcol=4, startrow=33, index=False, header=False)
            pd.DataFrame([RTN06_IuB]).to_excel      (writer, sheet_name='Excel_BaseDatos_RTN', startcol=4, startrow=34, index=False, header=False)
            pd.DataFrame([RTN06_s1]).to_excel       (writer, sheet_name='Excel_BaseDatos_RTN', startcol=4, startrow=35, index=False, header=False)
            pd.DataFrame([RTN06_s1_5g]).to_excel    (writer, sheet_name='Excel_BaseDatos_RTN', startcol=4, startrow=36, index=False, header=False)
        # #--------------------------------------------------------------------------------------------------------------------------
            pd.DataFrame([RTN07_OyM]).to_excel      (writer, sheet_name='Excel_BaseDatos_RTN', startcol=4, startrow=38, index=False, header=False)
            pd.DataFrame([RTN07_OyM1]).to_excel     (writer, sheet_name='Excel_BaseDatos_RTN', startcol=4, startrow=39, index=False, header=False)
            pd.DataFrame([RTN07_IuB]).to_excel      (writer, sheet_name='Excel_BaseDatos_RTN', startcol=4, startrow=40, index=False, header=False)
            pd.DataFrame([RTN07_s1]).to_excel       (writer, sheet_name='Excel_BaseDatos_RTN', startcol=4, startrow=41, index=False, header=False)
            pd.DataFrame([RTN07_s1_5g]).to_excel    (writer, sheet_name='Excel_BaseDatos_RTN', startcol=4, startrow=42, index=False, header=False)
        # #--------------------------------------------------------------------------------------------------------------------------
            pd.DataFrame([RTN08_OyM]).to_excel      (writer, sheet_name='Excel_BaseDatos_RTN', startcol=4, startrow=44, index=False, header=False)
            pd.DataFrame([RTN08_OyM1]).to_excel     (writer, sheet_name='Excel_BaseDatos_RTN', startcol=4, startrow=45, index=False, header=False)
            pd.DataFrame([RTN08_IuB]).to_excel      (writer, sheet_name='Excel_BaseDatos_RTN', startcol=4, startrow=46, index=False, header=False)
            pd.DataFrame([RTN08_s1]).to_excel       (writer, sheet_name='Excel_BaseDatos_RTN', startcol=4, startrow=47, index=False, header=False)
            pd.DataFrame([RTN08_s1_5g]).to_excel    (writer, sheet_name='Excel_BaseDatos_RTN', startcol=4, startrow=48, index=False, header=False)

        mostrarRTN = pd.DataFrame(pd.read_excel('opt/980_Excel_BaseDatos_RTNs_IF_SERVICE_LAST28.xlsx'))
        mostrarRTN.to_csv('opt/980_BD_RTNs.csv', index=None, header=True)
        tranformacion_excel_RTN = pd.DataFrame(pd.read_csv('opt/980_BD_RTNs.csv'))
# # #--------------------------------------------------------------------------------------------------------------------------
# # #------------------------------------------------------------------------------
# # #TRANSFORMACION DE ARCHIVO EXCEL A CSV  para ser manipulado por jinja2
# mostrarRTN = pd.DataFrame(pd.read_excel('opt/Excel_BaseDatos_RTNs.xlsx'))
# mostrarRTN.to_csv('opt/BD_RTNs.csv', index=None, header=True)
# tranformacion_excel_RTN = pd.DataFrame(pd.read_csv('opt/BD_RTNs.csv'))
#------------------------------------------------------------------------------
# MANIPULACION JINJA2 TEMPLATE + SOURCE FILE ( RTN )

source_file_RTN = 'opt/980_BD_RTNs.csv'
RTN_Template_file ='templates/final_template_jinja_interfaces_910_RTNs_csv.j2'

with open (RTN_Template_file) as f_rtn:
        RTN_Template_file = Template(f_rtn.read(), keep_trailing_newline=True)

interface_configs_rtn = ""

with open(source_file_RTN) as s_rtn:
    reader_rtn = csv.DictReader(s_rtn)
    for row in reader_rtn:
        interface_config_rtn  = RTN_Template_file.render(
            name = row['name'],
            vlan = row['vlan'],
            description = row['description'],
            vpn_instance = row['vpn_instance'],
            ip_address = row['ip_address'],
            troncal = row['troncal'],
        )
        interface_configs_rtn+= interface_config_rtn

with open(f'980C_RTN_CONFIG_FINAL_{nombre_router}.txt','w') as lectura_rtn:
        lectura_final_rtn = lectura_rtn.write(interface_configs_rtn)

print(Fore.GREEN+Style.BRIGHT,f"CONFIGURACION PARA {nombre_router} RTN OK", end="")
print(Style.RESET_ALL)
##-----------------------------------------------------------------------------------