from netmiko import ConnectHandler
import pandas as pd
import xlsxwriter
import pandas.io.formats.excel
pandas.io.formats.excel.ExcelFormatter.header_style = None

path = 'temp_inventario_final.xlsx'

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

#COMANDOS REQUERIDOS PARA INVENTARIO ANTERIOR-ACTIVIDAD:
#
#VV display version                #display ospf peer brief
#VV display arp all                #display bfd session all
#VV dis current configuration      #display bgp vpnv4 all peer
#VV display interface brief        
#dis ip interface brief
#dis lldp neighbor


screen                  = Connection.send_command("screen-length 0 temporary")
version                 = Connection.send_command("display version")
tabla_arp               = Connection.send_command("display arp all ")
interface_brief         = Connection.send_command("display interface brief")
config_actual           = Connection.send_command("display current configuration")
interface_ip_brief      = Connection.send_command("display ip int brief")
lldp_neighbors          = Connection.send_command("display lldp neighbor")
ospf_peer               = Connection.send_command("display ospf peer brief")
bfd_session             = Connection.send_command("display bfd session all")
bgp_peer                = Connection.send_command("display bgp vpnv4 all peer")

with open('temp_bgp_peer.txt', 'w', encoding='utf-8') as bgp_nei:
    final_bgp_peer = bgp_nei.write(bgp_peer)

with open('temp_texto_version.txt','w', encoding='utf-8') as v:
    final_version = v.write(version)

with open('temp_tabla_arp.txt', 'w', encoding='utf-8') as arp:
    final_tabla_arp = arp.write(tabla_arp)

with open('temp_tabla_ip.txt','w', encoding='utf-8') as t:
    final_tabla_ip = t.write(interface_brief)

with open('temp_configuracion_actual.txt', 'w', encoding='utf-8') as act_config:
    final_configuracion_actual = act_config.write(config_actual)

with open('temp_interface_brief.txt', 'w', encoding='utf-8') as int_brief:
    final_interface_brief = int_brief.write(interface_ip_brief)

with open('temp_lldp_neighbors.txt', 'w', encoding='utf-8') as lldp_nei:
    final_lldp_neighbors = lldp_nei.write(lldp_neighbors)

with open('temp_ospf_peers.txt', 'w', encoding='utf-8') as ospf_nei:
    final_ospf_peer = ospf_nei.write(ospf_peer)   

with open('temp_bfd_session.txt', 'w', encoding='utf-8') as bfd_sess:
    final_bfd_session = bfd_sess.write(bfd_session)

df0 = pd.read_table('temp_texto_version.txt')
df1 = pd.read_table('temp_texto_version.txt')
df2 = pd.read_table('temp_tabla_arp.txt')
df3 = pd.read_table('temp_tabla_ip.txt')
df4 = pd.read_table('temp_configuracion_actual.txt')
df5 = pd.read_table('temp_interface_brief.txt')
df6 = pd.read_table('temp_lldp_neighbors.txt')
df7 = pd.read_table('temp_ospf_peers.txt')
df8 = pd.read_table('temp_bfd_session.txt')
df9 = pd.read_table('temp_bgp_peer.txt', on_bad_lines='skip')

with pd.ExcelWriter(path) as writer:
    df0.to_excel(writer, startcol=0, startrow=2, sheet_name='Version', header=True, index=False)
    df2.to_excel(writer, startcol=0, startrow=2, sheet_name='Tabla_ARP', index=False)
    df3.to_excel(writer, startcol=0, startrow=2, sheet_name='Tabla_IP', index=False)
    df4.to_excel(writer, startcol=0, startrow=2, sheet_name='Current_Conf', index=False)
    df5.to_excel(writer, startcol=0, startrow=2, sheet_name='Interface_brief', index=False)
    df6.to_excel(writer, startcol=0, startrow=2, sheet_name='lldp neighbors', index=False)
    df7.to_excel(writer, startcol=0, startrow=1, sheet_name='Ospf peers', index=False)
    df8.to_excel(writer, startcol=0, startrow=1, sheet_name='BFD Session', index=False)
    df9.to_excel(writer, startcol=0, startrow=1, sheet_name='BGP peers', index=False)

print('archivos generados.')