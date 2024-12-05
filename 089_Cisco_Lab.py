import json
import threading
import re
from netmiko import ConnectHandler, NetMikoAuthenticationException, NetMikoTimeoutException, NetmikoBaseException
from netmiko.exceptions import NetMikoTimeoutException, AuthenticationException, SSHException
from concurrent.futures import ThreadPoolExecutor
import time
from queue import Queue, Empty

hosts = 'hosts_cisco.txt'

def conexion_equipos(equipos):
    try:
        device_connect  = {
        "device_type": 'cisco_ios',
        "ip": equipos,
        "username":"cisco",
        "password":"cisco",}
        Connection = ConnectHandler(**device_connect)
        return print(Connection.find_prompt())
    
    except (AuthenticationException):
        device_connect_otros  = {
        "device_type": 'cisco_ios',
        "ip": equipos,
        "username":"cisco",
        "password":"cisco123",}
        Connection = ConnectHandler(**device_connect_otros)
        print("problema con user/pass en el equipo:", equipos, "intentando con credenciales locales")
        return print(Connection.find_prompt())

    except (NetMikoTimeoutException):
        print("el equipo :", equipos, "encuentra apagado o inalcanzable")
    finally:
        if Connection:
            Connection.disconnect()

with open(hosts, 'r') as read_file:
     lines = read_file.readlines()

with ThreadPoolExecutor(max_workers=10) as executor:
    for lines in lines:
        try:
            future = executor.submit(conexion_equipos, lines)
        except Exception as e:
            print("error en la tarea")
