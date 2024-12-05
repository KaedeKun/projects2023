from netmiko import ConnectHandler
import pandas as pd
import xlsxwriter

path='Inventario_equipo.xlsx'

direccion = input('Ingrese IP de router: ')
usuario = input('Ingrese usuario de logueo: ')
password = input('Ingrese password: ')


device_config = {
    "device_type": "huawei",
    "ip": direccion,
    "username": usuario,
    "password": password,
    "global_delay_factor": .5
}
Connection = ConnectHandler(**device_config)

screen = Connection.send_command("screen-length 0 temporary")
version = Connection.send_command("display version")
arp = Connection.send_command("display arp all ")
config_actual = Connection.send_command("display current configuration")
tabla_ip = Connection.send_command("display ip interface brief")

df1 = pd.DataFrame([version])
df2 = pd.DataFrame([arp])
df3 = pd.DataFrame([config_actual])
df4 = pd.DataFrame([tabla_ip])

pd.set_option('display.max_column', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_seq_items', None)
pd.set_option('display.max_colwidth', 100)
pd.set_option('expand_frame_repr', True)

with pd.ExcelWriter(path) as writer:
     df1.to_excel(writer, sheet_name="version", startcol=0, startrow=0, index=False)
     df2.to_excel(writer, sheet_name="tabla ARP", startcol=0, startrow=0, index=False)
     df3.to_excel(writer, sheet_name="running config", startcol=0, startrow=0, index=False)
     df4.to_excel(writer, sheet_name="Tabla IP", startcol=0, startrow=0, index=False)

print('Archivo Generado.')