import requests
from pythonping import ping
from rich.pretty import pprint
from rich.console import Console
import re
import json
from rich.theme import Theme
from netmiko import ConnectHandler, NetMikoAuthenticationException, NetMikoTimeoutException, NetmikoBaseException
from credenciales import user_radius, pass_radius, user_without_radius, pass_without_radius, LIBRE_TOKEN, LIBRENMS_URL
from concurrent.futures import ThreadPoolExecutor

custom_theme = Theme({'success': 'green', 'error': 'bold red','informational' : 'bold white'})

console = Console(theme=custom_theme)

response = requests.get(
        LIBRENMS_URL, headers={"X-Auth-Token": LIBRE_TOKEN}
    )
raw_list = response.json()

# MODELO OBTENIDO DE LIBRENMS, SEGUN DESCRIPCION ( ESPECIALMENTE EQUIPOS 910B-D)
#-----------------------------------------------------------
patron_huawei = r"(?<=HUAWEI\s).*"
patron_sin = r"ATN(.*)"
def modelo_especial():
    for aa in raw_list["devices"]:
        equipos = aa['sysDescr']
        patron_sin = r"Ltd.\r\n(.*)"
        limpio = equipos.replace("\r \n," ""," ")
        salida_temp_sin = re.search(patron_sin, limpio)
        if salida_temp_sin:
            return salida_temp_sin.group(1)[0:-3]

#------------------------------------------------------------
# FUNCION DE INGRESO AL DISPOSITIVO 1ER INTENTO CON USUARIO RADIUS E INTENTO CON CUENTA LOCAL
#------------------------------------------------------------
def ssh_list(device_hostname, device_model, device_sysname):
    try:
        device_config_radius = {
            "device_type": "huawei_vrpv8",
            "ip": device_hostname,
            "username": user_radius,
            "password": pass_radius,
            "global_delay_factor": .2,}
        Connection_radius = ConnectHandler(**device_config_radius)
        console.print(':green_circle:', Connection_radius.find_prompt(), "Modelo", device_model, style='success')
    except NetMikoAuthenticationException:
        device_config_without_radius = {
            "device_type": "huawei_vrpv8",
            "ip": device_hostname,
            "username":user_without_radius,
            "password":pass_without_radius,
            "global_delay_factor": .2,}
        Connection_sin_radius = ConnectHandler(**device_config_without_radius)
        console.print(f':red_square:',':thinking_face:',"Fallo de autenticación al equipo: ", device_sysname.upper(),"Intentando con credenciales locales........", style="bold red3")
        console.print(':green_circle:', "listo, ahora si!", Connection_sin_radius.find_prompt(), "Modelo", device_model, style='success')
    except NetMikoTimeoutException:
            console.print(f':red_square:',':poop:'," El equipo : ",device_sysname.upper(),"Se ecuentra inalcanzable, posiblemente no exista", style="bold red3")
    except Exception as e:
            console.print(f':red_square:',':poop:'," Error indeterminado")
#------------------------------------------------------------
# def ejecucion_ping(device_hostname, device_name):
#     # EL response.success ES = TRUE O FALSE
#     list_ping = ping(device_hostname, count=1)
#     for response in list_ping:
#         if response == response.success:
#              return device_hostname
#------------------------------------------------------------

#------------------------------------------------------------
# EJECUCION DEL SCRIPT CON MAX_WORERS = CANTIDAD DE THREAD
# LA SALIDA NO ES SECUENCIAL DEBIDO A QUE CADA THREAD TRATA DEL PROCESO DE MANERA DIFERENTE Y PUEDE RESPONDER ORDEN DISCONTIGUOS
#------------------------------------------------------------
with ThreadPoolExecutor(max_workers=10) as executor:
    for items in raw_list["devices"]:
        device_hostname = items["hostname"]
        device_sysname = items["sysName"]
        sys_descr = items["sysDescr"]
        if bool(re.search(patron_huawei, sys_descr)) == True:
            modelo_equipo = items["hardware"]
        else:
            modelo_equipo = modelo_especial()
        try:
            future = executor.submit(ssh_list, device_hostname, modelo_equipo, device_sysname)
        except Exception as e:
            print(f'error al enviar la Tarea al Thread: {e}')